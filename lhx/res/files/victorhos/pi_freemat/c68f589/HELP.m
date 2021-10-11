% Add gaussian noise to an image
img = imread('/Users/victor/Pictures/lenna.jpg');
img_r = img(:,:,1);
colormap(gray);
image(img_r);
nmean = 10;
nvar = 1000;
img_r_n = img_r + sqrt(nvar)*randn(256,256)+nmean;
figure(2);
colormap(gray);
image(img_r_n);

x  = linspace(1,256,256);
y1 = img_r(128,1:256);
y2 = img_r_n(128,1:256);
figure(3);

plot(x,y1,'b-');
figure(4);
plot(x,y2,'r-');
mean(y1)
std(y1)
mean(y2)
std(y2)