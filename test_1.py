import cv2
import numpy as np

frame = np.zeros((480, 640, 3), dtype=np.uint8)
positions = [(100+i*3, 200) for i in range(190)]

for i, pos in enumerate(positions):
    temp = frame.copy()
    cv2.circle(temp, pos, 20, (0, 255, 0), -1)
    cv2.putText(temp, f"Frame:{i}", (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Sim", temp)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()