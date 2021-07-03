# author: @gerfsm

import os
import cv2


RGB_img = 'C:/Users/Germano Moreira/Desktop/Histograma/ROIs'
HSV_img = 'C:/Users/Germano Moreira/Desktop/Histograma/HSV_images'

images = os.listdir(RGB_img)

def transform():
    
    list=[]
    for i in images:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i) 
            doc = RGB_img + '/' + name + '.jpg'
            final = HSV_img + '/' + name + '_HSV' + '.jpg'
            image = cv2.imread(doc)
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            cv2.imwrite(final,hsv)
        
        
transform()


        
            
        