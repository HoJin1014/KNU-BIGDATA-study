# 파일명: image_generation_train_sub.py

# imports
import os
import io
import shutil
import numpy as np
import base64

import tensorflow as tf
from tensorflow.python.keras import models
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

from PIL import Image
import imageio
import logging

logging.getLogger('PIL').setLevel(logging.WARNING)

logging.info(f'[hunmin log] tensorflow ver : {tf.__version__}')

# 사용할 gpu 번호를 적는다.
# os.environ["CUDA_VISIBLE_DEVICES"]='0'

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_visible_devices(gpus, 'GPU')
        logging.info('[hunmin log] gpu set complete')
        logging.info('[hunmin log] num of gpu: {}'.format(len(gpus)))
    
    except RuntimeError as e:
        logging.info('[hunmin log] gpu set failed')
        logging.info(e)

# Content feature을 뽑을 층
content_layers = ['block5_conv2'] 

# Style feature을 뽑을 층
style_layers = ['block1_conv1',
                'block2_conv1',
                'block3_conv1', 
                'block4_conv1', 
                'block5_conv1'
               ]

num_content_layers = len(content_layers)
num_style_layers = len(style_layers)

def exec_train(tm):
    
    logging.info('[hunmin log] the start line of the function [exec_train]')
    logging.info('[hunmin log] tm.train_data_path : {}'.format(tm.train_data_path))
    
    # 저장 파일 확인
    list_files_directories(tm.train_data_path)
    
    ###########################################################################
    ## 1. 데이터셋 준비(Data Setup)
    ###########################################################################
    
    data_path = tm.train_data_path + '/dataset'
    list_files_directories(data_path)
    
    # 이미지 경로
    content_path = data_path + '/view.jpg'
    style_path = data_path + '/mountain.jpg'
    
    logging.info('[hunmin log] content_path : {}'.format(content_path))
    logging.info('[hunmin log] style_path : {}'.format(style_path))
    
    # 스타일 이미지 저장
    style_save_path = os.path.join(tm.model_path, 'mountain.jpg')
    shutil.copyfile(style_path, style_save_path)
    
    list_files_directories(tm.model_path)
    
    # 스타일 전이 수행
    images, losses = run_style_transfer(content_path, 
                                    style_path, num_iterations=1000)
    
    logging.info('[hunmin log] losses : {}'.format(losses))
    
    ###########################################################################
    ## 플랫폼 시각화
    ###########################################################################  
    
    plot_metrics(tm, losses)
    
    
    logging.info('[hunmin log]  the finish line of the function [exec_train]')


def exec_init_svc(im):
    style_path = os.path.join(im.model_path, 'mountain.jpg')
    return { 'style_path': style_path }


def exec_inference(df, params, batch_id):
    ###########################################################################
    ## 4. 추론(Inference)
    ###########################################################################
    
    logging.info('[hunmin log] the start line of the function [exec_inference]')
    
    # 스타일 이미지 경로 불러오기
    style_path = params['style_path']
    logging.info('[hunmin log] style_path : {}'.format(style_path))
    
    logging.info('[hunmin log] base64 image read')
    image_bytes = io.BytesIO(base64.b64decode(df.iloc[0, 0]))
    
    # compute grads & loss
    images, losses = run_style_transfer(image_bytes, style_path)
    
    # # save image
    # target_path = os.path.join(hunmin_dir, 'TRANSFORM.jpg')
    # Image.fromarray(images[-1]).save(target_path)
    
    # inverse transform
    result = {'inference' : "Style Transfer Complete"}
    logging.info('[hunmin log] result : {}'.format(result))

    return result



# 저장 파일 확인
def list_files_directories(path):
    # Get the list of all files and directories in current working directory
    dir_list = os.listdir(path)
    logging.info('[hunmin log] Files and directories in {} :'.format(path))
    logging.info('[hunmin log] dir_list : {}'.format(dir_list))


###########################################################################
## exec_train(tm) 호출 함수 
###########################################################################

###########################################################################
## 2. 데이터 전처리(Data Preprocessing)
###########################################################################
# 스타일 전이 전처리
# 이미지 크기 조정, 형식 변환
def preprocessing_style_transfer(file):
    img = Image.open(file)
    img = img.resize((int(img.size[0]*0.5),int(img.size[1]*0.5)), Image.ANTIALIAS)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array,axis=0)
    input_img = preprocess_input(img_array) #prepare image for model vgg16
    return input_img

###########################################################################
## 3. 학습 모델 훈련(Train Model)
###########################################################################
# 모델 정의
def get_model():
    vgg = VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False
    
    style_outputs = [vgg.get_layer(name).output for name in style_layers]
    content_outputs = [vgg.get_layer(name).output for name in content_layers]
    model_outputs = style_outputs + content_outputs

    return models.Model(vgg.input, model_outputs)

# 콘텐츠 이미지 손실 계산
def get_content_loss(base_content, target):
    return tf.reduce_mean(tf.square(base_content - target))

# gram matrix 계산 함수(스타일 이미지 손실 계산에 이용)
def gram_matrix(input_tensor):
    # We make the image channels first 
    channels = int(input_tensor.shape[-1])
    a = tf.reshape(input_tensor, [-1, channels])
    n = tf.shape(a)[0]
    gram = tf.matmul(a, a, transpose_a=True)
    return gram / tf.cast(n, tf.float32)

# 스타일 손실 계산
def get_style_loss(base_style, gram_target):
    height, width, channels = base_style.get_shape().as_list()
    gram_style = gram_matrix(base_style)
    return tf.reduce_mean(tf.square(gram_style - gram_target))

# 이미지를 로드하고 네트워크를 통해 전달하는 함수를 정의한 다음
# 모델에서 콘텐츠 및 스타일 특징 표현을 출력한다.
def get_feature_representations(model, content_path, style_path):

    content_image = preprocessing_style_transfer(content_path)
    style_image = preprocessing_style_transfer(style_path)
    
    # 원하는 콘텐츠 이미지와 기본 입력 이미지를 네트워크에 전달한다.
    # 이것은 모델의 중간에서 선택한 레이어 출력을 반환한다.
    style_outputs = model(style_image)
    content_outputs = model(content_image)
    
    # 모델의 출력(style_outputs 및 content_outputs)은
    # style_feature를 추출할 출력 5개 + content_feature를 추출할 출력 1개로 
    # 이루어져 있으므로 이를 스타일 특징, 콘텐츠 특징으로 반환한다.
    style_features = [style_layer[0] for style_layer in style_outputs[:num_style_layers]]
    content_features = [content_layer[0] for content_layer in content_outputs[num_style_layers:]]
    return style_features, content_features

# 손실 계산
def compute_loss(model, loss_weights, init_image, gram_style_features, content_features):
    style_weight, content_weight = loss_weights

    model_outputs = model(init_image)

    style_output_features = model_outputs[:num_style_layers]
    content_output_features = model_outputs[num_style_layers:]

    style_score = 0
    content_score = 0
    
    weight_per_style_layer = 1.0 / float(num_style_layers)
    for target_style, comb_style in zip(gram_style_features, style_output_features):
        style_score += weight_per_style_layer * get_style_loss(comb_style[0], target_style)
    
    weight_per_content_layer = 1.0 / float(num_content_layers)
    for target_content, comb_content in zip(content_features, content_output_features):
        content_score += weight_per_content_layer * get_content_loss(comb_content[0], target_content)

    style_score *= style_weight
    content_score *= content_weight

    loss = style_score + content_score 
    return loss, style_score, content_score

# 가중치 계산
def compute_grads(cfg):
    with tf.GradientTape() as tape: 
        all_loss = compute_loss(**cfg)

    total_loss = all_loss[0]
    return tape.gradient(total_loss, cfg['init_image']), all_loss

# 가중치와 손실을 계산하는 과정에서 norm_means를 적용시켰던 데이터를 이미지로 변환한다.
def deprocess_img(processed_img):
    x = processed_img.copy()
    if len(x.shape) == 4:
        x = np.squeeze(x, 0)
    assert len(x.shape) == 3, ("Input to deprocess image must be an image of "
                             "dimension [1, height, width, channel] or [height, width, channel]")
    if len(x.shape) != 3:
        raise ValueError("Invalid input to deprocessing image")
    # perform the inverse of the preprocessing step
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]

    x = np.clip(x, 0, 255).astype('uint8')
    return x

# 스타일 전이 수행
def run_style_transfer(content_path, 
                       style_path,
                       num_iterations=1000,
                       content_weight=1e3, 
                       style_weight=1e-2): 
    model = get_model()
    for layer in model.layers:
        layer.trainable = False
    
    # style_features 5개, content_features 1개
    style_features, content_features = get_feature_representations(model, content_path, style_path)
    gram_style_features = [gram_matrix(style_feature) for style_feature in style_features]
    
    init_image = preprocessing_style_transfer(content_path)
    init_image = tf.Variable(init_image, dtype=tf.float32)
    
    opt = tf.optimizers.Adam(learning_rate=5, beta_1=0.99, epsilon=1e-1)
    
    best_loss, best_img = float('inf'), None
    
    loss_weights = (style_weight, content_weight)
    cfg = {
        'model': model,
        'loss_weights': loss_weights,
        'init_image': init_image,
        'gram_style_features': gram_style_features,
        'content_features': content_features
    }
    
    # norm_means는 불러온 모델(VGG19에 imageNet가중치)에서 학습시켰던 이미지의 채널별 픽셀 평균값이다.
    # 평균을 알면 모든 픽셀 값에서 빼서 중심이 0에 오도록 할 수 있다.
    # 이는 훈련 속도와 정확도를 높이는데 도움이 된다.
    norm_means = np.array([103.939, 116.779, 123.68])
    min_vals = -norm_means
    max_vals = 255 - norm_means
    
    # 생성한 이미지 저장
    generated_images = np.expand_dims(deprocess_img(init_image.numpy()), axis=0)
    losses = []
    
    for i in range(1, num_iterations+1):
        grads, all_loss = compute_grads(cfg)
        loss, style_score, content_score = all_loss
        opt.apply_gradients([(grads, init_image)])
        # 범위를 벗어나는 값은 버린다.
        clipped = tf.clip_by_value(init_image, min_vals, max_vals)
        init_image.assign(clipped)
        if i % 10 == 0:
            image = np.expand_dims(deprocess_img(init_image.numpy()), axis=0)
            generated_images = np.concatenate((generated_images, image), axis=0)
        losses.append(loss.numpy())
    
    return generated_images, losses


# 시각화
def plot_metrics(tm, losses):
    loss_list = losses
    for step, loss in enumerate(loss_list):
        metric={}
        metric['accuracy'] = 0
        metric['loss'] = loss
        metric['step'] = step
        tm.save_stat_metrics(metric)
        
    logging.info('[hunmin log] loss curve plot for platform')