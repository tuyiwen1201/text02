from typing import List, Any, Union

import cv2
import numpy as np
from PIL import Image

def gray_and_label(image):
    # 图片灰度处理和图片范围标定
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(gray, (9, 9))
    _, thresh = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)
    (cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    cv2.drawContours(image, [box], -1, (0, 255, 0), 3) #画图，绿色范围标记
    return box

def pillow_dealwith(imgpath,x1,x2,y1,y2):
    im = Image.open(imgpath)    #PIL库自带方法实现灰度化
    gray_np = im.convert("L")   #PIL库自带方法实现灰度化
    im = im.load()
    Rvalue = []
    Gvalue = []
    Bvalue = []
    grayvalue = []
    #灰度图gary
    data_gray = np.asarray(gray_np)

    for i in range(x1,x2):
        for j in range(y1,y2):
            r,g,b = im[i,j]
            Rvalue.append(r)
            Gvalue.append(g)
            Bvalue.append(b)
            gray = data_gray[i,j]
            grayvalue.append(gray)
    ravg = sum(Rvalue)/len(Rvalue)
    gavg = sum(Gvalue)/len(Gvalue)
    bavg = sum(Bvalue)/len(Bvalue)
    gray = sum(grayvalue)/len(grayvalue)
    return ravg,gavg,bavg,gray

if __name__ == '__main__':
    #文件图片读取
    imgpath = input("请输入图片路径：") #输入图片路径
    image = cv2.imread(imgpath)

    # image = cv2.resize(image,(100,100))
    #图片灰度处理和图片范围标定
    box = gray_and_label(image)
    #荧光图案范围标定显示
    cv2.imshow("Image", image)
    cv2.imwrite("contoursImage2.jpg", image)
    cv2.waitKey(0)
    #平均RGB三色得亮度处理
    Xs = [i[0] for i in box]
    print(Xs)
    Ys = [i[0] for i in box]
    print(Ys)
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    # Bvalue = []
    # Gvalue = []
    # Rvalue = []
    # print(x1,x2,y1,y2)
    # for x in range(x1+7,x2-7):
    #     for y in range(y1+7,y2-7):
    #         b = image.item(x,y,0)
    #         Bvalue.append(b)
    #         g = image.item(x,y,1)
    #         Gvalue.append(g)
    #         r = image.item(x,y,2)
    #         Rvalue.append(r)
    # ravg = sum(Rvalue)/len(Rvalue)
    # gavg = sum(Gvalue)/len(Gvalue)
    # bavg = sum(Bvalue)/len(Bvalue)
    # print("R的平均为",ravg)
    # print("G的平均为", gavg)
    # print("B的平均为", bavg)
    #pillow 处理 R G B和gray值
    ravg,gavg,bavg,gray = pillow_dealwith(imgpath,x1,x2,y1,y2)
    print("R的平均为",ravg)
    print("G的平均为", gavg)
    print("B的平均为", bavg)
    print("灰度值为", gray)





#判断语句
ravg,gavg,bavg,gray = pillow_dealwith(imgpath,x1,x2,y1,y2)
gray = float(gray)
if gray == 119.244:
    print("standard")
elif gray < 119.244:
    print("Lower")
else:
    print("Higher")



