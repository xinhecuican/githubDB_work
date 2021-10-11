%lendo a imagem
img = imread('/Users/victor/Pictures/burger.jpg');

%mostrando imagem lida
figure(1)
colormap(gray);
image(img);

%criando filtro passa baixa
filtroPassaBaixa = [0.12, 0.12, 0.12 ; 0.12, 0.12, 0.12; 0.12, 0.12, 0.12]

%criando filtro passa alta
filtroPassaAlta = [0, -1, 0; -1, 5, -1; 0, -1, 0]

%criando uma linha
x  = linspace(1,256,256);

%------------------------------------------------------------------------

%aplicando o algoritmo gaussiano (aplicar ruido)
img_r = img(:,:,1);
img_g = img(:,:,2);
img_b = img(:,:,3);
colormap(gray);
image(img_r);
nmean = 10;
nvar = 1000;
img_r_n = img_r + sqrt(nvar)*randn(256,256)+nmean;

%mostrando imagem com ruido
figure(2);
colormap(gray);
image(img_r_n);

%grafico ruido
%pega a linha 128, de 1 ate 256 para mostrar no grafico
linha_ruido = img_r_n(128,1:256);
figure(5);
plot(x,linha_ruido,'b-');
mean(linha_ruido)
std(linha_ruido)

%------------------------------------------------------------------------
%algoritimo de convolucao PASSA BAIXA

for x = 2:254
    for y = 2:254
        
        a = filtroPassaBaixa(1,1) * img(x-1,y-1)
        b = filtroPassaBaixa(1,2) * img(x-1,y)
        c = filtroPassaBaixa(1,3) * img(x-1,y+1)
        d = filtroPassaBaixa(2,1) * img(x,y-1)
        e = filtroPassaBaixa(2,2) * img(x,y)
        f = filtroPassaBaixa(2,3) * img(x, y+1)
        g = filtroPassaBaixa(3,1) * img(x+1,y-1)
        h = filtroPassaBaixa(3,2) * img(x+1,y)
        i = filtroPassaBaixa(3,3) * img(x+1,y+1)
        
        imagem(x, y) = a + b + c + d + e + f + g + h + i;
        
    end
end

%tratando as bordas das imagens
for q = 1:256
    imagem(1,q) = img(2, q)
    imagem(q,1) = img(q, 2)
    
    imagem(256,q) = img(255, q);
    imagem(q, 256) = img(q, 255);
end

%Mostrando a imagem com passa baixa
figure(3)
colormap(gray);
image(imagem)

%grafico pos passa-baixa
%pega a linha 128, de 1 ate 256 para mostrar no grafico
linha_ruido = img_r_n(128,1:256);
figure(5);
plot(x,linha_ruido,'b-');
mean(linha_ruido)
std(linha_ruido)

%------------------------------------------------------------------------
%algoritimo de convolucao PASSA ALTA

for x = 2:254
    for y = 2:254
        
        a = filtroPassaAlta(1,1) * img(x-1,y-1)
        b = filtroPassaAlta(1,2) * img(x-1,y)
        c = filtroPassaAlta(1,3) * img(x-1,y+1)
        d = filtroPassaAlta(2,1) * img(x,y-1)
        e = filtroPassaAlta(2,2) * img(x,y)
        f = filtroPassaAlta(2,3) * img(x, y+1)
        g = filtroPassaAlta(3,1) * img(x+1,y-1)
        h = filtroPassaAlta(3,2) * img(x+1,y)
        i = filtroPassaAlta(3,3) * img(x+1,y+1)
        
        imagem(x, y) = a + b + c + d + e + f + g + h + i;
        
    end
end

%tratando as bordas
for q = 1:256
    imagem(1,q) = img(2, q)
    imagem(q,1) = img(q, 2)
    
    imagem(256,q) = img(255, q);
    imagem(q, 256) = img(q, 255);
end

%Mostrando a imagem com passa alta
figure(4)
colormap(gray);
image(imagem)

%------------------------------------------------------------------------