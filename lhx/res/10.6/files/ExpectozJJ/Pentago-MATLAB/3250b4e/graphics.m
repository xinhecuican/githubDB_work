function G_board = graphics(Board)
% This function creates and updates the graphical interface of the board at
% every turn when called. 
% Format of Call: graphics(Board)
% Returns G_board
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Gets the tile pieces selected (or by default) by user from Settings UI 
global tile1
global tile2
global tile3
global tileud
global tilelr
global tilerl
global tiledu
global tileborder

% This stores all the relevant image files as variables.
% These are the tile pieces for the game board.
tile{3} = imread(tile3,'png');
tile{2} = imread(tile2,'png');
tile{1} = imread(tile1,'png');

% This sets the arrows images on the game board.
rot{1} = imread(tileud,'png');
rot{2} = imread(tilelr,'png');
rot{3} = imread(tilerl,'png');
rot{4} = imread(tiledu,'png');
rot{5} = imread(tileborder,'png');

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
            G_board1=[G_board1 tile{1}];
        elseif Board(i,j)==1 % If entry is 1, puts a red tile. Here, 1 refers to the computer player.
            G_board1=[G_board1 tile{2}];
        elseif Board(i,j)==2 % If entry is 2, puts a blue tile. 
            G_board1=[G_board1 tile{3}];
        elseif Board(i,j)==3 % If entry is 3, puts a red tile. 
            G_board1=[G_board1 tile{2}];
        end
    end
    % Concatenate each row image board to G_board column by column
    G_board=[G_board; G_board1];
end

% Concatenates the border(with arrows image) with the main G_board. 
sidel=[rot{5}; rot{5}; rot{4}; rot{1}; rot{5}; rot{5}];
sideu=[rot{5} rot{5} rot{5} rot{3} rot{2} rot{5} rot{5} rot{5}];
G_board = [sidel G_board sidel];
G_board = [sideu; G_board; sideu];
% sets the dimension of the figure window
set(gcf,'Position',[150 80 500 500]);
% Prints the Board image on figure windows 
image(G_board);

% Sets gridlines at the borderline and the x and y axis from the center of
% the board.
line([2005 2005],[505 3528],'LineWidth',2,'Color',[0 0 0]);
line([505 3528],[2000 2000],'LineWidth',2,'Color',[0 0 0]);

% Labels figure (G_board) as 'Pentago' and sets board as square. 
title('Pentago')

% Disables visibility of axis.
axis off

% Ensures G_board is square even when resizing. 
axis square
end