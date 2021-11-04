# author: gerfsm

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import norm
import cv2 as cv
from sklearn import mixture
import scipy.stats as stats

ROIs = # Path to the segmented RoI's
Dist_Histograms = # Path where we will save the HSV histograms with a Gaussian Mixture


            
img = cv.imread(ROIs)
            
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
colour = cm.get_cmap('hsv')
h = img[:,:,0]
print(h.reshape(-1))
            
h_filtered1 = [x for x in h.reshape(-1) if x < 50]
h_filtered2 = [x for x in h.reshape(-1) if x > 135]
h_final = h_filtered2 + h_filtered1
            
h_new = [x + 45 if x < 50 else x - 135 for x in h_final]
            
f= np.ravel(h_new).astype(np.float)
f=f.reshape(-1, 1)
g = mixture.GaussianMixture(n_components=3,covariance_type='full')
g.fit(f)
weights = g.weights_
means = g.means_
covars = g.covariances_

print(weights)

n, bins, patches = plt.hist(f,101,[0,100],density=True)

f_axis = f.copy().ravel()
f_axis.sort()


m = np.argmax(weights)
print(m)
plt.plot(f_axis,weights[m]*stats.norm.pdf(f_axis,means[m],np.sqrt(covars[m])).ravel(), c='black')
            
nbins = bins/181
for c, p in zip(nbins, patches):
    plt.setp(p, 'facecolor', colour(c))
    
plt.ylabel("Frequency")
plt.xlabel("Pixel Intensity")
            
plt.savefig('Dist_Histograms/.......')
plt.show()



                 
