% Add gaussian noise to an image
img = imread('/Users/victor/Pictures/lenna.jpg');
% img(lin, col, layer)
img_r = img(:,:,1);
img_g = img(:,:,2);
img_b = img(:,:,3);
colormap(gray);
image(img_r);
nmean = 10;
nvar = 1000;
img_r_n = img_r + sqrt(nvar)*randn(256,256)+nmean;
figure(2);
colormap(gray);
image(img_r_n);