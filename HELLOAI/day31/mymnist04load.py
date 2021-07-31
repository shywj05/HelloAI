import tensorflow as tf
import cv2
import numpy as np

model= tf.keras.models.load_model("my_fashion")

img = cv2.imread('baji.jpg', cv2.IMREAD_GRAYSCALE)
img_g = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_AREA)
img_gmi = 255 - img_g  # 색 반전 해서 비교할 수 잇도록 환경설정 
img_out = np.reshape(img_gmi, (1, 28, 28))

predictions = model.predict(img_out)

print(np.argmax(predictions[0]))

cv2.waitKey(0)
cv2.destroyAllWindows()
    
