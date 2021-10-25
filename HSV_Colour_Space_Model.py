# author: @gerfsm


import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import norm
import cv2 as cv
from sklearn import mixture
import scipy.stats as stats

#Path to save Rois
ROIs = '____________________________________________________________'

# Path to the folder where we will save the New Annotations
New_annotation_folder = '___________________________________________'

# Path to the folder where we have the original images
img_folder = '______________________________________________________'

# Path to the folder where we have the annotations (txt) of the original images
ann_folder = '______________________________________________________'


images = os.listdir(img_folder)
annotations = os.listdir(ann_folder)

def segm_crop():
    for i in images:
        name,h = os.path.splitext(i)
        print (name)
        doc = ann_folder + '/' + name + '.txt'
        print (doc)
        with open(doc) as infile:
            contents = infile.readlines()
            img = Image.open(img_folder + '/' + i)
            Results_list=[]
            for ann in range(len(contents)):
                a = contents[ann]
                coords = a.split()
                xmin = int(coords[1])
                ymin = int(coords[2])
                xmax = int(coords[3])
                ymax = int(coords[4])
                final1 = ROIs + '/' + name + '_' + str(xmin) + '.jpg' 
                final2 = New_annotation_folder + '/' + name + '.txt'
                
                img1 = img.crop((xmin, ymin, xmax, ymax))
                img1.save(final1)    
                img2 = cv.imread(final1)
                    
                img2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
                colour = cm.get_cmap('hsv')
                h = img2[:,:,0]
                print(h.reshape(-1))
            
                h_filtered1 = [x for x in h.reshape(-1) if x < 50]
                h_filtered2 = [x for x in h.reshape(-1) if x > 135]
                h_final = h_filtered2 + h_filtered1
            
                h_new = [x + 45 if x < 50 else x - 135 for x in h_final]
            
                f= np.ravel(h_new).astype(np.float64)
                f=f.reshape(-1, 1)
                g = mixture.GaussianMixture(n_components=3,covariance_type='full')
                g.fit(f)
                weights = g.weights_
                means = g.means_
                covars = g.covariances_
                
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

           
                plt.show()

                m = np.argmax(weights)

                media = means[m]
                print(media)

                y = (0.001*(media**2))-(0.2241*media)+12.613
                print (y)

                if 0 < y <= 1.5:
                    Results_list.append("green" + ' ' + str(xmin)+ ' ' + str(ymin)+ ' ' + str(xmax)+ ' ' + str(ymax)) 
                else:
                    if 1.5 < y <= 2.5:
                        Results_list.append("breaking" + ' ' + str(xmin)+ ' ' + str(ymin)+ ' ' + str(xmax)+ ' ' + str(ymax))
                    else:
                        if 2.5 < y <= 3.5:
                            Results_list.append("reddish" + ' ' + str(xmin)+ ' ' + str(ymin)+ ' ' + str(xmax)+ ' ' + str(ymax))
                        else:
                            if y > 3.5:
                                Results_list.append("red" + ' ' + str(xmin)+ ' ' + str(ymin)+ ' ' + str(xmax)+ ' ' + str(ymax))
                
                    
                   
                   
            with open(final2, 'w') as f:
                f.write('\n'.join(Results_list))
                f.close()
                    
segm_crop()
