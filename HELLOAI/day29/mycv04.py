import cv2


src = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(100, 100), interpolation=cv2.INTER_AREA)

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()