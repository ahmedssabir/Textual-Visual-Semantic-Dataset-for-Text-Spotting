#!/bin/bash
#import COCO-Text
import coco_text  
import numpy
from matplotlib import pyplot as plt

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab as pl
import pylab
from matplotlib.pyplot import *
import cv2
import sys
from PIL import Image
   


if __name__ == '__main__':

  for loop in range(0, 2): # loop and pick random pictures   

#API offers some basic infos of the dataset.   
    ct = coco_text.COCO_Text('/COCO_Data_set/COCO_Text.json')
    ct.info()

    #Select annotations and images based on filter criteria
    # get all images containing at least one instance of legible text
    #retrieve some images. We want to get a list of all image ids from the training set,
    #where the image contains at least one text instance that is legilbe and is machine printed.
     
    imgs = ct.getImgIds(imgIds=ct.train,catIds=[('legibility','legible'),('class','machine printed')])

    #all annotation ids from the validation set that are legible, machine printed
    #and have an area between 0 and 200 pixels.
    anns = ct.getAnnIds(imgIds=ct.val,
                        catIds=[('legibility','legible'),('class','machine printed')],
                        areaRng=[0,200])

    
    dataDir='/Data1/COCO_Data_set'
    dataType='train2014'
   
   

    #Using the API introduced above, lets select an image
    #that has at least one instance of legible text.

    # get all images containing at least one instance of legible text
    imgIds = ct.getImgIds(imgIds=ct.train,
                    catIds=[('legibility','legible')])
    # pick one at random
    img = ct.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

    # --- running code start here
    I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
   
    
    file_name = str(img['file_name'])
    
    # save to file  full image 
    io.imsave('/coco_image/%s'%file_name.format(loop), I)
 
    # getting the json  file that assocated with ID
    annIds = ct.getAnnIds(imgIds=img['id'])
    anns = ct.loadAnns(annIds)
    ct.showAnns(anns)
   
    # write annotation to spearte file 
    f= open('/coco_image/ann_coco_Image/%s.txt'%file_name.format(loop),'w')

    gt = str(anns)
    f.write(gt)
    #f.write('\n\n')
    f.close

 

_ = raw_input("Press [enter] tome continue.")

