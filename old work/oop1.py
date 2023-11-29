import cv2 as cv
import numpy as np
# คือตั้งชื่อเล่นให้ฟังก์ขัน

class Picture:
    def __init__(self,main_img,temp_img) -> None:
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def findpic(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCORR_NORMED)
        min,max,minloc,maxloc = cv.minMaxLoc(result)
        print(max)
        print(maxloc)
        
        accuracy = 0.9
        
        if max >= accuracy:
            topleft = maxloc
            print(self.temp_img.shape)
            
            height = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
            
            buttonright = (topleft[0]+width,topleft[1]+height)
            cv.rectangle(self.main_img,topleft,buttonright,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
            font = cv.FONT_HERSHEY_DUPLEX
            
            
            position = (topleft[0],topleft[1]+15)
            fontsize = 0.5
            color = (255,0,255)
            cv.putText(self.main_img,"TEST_TEXT",position,font,fontsize,color,thickness=2)
            # การใส่ข้อความลงไป
            
            
            
            cv.imshow('result',self.main_img)
            cv.waitKey()
            cv.destroyAllWindows()
            
        