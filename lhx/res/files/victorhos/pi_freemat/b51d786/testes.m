img = imread('/Users/victor/Pictures/lenna.jpg');

filtroPassaBaixa = 2 + 2
A = zeros(4:2)

A = [0.12, 0.12, 0.12 ; 0.12, 0.12, 0.12; 0.12, 0.12, 0.12]


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

%criando filtro passa baixa
filtroPassaBaixa = [0.12, 0.12, 0.12 ; 0.12, 0.12, 0.12; 0.12, 0.12, 0.12]

%criando filtro passa alta
filtroPassaAlta = [0, -1, 0; -1, 5, -1; 0, -1, 0]

%plot(x,y1,'b-')
%linspce(1,256,256)
%':' é até
% mean - merdia
%std - desvio padrao