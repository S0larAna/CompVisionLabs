import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('webcam-recording.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Camera with Red Cross', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    output_video.write(frame)

cap.release()
cv2.destroyAllWindows()