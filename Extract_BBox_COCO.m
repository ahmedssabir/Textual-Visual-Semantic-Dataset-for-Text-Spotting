for k = 81 % number of the image (for loop k= first:last)
%% read the ground_truth.txt  
s = sprintf('/ann_coco_Image/COCO_train2014_000000%06d.jpg.txt', k);
fid = fopen(s);
tline = fgetl(fid);
%% Extract the ground truth and bbox,  there are two diffrnet formats of json files
%% we only extract one text image per image.  
s = fileread(s);
% Remove the odd u'
s = strrep(s, 'u''', '''');
% Replace ' by "
s = strrep(s, '''', '"');
% matlab new 2018
t = jsondecode(s);
try
bbox = t.bbox; % doble
BBox = bbox;
word1 = t.utf8_string;
word1 = lower(word1);
catch 
end
try
word1 = t{1}.utf8_string;
BBox = t{1}.bbox;
word1 = lower(word1);
catch
end     
%% Extracting Coordinates of the bounding Box 
bbox = regexp(tline, '\d*[0-9]','Match'); %regx
bbox = str2double(bbox); % convert to double for bounding box
bbox = [ bbox(1), bbox(2), bbox(3), bbox(4)];
width = bbox(3) - bbox(1);
height = bbox(4) -bbox(2);
bbox= [bbox(1) bbox(2) width height];
%word1 = regexp(tline, '\w*[A-Z a-z]' ,'Match');
%% Read and Extract the BBox 
w{k}=imread(sprintf('/coco_image-1/COCO_train2014_000000%06d.jpg',k));
%figure; imshow(w{k})
subImage = imcrop(w{k}, BBox);
I= subImage;
try
% write bbox and full image to a file 
imwrite(I,sprintf('/home/bbox/COCO_train2014_000000%06d.jpg', k))
imwrite(w{k},sprintf('/home/full-image/COCO_train2014_000000%06d.jpg', k))
catch
end
%% print the ground_truth to text file
opt =fopen('/home/asabir/file/ground_truth.txt','a');
q = sprintf('COCO_train2014_000000%06d.jpg', k);
s=strcat(num2str(q), ',' , {word1} ,'\n'); 
s=s{1};
fprintf(opt,s);
%% 
% Extract the visual infromation 
run  matlab/vl_setupnn % run matconvnet here 
%% Deep model Res-net152 
% load the pre-trained weight here 
net = dagnn.DagNN.loadobj(load('/home/asabir/Desktop/weight/imagenet-resnet-152-dag.mat'));
net.mode = 'test' ;
%% read the image/norm 
img{k}=imread(sprintf('/media/asabir/full-images/COCO_train2014_000000%06d.jpg', k ));
im = ([img{k}]);
im_ = single(im) ; % note: 255 range
im_ = imresize(im_, net.meta.normalization.imageSize(1:2)) ;
%im_ = im_ - net.meta.normalization.averageImage ;
im_ = bsxfun(@minus, im_, net.meta.normalization.averageImage) ;
%% run the CNN
net.eval({'data', im_});
%% print the output
%figure; imshow(im)
%% obtain the CNN otuput from softmax score
scores = net.vars(net.getVarIndex('prob')).value ;
scores = squeeze(gather(scores)) ;
[asort,idsort] = sort(scores,'descend');
asort(1:3); 
idsort(1:3);
%% Getting the P(w|x1) and P(w|x2)
 p1 = asort(1);
 p2 = asort(2);
 p3 = asort(3);
%% Output word1, word2 
output1 = idsort(1);
output2 = idsort(2);
output3 = idsort(3);
% print the labels 
fprintf('Predicted1 lable: %s\n', net.meta.classes.description{output1});
fprintf('Predicted2 lable: %s\n', net.meta.classes.description{output2});
fprintf('Predicted3 lable: %s\n', net.meta.classes.description{output3});
%% Table of P(w1|x) P(w2|x)
Name = {'Word lable';' P(x)'};
lable1 = { net.meta.classes.description{output1}; p1};
%lable2 = {net.meta.classes.description{output2} ; p2}; 
%lable3 = {net.meta.classes.description{output3} ; p3};
%T = table(lable1,lable2, lable3,  'RowName',Name);
T = table(lable1,  'RowName',Name);
%% Extract only max P1(w_max|x) but you could extract more object2, object3 etc 
% object 1
all = lable1;
fw = all{1}; %index the first word
fprintf(fw);
fw= strsplit(fw); %split
%fw = regexp(fw, '\S*', 'match')
%% object 2
%all1 = lable2;
%fw1 = all1{1};
%% object 3
%all2 = lable3;
%fw2 = all2{1};
%% print to text file 
 opt =fopen('/home/file/visual_context_information.txt','a');
 s=strcat(num2str(q), ',',  fw, '\n');
 %s = strrep(s, ', ');
 s = s{1};
 fprintf(opt,s);
 %% print all in one file
 n = 1;
 opt =fopen('/home/file/visual_context_information_ground_truth.txt','a');
 s=strcat(num2str(q), ',', word1 ,',', fw,  num2str(n),  '\n');
 %s = strrep(s, ', ');
 s = s{1};
 fprintf(opt,s);
%% print the all with the prob 
 opt =fopen('/home/file/visual_context_information_ground_truth_prob.txt','a');
 s=strcat(num2str(q), ',', word1 ,',', fw, ',', num2str(p1), '\n');
 %s = strrep(s, ', ');
 s = s{1};
 fprintf(opt,s);

  %% print word with (object1,2,3)
%  opt =fopen('/home/file/visual-prob.txt','a');
%  s=strcat(num2str(q), ',', word1 ,',', fw ,',', fw1, ',',  lable3, ',' ,num2str(p1), ',', num2str(p2), ',' ,  num2str(p2), '\n');
%  %s = strrep(s, ', ');
%  s = s{1};
%  fprintf(opt,s);
clear

end


    
