# 파일명: text_generation_train_sub.py

# Imports
import tensorflow as tf
import numpy as np
import os
import pickle
import logging

logging.info(f'[hunmin log] tensorflow ver : {tf.__version__}')

# 사용할 gpu 번호를 적는다.
os.environ["CUDA_VISIBLE_DEVICES"]='0'

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_visible_devices(gpus, 'GPU')
        logging.info('[hunmin log] gpu set complete')
        logging.info('[hunmin log] num of gpu: {}'.format(len(gpus)))
    
    except RuntimeError as e:
        logging.info('[hunmin log] gpu set failed')
        logging.info(e)
        
        
def exec_train(tm):
    
    logging.info('[hunmin log] the start line of the function [exec_train]')
    
    logging.info('[hunmin log] tm.train_data_path : {}'.format(tm.train_data_path))
    
    # 저장 파일 확인
    list_files_directories(tm.train_data_path)
    
    ###########################################################################
    ## 1. 데이터셋 준비(Data Setup)
    ###########################################################################
    logging.info('[hunmin log] data load')
    
    path_to_file = os.path.join(tm.train_data_path, 'dataset/shakespeare.txt')
    logging.info('[hunmin log] file path : {}'.format(path_to_file))
    
    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    logging.info('[hunmin log] loaded data check (text[:100]) : {}'.format(text[:100]))
    
    ###########################################################################
    ## 2. 데이터 전처리(Data Preprocessing)
    ###########################################################################
    vocab = sorted(set(text))
    
    # 추론에 사용할 vocab데이터 저장
    with open(os.path.join(tm.model_path, 'vocabulary.p'), 'wb') as f:
        pickle.dump(vocab, f)
    
    # 문자를 id로 변환
    ids_from_chars = tf.keras.layers.experimental.preprocessing.StringLookup(vocabulary=list(vocab), mask_token=None)
    all_ids = ids_from_chars(tf.strings.unicode_split(text, 'UTF-8'))
    ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)

    seq_length = 100
    sequences = ids_dataset.batch(seq_length+1, drop_remainder=True)
    dataset = sequences.map(split_input_target)

    # Batch size
    BATCH_SIZE = 64 * len(gpus) if len(gpus) > 0 else 64
    BUFFER_SIZE = 10000

    dataset = (dataset
            .shuffle(BUFFER_SIZE)
            .batch(BATCH_SIZE, drop_remainder=True)
            .prefetch(tf.data.experimental.AUTOTUNE))
    
    ###########################################################################
    ## 3. 학습 모델 훈련(Train Model)
    ###########################################################################

    # 모델 구축 (Build Model)
    # The embedding dimension
    embedding_dim = 256
    # Number of RNN units
    rnn_units = 1024
    
    
    # 단일 gpu 혹은 cpu학습
    if len(gpus) < 2:
        model = MyModel(
                    # Be sure the vocabulary size matches the `StringLookup` layers.
                    vocab_size=len(ids_from_chars.get_vocabulary()),
                    embedding_dim=embedding_dim,
                    rnn_units=rnn_units)
            
        # 입력 텍스트 다음에 올 문자 중 확률이 가장 높은 문자를 추출해야 하므로 
        # 다중분류에 사용되는 loss를 사용한다.
        loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
        model.compile(optimizer='adam', loss=loss)
        
    # multi-gpu
    else:
        strategy = tf.distribute.MirroredStrategy()
        logging.info('[hunmin log] gpu devices num {}'.format(strategy.num_replicas_in_sync))
        with strategy.scope():
            model = MyModel(
                    # Be sure the vocabulary size matches the `StringLookup` layers.
                    vocab_size=len(ids_from_chars.get_vocabulary()),
                    embedding_dim=embedding_dim,
                    rnn_units=rnn_units)
            
            # 입력 텍스트 다음에 올 문자 중 확률이 가장 높은 문자를 추출해야 하므로 
            # 다중분류에 사용되는 loss를 사용한다.
            loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
            model.compile(optimizer='adam', loss=loss)
            

    # 모델 학습
    # Directory where the checkpoints will be saved
    checkpoint_dir = os.path.join(tm.model_path, 'training_checkpoints')
    
    # 체크포인트 콜백
    checkpoint_prefix = os.path.join(checkpoint_dir, "last_ckpt")
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
                                        filepath=checkpoint_prefix,
                                        save_weights_only=True)
    
    EPOCHS = 50
    history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
    
    logging.info('[hunmin log] model.summary() : ')
    model.summary(print_fn=logging.info)
    
    ###########################################################################
    ## 플랫폼 시각화
    ###########################################################################  
    '''
    plot_metrics(tm, history)
    '''
    
    # 저장 파일 확인
    list_files_directories(tm.model_path)
    
    logging.info('[hunmin log]  the finish line of the function [exec_train]')
    

def exec_init_svc(im):

    logging.info('[hunmin log] im.model_path : {}'.format(im.model_path))
    
    # 저장 파일 확인
    list_files_directories(im.model_path)
    
    ###########################################################################
    ## 학습 모델 준비
    ########################################################################### 
    with open(os.path.join(im.model_path, 'vocabulary.p'), 'rb') as f:
        vocab = pickle.load(f)
        
    # rebuild model
    ids_from_chars = tf.keras.layers.experimental.preprocessing.StringLookup(vocabulary=list(vocab), mask_token=None)
    # The embedding dimension
    embedding_dim = 256
    # Number of RNN units
    rnn_units = 1024
    
    loaded_model = MyModel(
            # Be sure the vocabulary size matches the `StringLookup` layers.
            vocab_size=len(ids_from_chars.get_vocabulary()),
            embedding_dim=embedding_dim,
            rnn_units=rnn_units)
    loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
    loaded_model.compile(optimizer='adam', loss=loss)
    
    # 가장 최근 체크포인트를 호출
    latest = tf.train.latest_checkpoint(os.path.join(im.model_path, 'training_checkpoints'))
    loaded_model.load_weights(latest)
    
    chars_from_ids = tf.keras.layers.experimental.preprocessing.StringLookup(vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None)
    
    # rebuild한 모델을 이용하여 입력 텍스트에 이어지는 텍스트를 예측하는 모델을 반환한다.
    loaded_one_step_model = OneStep(loaded_model, chars_from_ids, ids_from_chars)
    
    return {'model' : loaded_one_step_model}



def exec_inference(df, params, batch_id):
    
    ###########################################################################
    ## 4. 추론(Inference)
    ###########################################################################
    
    logging.info('[hunmin log] the start line of the function [exec_inference]')
    
    ## 학습 모델 준비
    model = params['model']
    
    origin_data = df.iloc[0, 0]
    input_data = tf.constant([origin_data])
    
    logging.info('[hunmin log] data predict')
    # data predict
    # 상태 초기값 : None
    states = None
    prediction = [input_data]
    # 입력 이후 100자 예측
    for n in range(100):
        input_data, states = model.generate_one_step(input_data, states=states)
        prediction.append(input_data)
    
    inference = tf.strings.join(prediction)[0].numpy().decode("utf-8")
    logging.info('[hunmin log] inference : {}'.format(inference))
    
    # inverse transform
    result = {'inference' : inference}
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
def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text

# 모델 객체 정의
class MyModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, rnn_units):
        super().__init__(self)
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(rnn_units,
                                       return_sequences=True,
                                       return_state=True)
        self.dense = tf.keras.layers.Dense(vocab_size)
    
    def call(self, inputs, states=None, return_state=False, training=False):
        x = inputs
        x = self.embedding(x, training=training)
        if states is None:
            states = self.gru.get_initial_state(x)
        x, states = self.gru(x, initial_state=states, training=training)
        x = self.dense(x, training=training)
    
        if return_state:
            return x, states
        else:
            return x

class OneStep(tf.keras.Model):
    def __init__(self, model, chars_from_ids, ids_from_chars, temperature=1.0):
        super().__init__()
        self.temperature = temperature
        self.model = model
        self.chars_from_ids = chars_from_ids
        self.ids_from_chars = ids_from_chars
    
        # Create a mask to prevent "[UNK]" from being generated.
        skip_ids = self.ids_from_chars(['[UNK]'])[:, None]
        sparse_mask = tf.SparseTensor(
            # Put a -inf at each bad index.
            values=[-float('inf')]*len(skip_ids),
            indices=skip_ids,
            # Match the shape to the vocabulary
            dense_shape=[len(ids_from_chars.get_vocabulary())])
        self.prediction_mask = tf.sparse.to_dense(sparse_mask)
  
    @tf.function
    def generate_one_step(self, inputs, states=None):
        # Convert strings to token IDs.
        input_chars = tf.strings.unicode_split(inputs, 'UTF-8')
        input_ids = self.ids_from_chars(input_chars).to_tensor()
    
        # Run the model.
        # predicted_logits.shape is [batch, char, next_char_logits]
        predicted_logits, states = self.model(inputs=input_ids, states=states,
                                              return_state=True)
        # Only use the last prediction.
        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits/self.temperature
        # Apply the prediction mask: prevent "[UNK]" from being generated.
        predicted_logits = predicted_logits + self.prediction_mask
    
        # Sample the output logits to generate token IDs.
        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)
    
        # Convert from token ids to characters
        predicted_chars = self.chars_from_ids(predicted_ids)
    
        # Return the characters and model state.
        return predicted_chars, states

# 시각화
def plot_metrics(tm, history):
    
    # accuracy_list = history.history['accuracy']
    loss_list = history.history['loss']
    
    for step, loss in enumerate(loss_list):
        metric={}
        metric['accuracy'] = 0
        metric['loss'] = loss
        metric['step'] = step
        tm.save_stat_metrics(metric)

    logging.info('[hunmin log] accuracy and loss curve plot for platform')
    