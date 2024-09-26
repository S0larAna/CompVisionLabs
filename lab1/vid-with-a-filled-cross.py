import cv2
import numpy as np

red = np.array([0, 0, 255])
green = np.array([0, 255, 0])
blue = np.array([255, 0, 0])

def closest_color(pixel):
    dist_red = np.linalg.norm(pixel - red)
    dist_green = np.linalg.norm(pixel - green)
    dist_blue = np.linalg.norm(pixel - blue)

    min_dist = min(dist_red, dist_green, dist_blue)

    if min_dist == dist_red:
        return (0, 0, 255)
    elif min_dist == dist_green:
        return (0, 255, 0)
    else:
        return (255, 0, 0)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    center_x, center_y = width // 2, height // 2
    central_pixel = frame[center_y, center_x]
    dist_red = np.linalg.norm(central_pixel - red)
    dist_green = np.linalg.norm(central_pixel - green)
    dist_blue = np.linalg.norm(central_pixel - blue)

    cross_color = closest_color(central_pixel)
    cross_thickness = 25
    cross_size = min(width, height) // 5

    cv2.rectangle(frame,
                  (center_x - cross_size, center_y - cross_thickness // 2),
                  (center_x + cross_size, center_y + cross_thickness // 2),
                  cross_color, -1)

    cv2.rectangle(frame,
                  (center_x - cross_thickness // 2, center_y - cross_size),
                  (center_x + cross_thickness // 2, center_y + cross_size),
                  cross_color, -1)

    cv2.imshow('Camera with Red Cross', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()