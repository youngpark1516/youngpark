import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense

#인공신경망 모델 정의
class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.input_layer = Dense(256, activation = 'relu', input_shape=(784,))
        self.hidden_layer = Dense(128, activation = 'relu')
        self.output_layer = Dense(10,activation = 'softmax')

    def call(self, x):
        x = self.input_layer(x)
        x = self.hidden_layer(x)
        output = self.output_layer(x)
        return output

if __name__ == "__main__":
    #모델, 오류함수, 옵티마이저 생성
    model = Model()
    cross_entropy = tf.keras.losses.CategoricalCrossentropy(from_logits=False)
    optimizer = Adam(1e-4)
    # 데이터 불러오기
    mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    #0~255 범위의 값을 0~1로 노멀라이즈
    x_train, x_test = x_train/255.0, x_test/255.0

    #미니 배치 사이즈 설정
    batch_size = 32
    num_train_data = x_train.shape[0]
    num_test_data = x_test.shape[0]

    num_epoch = 10

    for e in range(num_epoch):
        for i in range(num_train_data // batch_size):
            #미니배치 하나만큼 데이터 가져오기
            x_batch = x_train[i*batch_size:(i+1)*batch_size]
            y_batch = y_train[i*batch_size:(i+1)*batch_size]
            x_batch = x_batch.reshape(-1,28*28)
            y_batch = tf.one_hot(y_batch, 10)

            model_param = model.trainable_variables
            with tf.GradientTape() as tape:
                predicts = model(x_batch)
                losses = cross_entropy(predicts, y_batch)
            grads = tape.gradient(losses, model_param)
            optimizer.apply_gradients(zip(grads,model_param))