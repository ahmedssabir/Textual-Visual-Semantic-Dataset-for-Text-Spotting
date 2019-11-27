##Textual Visual Semantic Dataset for Text Spotting  
<!---Visual Re-ranking with Natural Language Understanding for Text Spotting -->

![example](https://github.com/ahmedssabir/dataset/blob/master/example.jpg)


This dataset has been used in these papers:

`Visual Re-ranking with Natural Language Understanding for Text Spotting` https://arxiv.org/pdf/1810.12738.pdf 

`Semantic Relatedness Based Re-ranker for Text Spotting` https://arxiv.org/pdf/1909.07950.pdf  


## Motivation
Text Spotting in the Wild is a Computer Vision (CV) task consisting of detecting and recognizing text appearing in  images (e.g.  signboards, traffic signals or brands in clothing or objects). This is an unsolved problem due to the complexity of the context where texts appear (uneven backgrounds, shading, occlusions, perspective distortions, etc.). Only a few CV approaches try to exploit the relation between text and its surrounding environment to better recognize text in the scene. In this work, we propose a visual context dataset for Text Spotting in the wild, where the  publicly available dataset COCO-text Veit (veit *et al.*, 2016) has been extended with information about the scene (such as objects and places appearing in the image) to enable researchers to include on semantic relations between texts and scene in their Text Spotting systems, and to offer a common framework for such approaches.

## Highlights
This dataset is based on [COCO-text], Please visit https://github.com/andreasveit/coco-text. COCO-text is based on Microsoft COCO Please visit http://mscoco.org/ for more information on COCO-dataset, including the image data, object annotatins and caption annotations.

[COCO-text]:https://github.com/andreasveit/coco-text
## 1 - Extracting  full images with bounding box (gt) from COCO-text
- [COCO-text offical API][4] `python 2,7` 
- Run `coco_api_modified.py` Extract full image with its gt (json files) 

[4]: https://github.com/andreasveit/coco-text

## 2 -  Extracting  the Bounding box and top-k objects (from object classifer) 
- [Matlab 2018][3] - you only need to run it once 
- [MatConvNet][1] open source deep learning freamework 
- Download most recent [Pre-trained] SOTA object classifer or Resnet152 (this code)  
- Run `Extract_BBox.m` file 1 bounding box file 2 full image 


![Cropped text images](https://github.com/ahmedssabir/dataset/blob/master/COCO_train2014_000000000081_s.jpg)


![full image](https://github.com/ahmedssabir/dataset/blob/master/COCO_train2014_000000000081.jpg)

[3]: https://www.mathworks.com/campaigns/products/trials.html
[1]:http://www.vlfeat.org/matconvnet/install/
[Pre-trained]:http://www.vlfeat.org/matconvnet/pretrained



  ## Visual contexts dataset (object, places*)  word level   
- [x] word level
- [ ] sentence level
 - Image_id, spotted word(gt), objects, places
 -  Example: `COCO_train2014_000000000081.jpg,airfracne, airliner, airfield`
 
*You can find the model [Places365-CNNs] 


[Places365-CNNs]:https://github.com/CSAILVision/places365
 
 ## For testing (object1, object2, places) 
$`\sqrt{2}`$- [x] word level
- [ ] sentence level
- This dataset from [ICDAR2017 Robust Reading Challenge on COCO-Text][5], [Task 3 End-to-End Recognition][6] 

- Image_id, spotted word(baseline), objects1,object2,places
 -  Example: `COCO_train2014_000000273358.jpg,barber,street,ticket_booth, barbershop`


 ## Visual contexts 2 (image description, object, place) 
- [x] word level
- [x] sentence level
 - Image_id, spotted word(gt/baseline), caption
 - Example: `COCO_train2014_000000000081.jpg, airfracne,a large jetliner flying through the sky with a sky background ,airliner, airfield)`
 
 
 ## For testing  (image description) 
- [ ] word level
- [x] sentence level
- This dataset from [ICDAR2017 Robust Reading Challenge on COCO-Text][5], [Task 3 End-to-End Recognition][6] 
- Image_id, spotted word(baseline),object_1, object_2, place, caption

 ## Object and text co-occurrence database 
- [x] word level 
- [ ] sentence level
- spotted word(gt), places/object- co-occurrence information between text and objects
- The conditional probability of  object/text happen togaher in COCO-text P(word|object) = count(word,object)/count(object) `object-text-co-occurrence-(P(w|c)` 
- run `counting_pairs.py` to count the pairs (spotted text, object/place) happen together 
```math
$`\sqrt{2}`$
```

[5]:http://rrc.cvc.uab.es/?ch=5&com=introduction
[6]:http://rrc.cvc.uab.es/?ch=5&com=tasks


## Dictionary 300K 
- Matlab 2018 
- Load the [Pre-trained Dictionary] A) [opensubtitle](https://www.duo.uio.no/bitstream/handle/10852/50459/947_Paper.pdf?sequence=4)   or B) [enhanced version with google n-gram](https://books.google.com/ngrams/info)   
- `runMap = containers.Map(T3w, T3N) % A)Dic` 
- `runMap = containers.Map(opensub_google_ngram_W, opensub_google_ngram_N) % B)Dic`
- `word = runMap('barcelona') % get word`  

[Pre-trained Dictionary]:https://www.dropbox.com/sh/1af43nvlmac54ib/AADyRtK4ztyTS65hull1gyxMa?dl=0
[opensubtitle]:https://www.duo.uio.no/bitstream/handle/10852/50459

## Feedback 
 :raising_hand_man: Suggestions and opinions  of this dataset (both positive and negative) are greatly welcome :bowing_man:. Please contact the author by sending an email to asabir◎cs。upc。edu
 
