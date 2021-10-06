function winningmoves = forthewin(Board,who_to_play)
% This function checks for positions whereby it needs
% to make 4 in a row,column or diagonal become 5 in a row,column or
% diagonal to win the game in the next move. 
% Format of Call: forthewin(Board,who_to_play)
% Returns winningmoves 
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Initialises empty matrix for collection of winning moves. 
winningmoves=[];

% Checks for any 4 in a row from row 1 to 6. 
for i=1:6
    row=[1 7 13 19 25 31]+(i-1); % Formula for getting linear index of move positions
    if sum(Board(i,1:5)==who_to_play)==4 % Checks from 1st to 5th tile for any 4 tiles itself has taken up in the field.
        x=find(Board(i,1:5)==0); % Identifies move positions
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            winningmoves=[winningmoves row(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(i,2:6)==who_to_play)==4 % Checks from 2nd to 6th tile for any 4 tiles itself has taken up in the field.
        x=find(Board(i,2:6)==0); % Identifies move positions
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            winningmoves=[winningmoves row(x)]; % Stores move into the vector. 
        end
    end
end

for j=1:6 % Similarly for the columns. (Similar to code for BasicGenius.m)
    column=[1 2 3 4 5 6]+6*(j-1);
    if sum(Board(1:5,j)==who_to_play)==4 
        x=find(Board(1:5,j)==0);
        if Board(column(x))==0
            winningmoves=[winningmoves column(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(2:6,j)==who_to_play)==4
        x=find(Board(2:6,j)==0);
        if Board(column(x))==0
            winningmoves=[winningmoves column(x)]; % Stores move into the vector. 
        end
    end
end 

for k=-1:1 % k refers to the diagonal index for diag built in function (-1 to 1 are diagonals that have at least 5 pieces in a line)
    % Similar to those check winning conditions function (determinewin.m).
    % But here, it checks for 4 tiles AI has taken up. 
    d=diag(Board,k);
    e=diag(rot90(Board),k);
    if k==0
        identityd=[1 8 15 22 29 36];
        identitye=[31 26 21 16 11 6];
        if sum(d(1:5)==who_to_play)==4 || sum(d(2:6)==who_to_play)==4 
            y= d(1:5)==0;
            winningmoves=[winningmoves identityd(y)];
            y=d(2:6)==0;
            winningmoves=[winningmoves identityd(y)];
        elseif sum(e(1:5)==who_to_play)==4 || sum(e(2:6)==who_to_play)==4
            y=e(1:5)==0;
            winningmoves=[winningmoves identitye(y)];
            y=e(2:6)==0;
            winningmoves=[winningmoves identitye(y)];
        end
    end
    identitymind=[2 9 16 23 30];
    identityplud=[7 14 21 28 35];
    identitymine=[25 20 15 10 5];
    identityplue=[32 27 22 17 12];
    if sum(d(1:5)==who_to_play)==4
        y= d(1:5)==0;
        if k==-1
            winningmoves=[winningmoves identitymind(y)];
        elseif k==1
            winningmoves=[winningmoves identityplud(y)]; 
        end
    elseif sum(e(1:5)==who_to_play)==4
        y= e(1:5)==0;
        if k==-1
            winningmoves=[winningmoves identitymine(y)];
        elseif k==1
            winningmoves=[winningmoves identityplue(y)];
        end
    end
end
end