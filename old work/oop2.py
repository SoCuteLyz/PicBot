import cv2 as cv
import numpy as np

class searchPic :
    def __init__(self,main_img,temp_img) -> None:
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def find(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        # main เป็นตัวหลัก temp เป็นตัวที่ต้องการค้นหา
        min,max,minloc,maxloc = cv.minMaxLoc(result)
        
        accuracy = 0.9
        
        location = np.where(result >= accuracy)
        # การหาตำแหน่งภาพที่ต้องการด้วย numpy และ where
        locations = list(zip(*location[::-1]))
        # print(locations)
        if locations:
            height = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
            
            # print(height)
            # print(width)
            
            for l in locations:
                buttomRight = (l[0]+width,l[1]+height)
                cv.rectangle(self.main_img,l,buttomRight,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
                
                font = cv.FONT_HERSHEY_PLAIN
                
                position = (l[0],l[1]-15)
                fontsize = 2
                color = ((255, 255, 67))
                cv.putText(self.main_img,"circle",position,font,fontsize,color,thickness=1)
                
        cv.imshow('result',self.main_img)
        cv.waitKey()
        cv.destroyAllWindows()
        
        
        

findPic = searchPic('../basic_venv/image/bg3-main.png','../basic_venv/image/bg3.png')
findPic.find()
        