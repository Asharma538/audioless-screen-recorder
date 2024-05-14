import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920,1080)

fourcc = cv2.VideoWriter.fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(SCREEN_SIZE))

fps = 120
prev = 0

count_down = time.time()
print("3")
printed2 = False
printed1 = False
while time.time()<count_down+3:
    if (time.time() > count_down+2) and (not printed1):
        print("1")
        printed1 = True
    elif time.time() > count_down+1 and (not printed2):
        print("2")
        printed2 = True

print("Going Live!")

while True:    
    time_elapsed = time.time() - prev
    img = pyautogui.screenshot()

    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    cv2.waitKey(9)

cv2.destroyAllWindows()
out.release()