import cv2

img1=cv2.imread(r'happy-cat.bmp', 1)
cv2.namedWindow('Display window', cv2.WINDOW_FREERATIO)
cv2.imshow('Display window', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()