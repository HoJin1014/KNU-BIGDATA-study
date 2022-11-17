#%%
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

IMAGE_SIZE = (514, 616)
IMAGE_SHAPE = IMAGE_SIZE + (3,)

def get_top_model():
    top_model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(16, (5,5), input_shape=IMAGE_SHAPE),
        tf.keras.layers.ReLU(),
        tf.keras.layers.AveragePooling2D((2, 2)),
        tf.keras.layers.Conv2D(24, (5,5)),
        tf.keras.layers.ReLU(),
        tf.keras.layers.AveragePooling2D((2,2)),
        tf.keras.layers.Conv2D(32, (5,5)),
        tf.keras.layers.ReLU(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(256, activation='relu',
                              kernel_regularizer=tf.keras.regularizers.L2(l2=0.0001)),
        tf.keras.layers.Dropout(.4),
        tf.keras.layers.Dense(16, activation='relu',
                              kernel_regularizer=tf.keras.regularizers.L2(l2=0.0001)),
        tf.keras.layers.Dropout(.3),
        tf.keras.layers.Dense(1, activation='sigmoid',
                              kernel_regularizer=tf.keras.regularizers.L2(l2=0.0001))], name='top_model')
    return top_model

def get_data_agumenter():
    augmenter = tf.keras.Sequential(name='data_augmenter')
    augmenter.add(tf.keras.layers.RandomBrightness(
        0.05, value_range=[-1., 1.]))
    augmenter.add(tf.keras.layers.RandomContrast(0.05))
    augmenter.add(tf.keras.layers.RandomFlip())
    augmenter.add(tf.keras.layers.RandomRotation(0.01))
    augmenter.add(tf.keras.layers.RandomTranslation(0.06, 0.06))
    return augmenter

class Model(tf.keras.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.augmenter = get_data_agumenter()

        #self.base_model = tf.keras.applications.VGG16(
        #    include_top=False, weights='imagenet', input_shape=IMAGE_SHAPE)
        #self.base_model.trainable = False

        self.top_model = get_top_model()

    def call(self, inputs):
        x = self.augmenter(inputs)
        return self.top_model(x)

    @property
    def export_model(self):
        return tf.keras.Sequential(
            [self.get_preprocess_layer(), self.base_model, self.top_model])

    @classmethod
    def get_preprocess_layer(cls):
        return tf.keras.layers.Rescaling(1./127.5, offset=-1, name='rescaling')

model = Model()
train_set = tf.keras.utils.image_dataset_from_directory(
    '../images/test_set', label_mode='binary', color_mode='rgb', image_size=IMAGE_SIZE, batch_size=1)
dev_set = tf.keras.utils.image_dataset_from_directory(
    '../images/dev_set', label_mode='binary', color_mode='rgb', image_size=IMAGE_SIZE, batch_size=1)

preprocess_layer = Model.get_preprocess_layer()
dev_set = dev_set.map(lambda x, y: (preprocess_layer(x), y)
                      ).prefetch(tf.data.AUTOTUNE)
train_set = train_set.map(lambda x, y: (preprocess_layer(x), y)
                          ).prefetch(tf.data.AUTOTUNE)
                          
#%%
epochs = 10
learning_rate = 0.0005

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss=tf.keras.losses.BinaryFocalCrossentropy(
    gamma=2.0, from_logits=False), metrics=[
    tf.keras.metrics.BinaryAccuracy(name='accuracy'),
    tf.keras.metrics.Precision(name='precision'),
    tf.keras.metrics.Recall(name='recall'),
    tf.keras.metrics.RecallAtPrecision(1, name='recall_at_perfect_precision')])

test_date = '20221115_1416'
backup_dir = f'.backup/{test_date}'
log_dir = f'.logs/{test_date}'
ckpt_dir = f'.ckpt/{test_date}'
 #%%
callbacks = [
    tf.keras.callbacks.BackupAndRestore(backup_dir),
    tf.keras.callbacks.TensorBoard(log_dir),
    tf.keras.callbacks.ModelCheckpoint(f'{ckpt_dir}/{{epoch}}', save_weights_only=True)]

model.fit(train_set, epochs=epochs, validation_data=dev_set, callbacks=callbacks)
# %%
