from windowCapture import *
import cv2 as cv
from myClassbot import *

windows = WindowCapture('Calculator')

# white true เพื่อให้มันทำคำสั่งนี้ตลอดทำให้สามารถจับภาพแบบ realtime ได้
while True :
    
    screen = windows.screenshot()
    search = searchPic(screen,'image/five.png')
    point = search.find(debug=True,text="mynumber")
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    # print(screen)
    # cv.imshow('paint',screen)
    # cv.waitKey()
    # cv.destroyAllWindows()
