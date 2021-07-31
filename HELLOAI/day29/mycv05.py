import cv2


src = cv2.imread("lena.jpg", 1)
 
img90 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)


cv2.imshow("Test Image", img90)

cv2.waitKey(0)
cv2.destroyAllWindows()