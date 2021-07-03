# author: @gerfsm


import os
from PIL import Image

ROIs = 'Path to the folder where we will save the segmented images'

img_folder = 'Path to the folder where we have the original images'

ann_folder = 'Path to the folder where we have the annotations (txt) of the original images'

images = os.listdir(img_folder)
annotations = os.listdir(ann_folder)

def segm_crop():
    
    list=[]
    for i in images:
        list.append(i)
        for filename in list:
            name,h = os.path.splitext(i)
            doc = ann_folder + '/' + name + '.txt'
            with open(doc) as infile:
                contents = infile.readlines()
                img = Image.open(img_folder + '/' + filename)
                for ann in range(len(contents)):
                    a = contents[ann]
                    coords = a.split()
                    xmin = int(coords[1])
                    ymin = int(coords[2])
                    xmax = int(coords[3])
                    ymax = int(coords[4])
                    final = ROIs + '/' + name + '_' + str(xmin) + '.jpg'
                    img1 = img.crop((xmin, ymin, xmax, ymax))
                    img1.save(final)
                    img1.close()
                    
segm_crop()
