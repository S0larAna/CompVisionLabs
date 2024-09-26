import cv2

cap = cv2.VideoCapture(r"C:\Users\bodya\PycharmProject\CompVisionLabs\ballerina.mp4", cv2.CAP_ANY)
if cap.isOpened():
    print("Successfully opened the video file")
else:
    print("Error opening the video file")
cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print("Width: ", width, "Height: ", height, "FPS: ", fps)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
ret, frame = cap.read()
while ret:
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Display window', grayscale)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    ret, frame = cap.read()