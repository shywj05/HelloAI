import cv2


gray = cv2.imread('3_4.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('black', gray)
print(gray)

cv2.waitKey(0)
cv2.destroyAllWindows()