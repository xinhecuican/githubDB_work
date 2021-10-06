function [criticalmove,centremoves] = BasicGenius(Board,who_to_play)
% This function checks for centre positions and positions whereby it needs
% to block opponent's 4 in a row,column or diagonal to prevent opponent
% from winning next move. 
% Format of Call: BasicGenius(Board,who_to_play)
% Returns [criticalmove,centremoves] 
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Initialises empty matrix for collection of valid centre moves and
% critical moves.
centremoves=[];
criticalmove=[];

% check refers to the opponent value on the board field. 
if who_to_play==1
    check=2;
elseif who_to_play==2
    check=1;
end

% Checks for valid and available centre tile positions it can take on. 
if Board(8)==0
    centremoves=[centremoves 8];
elseif Board(11)==0
    centremoves=[centremoves 11];
elseif Board(26)==0
    centremoves=[centremoves 26];
elseif Board(29)==0
    centremoves=[centremoves 29];
end

% Checks for any 4 in a row from row 1 to 6. 
for i=1:6
    row=[1 7 13 19 25 31]+(i-1); % Formula for getting linear index of critical move positions
    if sum(Board(i,1:5)==check)==4 % Checks from 1st to 5th tile for any 4 tiles opponent has taken up in the field. 
        x=find(Board(i,1:5)==0); % Identifies critical move positions 
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            criticalmove=[criticalmove row(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(i,2:6)==check)==4 % Checks from 2nd to 6th tile for any 4 tiles opponent has taken up in the field.
        x=find(Board(i,2:6)==0); % Identifies critical move positions 
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            criticalmove=[criticalmove row(x)]; % Stores move into the vector. 
        end
    end
end

for j=1:6 % Checks for any 4 in a column from row 1 to 6. 
    column=[1 2 3 4 5 6]+6*(j-1); % Formula for getting linear index of critical move positions
    if sum(Board(1:5,j)==check)==4 % Checks from 1st to 5th tile for any 4 tiles opponent has taken up in the field.
        x=find(Board(1:5,j)==0); % Identifies critical move positions
        if Board(column(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            criticalmove=[criticalmove column(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(2:6,j)==check)==4 % Checks from 1st to 5th tile for any 4 tiles opponent has taken up in the field.
        x=find(Board(2:6,j)==0); % Identifies critical move positions
        if Board(column(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            criticalmove=[criticalmove column(x)]; % Stores move into the vector. 
        end
    end
end 

for k=-1:1 % k refers to the diagonal index for diag built in function (-1 to 1 are diagonals that have at least 5 pieces in a line)
    % Similar to those check winning conditions function (determinewin.m).
    % But here, it checks for 4 tiles opponent has taken up. 
    d=diag(Board,k);
    e=diag(rot90(Board),k);
    if k==0
        identityd=[1 8 15 22 29 36];
        identitye=[31 26 21 16 11 6];
        if sum(d(1:5)==check)==4 || sum(d(2:6)==check)==4 
            y= d(1:5)==0;
            criticalmove=[criticalmove identityd(y)];
            y=d(2:6)==0;
            criticalmove=[criticalmove identityd(y)];
        elseif sum(e(1:5)==check)==4 || sum(e(2:6)==check)==4
            y=e(1:5)==0;
            criticalmove=[criticalmove identitye(y)];
            y=e(2:6)==0;
            criticalmove=[criticalmove identitye(y)];
        end
    end
    identitymind=[2 9 16 23 30];
    identityplud=[7 14 21 28 35];
    identitymine=[25 20 15 10 5];
    identityplue=[32 27 22 17 12];
    if sum(d(1:5)==check)==4
        y= d(1:5)==0;
        if k==-1
            criticalmove=[criticalmove identitymind(y)];
        elseif k==1
            criticalmove=[criticalmove identityplud(y)]; 
        end
    elseif sum(e(1:5)==check)==4
        y= e(1:5)==0;
        if k==-1
            criticalmove=[criticalmove identitymine(y)];
        elseif k==1
            criticalmove=[criticalmove identityplue(y)];
        end
    end
end
end