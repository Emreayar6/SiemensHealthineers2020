import cv2
import numpy as np
import pyautogui
import time

while True:
    img = np.array(pyautogui.screenshot(region = (380, 300, 320, 220)))


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame = img
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yellow color
    low_yellow = np.array([17, 50, 50])
    high_yellow = np.array([25, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    median = cv2.medianBlur(yellow, 15)

    hsv_frame2 = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
    yellow_mask2 = cv2.inRange(hsv_frame2, low_yellow, high_yellow)

    kernel = np.ones((5,5),np.uint8)

    #diolation = cv2.dilate(yellow_mask2,kernel,iterations=1)



    cv2.imshow("yellow2", yellow_mask2)

    #cv2.imshow("frame", frame)

    cv2.imshow("median", median)

    t = 0
    for i in yellow_mask2.tolist():
        sliced = i[slice(0,320,32)]


        #time.sleep(5)
        if 255 in sliced:
            left_side = sliced[0:sliced.index(255)+1].count(0)
            right_side = sliced[sliced.index(255):10].count(0)
            t +=1
    try :
        if t > 50 and 0.75 <= (left_side/right_side) <= 1.50 :
            print("You are on the line!!")

        elif t > 50 and (left_side/right_side) < 0.75 :
            print("You are on the right side of the road.")

        elif t > 50 and 1.50 < (left_side/right_side)  :
            print("You are on the left side of the road.")

    except ZeroDivisionError:
        pass

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()