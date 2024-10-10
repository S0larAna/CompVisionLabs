import cv2
import numpy as np

cap = cv2.VideoCapture(0) # инициализируем камеру

while True:
    ret, frame = cap.read() # считываем кадр
    if not ret:
        break
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # переводим в цветовое пространство HSV
    lower_red1 = np.array([0, 125, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 125, 100])
    upper_red2 = np.array([179, 255, 255])
    threshold = cv2.inRange(hsvFrame, lower_red1, upper_red1) + cv2.inRange(hsvFrame, lower_red2, upper_red2) # создаем маску
    # cv2.imshow("", hsvFrame)s
    # cv2.imshow('Camera with Red Mask', threshold) # показываем
    kernel = np.ones((5, 5)) # создаем ядро для морфологических операций
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    red_object = cv2.bitwise_and(frame, frame, mask=closing) # применяем маску к кадру
    # cv2.imshow('Morphological Transformations', red_object)
    moments = cv2.moments(closing)
    area = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']
    # print(f"area={area}")
    # print(f"m01={m01}")
    # print(f"m10={m10}")
    if area> 500:
        cx = int(m10 / area)
        cy = int(m01 / area)
        cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
        y, x = np.nonzero(closing)
        left, top = np.min(x), np.min(y)
        right, bottom = np.max(x), np.max(y)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()