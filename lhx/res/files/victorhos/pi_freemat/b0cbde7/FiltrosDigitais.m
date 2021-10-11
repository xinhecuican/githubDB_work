%lendo a imagem
img = imread('C:\Users\Lilian\Documents\GitHub\pi_freemat\bb.jpg');
image(img);

%aplicando o algoritmo gaussiano (aplicar ruido)
figure(1)
img_r = img(:,:,1);
img_g = img(:,:,2);
img_b = img(:,:,3);
colormap(gray);
%image(img_r);
%nmean = 10;
%nvar = 1000;
img_r_n = img_r + sqrt(nvar)*randn(498,498)+nmean;
figure(2);
colormap(gray);
image(img_r_n);

%criando filtro passa baixa
filtroPassaBaixa = [0.12, 0.12, 0.12 ; 0.12, 0.12, 0.12; 0.12, 0.12, 0.12]

%criando filtro passa alta
filtroPassaAlta = [0, -1, 0; -1, 5, -1; 0, -1, 0]

%algoritimo de convolucao
%usar aquele exemplo do começo do comeco do tri
teste = 0
while teste <= 5
    imagem(1,1) = filtroPassaBaixa(2,2)*img(1,1)+filtroPassaBaixa(2,3)*img(1,2)+filtroPassaBaixa(3,2)*img(2,1)+filtroPassaBaixa(3,3)*img(2,2)
    circshift(img, [1,1])    
    teste = teste + 1
end
figure(3)
img = imagem
