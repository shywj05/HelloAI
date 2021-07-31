import cv2


img = cv2.imread("lena.jpg", 1)
 
img180 = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("Test Image", img180)
cv2.imwrite("lena_180.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()