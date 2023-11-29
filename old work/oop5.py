import cv2 as cv
import numpy as np

class searchPic :
    def __init__(self,main_img,temp_img) -> None:
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def find(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        # main เป็นตัวหลัก temp เป็นตัวที่ต้องการค้นหา
        
        accuracy = 0.9
        
        location = np.where(result >= accuracy)
        # การหาตำแหน่งภาพที่ต้องการด้วย numpy และ where
        locations = list(zip(*location[::-1]))
        # print(locations)
        height = self.temp_img.shape[0]
        width = self.temp_img.shape[1]
            
            # print(height)
            # print(width)
            
        rectangle = []
        point = []
            
        for l in locations:
                rect = [int(l[0]),int(l[1]),width,height]
                rectangle.append(rect)
                rectangle.append(rect)
                
        rex,weight = cv.groupRectangles(rectangle,groupThreshold=1,eps=0.5)
        exit
        
        if len(rex):
            for (x,y,w,h) in rex:
                print(x,y,w,h)
                topleft = (x,y)
                bottomright = (x+w,y+h)
                cv.rectangle(self.main_img,topleft,bottomright,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
                
                #หาจุดกึ่งกลางของ width ก่อน
                centerX = int(w/2) + x
                centerY = int(h/2) + y
                
                point.append((centerX, centerY))
                cv.drawMarker(self.main_img, (centerX, centerY),color=(255,255,255), thickness=2, markerSize=25, markerType=cv.MARKER_DIAMOND)
                
        cv.imshow('result',self.main_img)
        cv.waitKey()
        cv.destroyAllWindows()
        exit
        
        
mainpic = input("กรุณาเลือกชื่อ 3 ชื่อ ต่อไปนี้ \n1.bg1.jpg\n2.bg2.jpg\n3.bg3-main.png\n")
temppic = input("กรุณาเลือกชื่อ 3 ชื่อต่อไปนี้ \n1.bg1.png\n2.bg2.png\n3.bg3.png\n")
if mainpic != "" and temppic != "":
    findPic = searchPic('../basic_venv/image/bg3-main.png','../basic_venv/image/bg3.png')
    findPic.find()
        