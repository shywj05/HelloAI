import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images_ori, test_labels) = fashion_mnist.load_data()

train_images, test_images = train_images / 255.0, test_images_ori / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

gray = cv2.imread('baji.jpg', cv2.IMREAD_GRAYSCALE)
bajii = cv2.resize(gray, dsize=(28, 28), interpolation=cv2.INTER_AREA)
iijab = 255 - bajii  # 색 반전 해서 비교할 수 잇도록 환경설정 
img_out = np.reshape(iijab, (1, 28, 28))

predictions = model.predict(bajii)

print(np.argmax(predictions[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()
    
