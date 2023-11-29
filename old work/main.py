import cv2 as cv

# ใช้ cv เข้าไปอ่านรูปภาพ
main_img = cv.imread('image/main.png',cv.IMREAD_ANYCOLOR)
temp_img = cv.imread('image/temp.png',cv.IMREAD_ANYCOLOR)

# print(main_img)
# print(temp_img)

# print(type(temp_img))
# ใช้ค่า นัมไพล์ ในการอ่าน

result = cv.matchTemplate(main_img,temp_img,cv.TM_CCOEFF_NORMED)
# print(result)


min,max,minloc,maxloc = cv.minMaxLoc(result)
print(maxloc)

accurate = 0.9

if max >= accurate:
    topleft = maxloc
    print(temp_img.shape)
    
    height = temp_img.shape[0]
    width = temp_img.shape[1]
    
    bottomright = (topleft[0]+width,topleft[1]+height)
    
    # วาดจากมุมซ้ายบนไปขวาล่างเป็นสีเหลี่ยม
    cv.rectangle(main_img,topleft,bottomright,color=(97,189,92),thickness=4,lineType=cv.LINE_4)
    
    cv.imshow('result',main_img)
    cv.waitKey()
    cv.destroyAllWindows()