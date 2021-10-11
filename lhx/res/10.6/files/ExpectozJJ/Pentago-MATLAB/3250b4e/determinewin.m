function win=determinewin(Board) 
% This function checks for simple winning states between AI and its
% opponent and draw state. 
% Format of Call: determinewin(Board)
% Returns win 
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Initialises win as 0
win=0;

% Obtains dimensions of Board from Board itself. 
[r,c]=size(Board);

% Executes the first part for Board Pentago 6x6 
if r==6 && c==6
    for i = 1:6 % Checks through 1st row to the 6th. 
        if sum(Board(i,1:5)==1)==5 || sum(Board(i,2:6)==1)==5 % Check win for player 1 rows 
            win=1;
            break
        elseif sum(Board(i,1:5)==2)==5 || sum(Board(i,2:6)==2)==5
            win=2;
            break
        elseif sum(Board(i,1:5)==3)==5 || sum(Board(i,2:6)==3)==5 % Check win for AI rows
            win=3;
            break
        end
    end
    
    for j=1:6
        if sum(Board(1:5,j)==1)==5 || sum(Board(2:6,j)==1)==5 % Check win for player 1 columns 
            win=1;
            break
        elseif sum(Board(1:5,j)==2)==5 || sum(Board(2:6,j)==2)==5
            win=2;
            break
        elseif sum(Board(1:5,j)==3)==5 || sum(Board(2:6,j)==3)==5 % Check win for AI columns 
            win=3;
            break
        end
    end
    
    for k=-1:1 % k refers to the diagonal index for diag built in function (-1 to 1 are diagonals that have at least 5 pieces in a line)
        d=diag(Board,k); % main diagonals of Board 
        e=diag(rot90(Board),k); % anti-diagonals of Board 
        if k==0 % Main diagonal and main anti-diagonal check win for player 1 
            if sum(d(1:5)==1)==5 || sum(e(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(e(2:6)==1)==5
                win=1;
                break
            end
        elseif sum(d(1:5)==1)==5 || sum(e(1:5)==1)==5
            win=1;
            break
        end
        if k==0
            if sum(d(1:5)==2)==5 || sum(e(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(e(2:6)==2)==5
                win=2;
                break
            end
        elseif sum(d(1:5)==2)==5 || sum(e(1:5)==2)==5
            win=2;
            break
        end
        if k==0 % Main diagonal and main anti-diagonal check win for AI 
            if sum(d(1:5)==3)==5 || sum(e(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(e(2:6)==3)==5
                win=3;
                break
            end
        elseif sum(d(1:5)==3)==5 || sum(e(1:5)==3)==5
            win=3;
            break
        end
    end
end

if sum(any(Board==0))==0 && win==0 % Check win for draw state. 
    return
end
end