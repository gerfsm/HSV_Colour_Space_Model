# author: gerfsm

import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2 as cv

RGB_img = 'Path to the folder where we have the segmented images'
Hue_Histogram = 'Path to the folder where we will save the HSV histograms'

images = os.listdir(RGB_img)

def HSV_Histogram():
    list=[]
    for i in images:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i) 
            doc = RGB_img + '/' + name + '.jpg' 
            final = Hue_Histogram + '/' + name + '_Histogram' + '.jpg'
            img = cv.imread(doc)

            cv.imshow('RGB', img)
            cv.waitKey(0)

            img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

            colour = cm.get_cmap('hsv')

            h = img[:,:,0]
            print(h.reshape(-1))
            n, bins, patches = plt.hist(h.reshape(-1),256,[0,255])

            nbins = bins/256

            for c, p in zip(nbins, patches):
                plt.setp(p, 'facecolor', colour(c))

            plt.show()
            
            
            
            
HSV_Histogram()

