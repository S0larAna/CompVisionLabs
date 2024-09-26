import cv2

image = cv2.imread(r'C:\Users\bodya\PycharmProject\CompVisionLabs\img.jpg')

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
cv2.imshow('Original image', image)

cv2.namedWindow('HSV image', cv2.WINDOW_NORMAL)
cv2.imshow('HSV image', hsv_image)

cv2.waitKey(0)

cv2.destroyAllWindows()