from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np

import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print("google", test_labels[0])

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images_sec = test_images.reshape((10000, 28 * 28))
test_images_sec = test_images_sec.astype('float32') / 255

# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels_sec = to_categorical(test_labels)

# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()  # 신경망구성된 부분 
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)
predictions = model.predict(test_images_sec)

print("predict : ", np.argmax(predictions[0]))
print("google : ", test_labels[0])

o_cnt = 0
x_cnt = 0
for i in range(len(predictions)):
    pred = np.argmax(predictions[i])
    goog = test_labels[i]
    if pred == goog:
        o_cnt += 1
    else:
        x_cnt += 1 
        cv2.imwrite('miss/'+str(goog)+'_'+str(pred)+'_'+str(i)+'.jpg', test_images[i])
print(o_cnt)
print(x_cnt)
        
# cv2.imwrite('test/0.jpg', test_images[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
    
# 테스트 데이터로 정확도 측정하기
test_loss, test_acc = model.evaluate(test_images_sec, test_labels_sec)  # predict
print('test_acc: ', test_acc)





