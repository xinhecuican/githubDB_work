function defendbeflate = defendordie(Board,who_to_play)
% This function checks for positions whereby it needs
% to blocks an opponent's tile piece if it has 3 along the same row, column
% and diagonal. 
% Format of Call: defendordie(Board,who_to_play)
% Return defendbeflate
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% check refers to the opponent value on the board field. 
if who_to_play==1
    check=2;
elseif who_to_play==2
    check=1;
end

% Initialise empty matrix for the collection of these defensive moves. 
defendbeflate=[];

% Checks for any 3 in a row from row 1 to 6.
for i=1:6
    row=[1 7 13 19 25 31]+(i-1); % Formula for getting linear index of move positions
    if sum(Board(i,1:4)==check)==3 % Checks from 1st to 4th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(i,1:4)==0); % Identifies move positions
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate row(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(i,2:5)==check)==3 % Checks from 2nd to 5th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(i,2:5)==0); % Identifies move positions
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate row(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(i,3:6)==check)==3 % Checks from 3rd to 6th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(i,3:6)==0); % Identifies move positions
        if Board(row(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate row(x)]; % Stores move into the vector.
        end
    end
end

for j=1:6 % Checks for any 3 in a column from column 1 to 6.
    column=[1 2 3 4 5 6]+6*(j-1); % Formula for getting linear index of column move positions
    if sum(Board(1:4,j)==check)==3 % Checks from 1st to 4th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(1:4,j)==0); % Identifies move positions
        if Board(column(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate column(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(2:5,j)==check)==3 % Checks from 2nd to 5th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(2:5,j)==0); % Identifies move positions
        if Board(column(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate column(x)]; % Stores move into the vector. 
        end
    elseif sum(Board(3:6,j)==check)==3 % Checks from 3rd to 6th tile for any 3 tiles opponent has taken up in the field.
        x=find(Board(3:6,j)==0); % Identifies move positions
        if Board(column(x))==0 % Checks for any invalid move (Exisitng tile taken up anot)
            defendbeflate=[defendbeflate column(x)]; % Stores move into the vector.
        end        
    end
end

for k=-1:1 % k refers to the diagonal index for diag built in function (-1 to 1 are diagonals that have at least 5 pieces in a line)
    % Similar to those check winning conditions function (determinewin.m).
    % But here, it checks for 3 tiles opponent has taken up. 
    d=diag(Board,k);
    e=diag(rot90(Board),k);
    if k==0
        identityd=[1 8 15 22 29 36];
        identitye=[31 26 21 16 11 6];
        if sum(d(1:4)==check)==3 || sum(d(2:5)==check)==3 || sum(d(3:6)==check)==3
            y= d(1:4)==0;
            defendbeflate=[defendbeflate identityd(y)];
            y=d(2:5)==0;
            defendbeflate=[defendbeflate identityd(y)];
            y=d(3:6)==0;
            defendbeflate=[defendbeflate identityd(y)];
        elseif sum(e(1:4)==check)==3 || sum(e(2:5)==check)==3 || sum(e(3:6)==check)==3
            y=e(1:4)==0;
            defendbeflate=[defendbeflate identitye(y)];
            y=e(2:5)==0;
            defendbeflate=[defendbeflate identitye(y)];
            y=e(3:6)==0;
            defendbeflate=[defendbeflate identitye(y)];            
        end
    end
    identitymind=[2 9 16 23 30];
    identityplud=[7 14 21 28 35];
    identitymine=[25 20 15 10 5];
    identityplue=[32 27 22 17 12];
    if sum(d(1:4)==check)==3 || sum(d(2:5)==check)==3
        if k==-1
            y= d(1:4)==0;
            defendbeflate=[defendbeflate identitymind(y)];
            y= d(2:5)==0;
            defendbeflate=[defendbeflate identitymind(y)];
        elseif k==1
            y= d(1:4)==0;
            defendbeflate=[defendbeflate identityplud(y)];
            y= d(2:5)==0;
            defendbeflate=[defendbeflate identityplud(y)]; 
        end
    elseif sum(e(1:4)==check)==3 || sum(e(2:5)==check)==3
        if k==-1
            y= e(1:4)==0;
            defendbeflate=[defendbeflate identitymine(y)];
            y= e(2:5)==0;
            defendbeflate=[defendbeflate identitymine(y)];
        elseif k==1
            y= e(1:4)==0;
            defendbeflate=[defendbeflate identityplue(y)];
            y= e(2:5)==0;
            defendbeflate=[defendbeflate identityplue(y)];
        end
    end
end
end