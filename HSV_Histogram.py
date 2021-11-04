# author: gerfsm

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import norm
import cv2 as cv

ROIs = # Path to the RBG RoI's
Dist_Histograms = # Path where we will save the HSV Histograms 


            
img = cv.imread(ROIs)
            
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
colour = cm.get_cmap('hsv')
h = img[:,:,0]
print(h.reshape(-1))
            
h_filtered1 = [x for x in h.reshape(-1) if x < 50]
h_filtered2 = [x for x in h.reshape(-1) if x > 135]
h_final = h_filtered2 + h_filtered1
            
h_new = [x + 45 if x < 50 else x - 135 for x in h_final]
            
mu, std = norm.fit(h_new)
            
n, bins, patches = plt.hist(h_new,101,[0,100],density=True)
            
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
            
nbins = bins/256
for c, p in zip(nbins, patches):
    plt.setp(p, 'facecolor', colour(c))
                
plt.savefig(# Path to save the histograms 'Dist_Histograms/.......')
plt.show()

     


