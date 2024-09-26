import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    center_x, center_y = width // 2, height // 2

    cross_color = (0, 0, 255)
    cross_thickness = 25
    cross_size = min(width, height) // 5

    cv2.rectangle(frame,
                  (center_x - cross_size, center_y - cross_thickness // 2),
                  (center_x + cross_size, center_y + cross_thickness // 2),
                  cross_color, 2)

    cv2.rectangle(frame,
                  (center_x - cross_thickness // 2, center_y - cross_size),
                  (center_x + cross_thickness // 2, center_y + cross_size),
                  cross_color, 2)

    cv2.imshow('Camera with Red Cross', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()