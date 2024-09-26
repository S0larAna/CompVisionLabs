import cv2

input_video = cv2.VideoCapture(r"C:\Users\bodya\PycharmProject\CompVisionLabs\ballerina.mp4")

width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = input_video.read()
    if not ret:
        break
    contrast = cv2.convertScaleAbs(frame, alpha=2.0, beta=0)
    output_video.write(contrast)

input_video.release()
output_video.release()