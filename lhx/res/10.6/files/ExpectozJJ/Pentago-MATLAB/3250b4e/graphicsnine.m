function G_board=graphicsnine(Board)
% This function creates and updates the graphical interface of the board at
% every turn when called. 
% Format of Call: graphics(Board)
% Returns G_board
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Gets the tile pieces selected (or by default) by user from Settings UI 
global tile4
global tile5
global tile6
global tile7
global tile8
global arrow4
global arrow3
global arrow2
global arrow1
global arrowborder

% This stores all the relevant image files as variables.
% These are the tile pieces for the game board.
tile{8} = imread(tile7,'png');
tile{7} = imread(tile6,'png');
tile{6} = imread(tile5,'png');
tile{5} = imread(tile4,'png');
tile{4} = imread(tile8,'png');

% This sets the arrows images on the game board.
rot{1} = imread(arrow4,'png');
rot{2} = imread(arrow2,'png');
rot{3} = imread(arrow3,'png');
rot{4} = imread(arrow1,'png');
rot{5} = imread(arrowborder,'png');

% Initializes G_board as empty image board
G_board=[];
% Assigns r and c as board dimensions
[r,c]=size(Board);

% Initialises for loop to loop from 1st row to the last row of the board
% matrix.
for i=1:r
    % G_board1 is the empty row image board.
    G_board1=[];
    % Initializes for loop to loop every (i,j) entry from 1st column to
    % last column of ith row.
    for j=1:c;
        if Board(i,j)==0 % If entry is 0, puts an empty tile. 
            G_board1=[G_board1 tile{4}]; 
        elseif Board(i,j)==1 % If entry is 1, puts a red tile. 
            G_board1=[G_board1 tile{5}];
        elseif Board(i,j)==2 % If entry is 2, puts a blue tile. 
            G_board1=[G_board1 tile{6}];
        elseif Board(i,j)==3 % If entry is 3, puts a green tile. 
            G_board1=[G_board1 tile{7}];
        elseif Board(i,j)==4 % If entry is 4, puts a yellow tile. 
            G_board1=[G_board1 tile{8}];
        end
    end
    % Concatenate each row image board to G_board column by column
    G_board=[G_board; G_board1];
end

% Concatenates the border(with arrows image) with the main G_board. 
sidel1=[rot{5}; rot{5}; rot{4}; rot{1}; rot{2}; rot{4}; rot{1}; rot{5}; rot{5}];
sidel2=[rot{5}; rot{5}; rot{4}; rot{1}; rot{3}; rot{4}; rot{1}; rot{5}; rot{5}];
sideu=[rot{5} rot{5} rot{5} rot{3} rot{2} rot{5} rot{3} rot{2} rot{5} rot{5} rot{5}];
G_board=[sidel1 G_board sidel2];
G_board=[sideu; G_board; sideu];

% Sets the dimensions of the figre window
set(gcf,'Position',[150 80 500 500]);

% Prints the G_board in a figure window 
image(G_board);

% Sets appropriate gridlines at the correct coordinates with black colour 
line([2000 2000],[505 5040],'LineWidth',2,'Color',[0 0 0]);
line([505 5040],[2000 2000],'LineWidth',2,'Color',[0 0 0]);
line([3500 3500],[505 5040],'LineWidth',2,'Color',[0 0 0]);
line([505 5040], [3500 3500],'LineWidth',2,'Color',[0 0 0]);

% Labels figure (G_board) as 'Pentago' and sets board as square. 
title('Pentago XL')

% Disables visibility of axes 
axis off

% Ensures resizing of figure window will maintain G_board as square. 
axis square
end