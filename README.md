#  Visual Re-ranking with Natural Language Understanding for Text Spotting (Dataset)
This dataset have been used in this paper: 

Visual Re-ranking with Natural Language Understanding for Text Spotting

This dataset is based on [COCO-text], Please visit https://github.com/andreasveit/coco-text. COCO-text is based on Microsoft COCO Please visit http://mscoco.org/ for more information on COCO, including the image data, object annotatins and caption annotations.

[COCO-text]:https://github.com/andreasveit/coco-text
## 1 - Extracting  full images with bounding box (gt) from COCO-text
- [COCO-text offical API][4] `python 2,7` 
- Run `coco_api_modified.py` Extract full image with its gt (json files) 

[4]: https://github.com/andreasveit/coco-text

## 2) Extracting  the Bounding box and top-k objects (from object classifer) 
- [Matlab 2018][3] - ` Free 30 days trial ` you only need to run it once 
- [MatConvNet][1] open source deep learning freamework 
- Run `Extract_BBox.m` file 1 bounding box file 2 full image 


![Cropped text images](https://github.com/sabirdvd/Extracting_BBox_visual_information/blob/master/COCO_train2014_000000000081_s.jpg)


![full image](https://github.com/sabirdvd/Extracting_BBox_visual_information/blob/master/COCO_train2014_000000000081.jpg)

[3]: https://www.mathworks.com/campaigns/products/trials.html
[1]:http://www.vlfeat.org/matconvnet/install/


After installing MatConvNet you need to install pre-trained weight [Resent152][2]

[2]:https://www.dropbox.com/s/icuyb4qwbzctu1u/imagenet-resnet-152-dag.mat?dl=0
 
 
 ## Visual contexts (object, places*)  
 - Image_id, spotted word(gt), objects, places
 -  Example: `COCO_train2014_000000000081.jpg,airfracne, airliner, airfield`
 
*You can find the model [Places365-CNNs] 


[Places365-CNNs]:https://github.com/CSAILVision/places365
 
 ## For testing (object1, object2, places)
 This dataset from [ICDAR2017 Robust Reading Challenge on COCO-Text][5], [Task 3 End-to-End Recognition][6] 

- Image_id, spotted word(gt), objects1,object2,places
 -  Example: `COCO_train2014_000000273358.jpg,barber,street,ticket_booth, barbershop`


[5]:http://rrc.cvc.uab.es/?ch=5&com=introduction
[6]:http://rrc.cvc.uab.es/?ch=5&com=tasks

