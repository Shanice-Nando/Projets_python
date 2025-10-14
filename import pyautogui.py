import pyautogui
import cv2 as cv
import numpy as np
import time

capture_finie = False
fps = 60
taille_frame = (1366,768)
rec = cv.VideoWriter("test.avi",cv.VideoWriter_fourcc(*"DIVX"), 20.0, taille_frame)

cv.namedWindow("Direct", cv.WINDOW_NORMAL)
cv.resizeWindow("Direct",480,270)
prev =0
while 1:
    image=pyautogui.screenshot()
    now = time.time()
    if now - prev > 1.0/fps:
        prev = now
        image = np.array(image)
        image= cv.cvtColor(image,cv.COLOR_BGR2RGB)
        rec.write(image)
        cv.imshow("Direct",image)
        if cv.waitKey(1) == ord("s"):
            break
            rec.release()
            cv.destroyAllWindows()