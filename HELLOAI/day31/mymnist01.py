import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))

for i in range(100):
    fas = train_labels[i]
    cv2.imwrite('train/'+str(fas)+'_'+str(i)+'.jpg',train_images[i])
    

train_images, test_images = train_images / 255.0, test_images / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
          loss='sparse_categorical_crossentropy',
          metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

predictions = model.predict(test_images)

print(np.argmax(predictions[0]))
print(test_labels[0])

cv2.waitKey(0)
cv2.destroyAllWindows()





    