from windowCapture import *
import cv2 as cv
from myClassbot import *
from pyautogui import click

windows = WindowCapture('WHACK EM ALL - เล่น Whack em all - Poki - Google Chrome')

myMoledata = [
    {
    'mole1':'image/nosemole.jpg',
    'mole2':'image/nosemole1.jpg',
    'mole3':'image/nosemole2.jpg',
    'mole4':'image/nosemole3.jpg'
   },
    {
        
    }
    ]

# white true เพื่อให้มันทำคำสั่งนี้ตลอดทำให้สามารถจับภาพแบบ realtime ได้
while True :
    
    screen = windows.screenshot()
    
    for name,path in myMoledata.items():
        
        search = searchPic(screen,path)
        point = search.find(debug=True,text=name)
    
        for myClick in point:
            click(x=myClick[0],y=myClick[1])
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    # print(screen)
    # cv.imshow('paint',screen)
    # cv.waitKey()
    # cv.destroyAllWindows()
