function win=victorytest(Board)
% This function checks for a winning state whenever it is being called. 
% Format of Call: victory test(Board)
% Returns win 
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Pre-defines all win states of all players as zero 
player1win=0;
player2win=0;
player3win=0;
player4win=0;
comwin=0;

% Stores size of the Board as variable 
[r,c]=size(Board);

%% For Pentago 6x6, we do the winning checks for all rows, columns and diagonals (including anti-diagonals)
if r==6
    for i = 1:6 % i refers to row 1 to 6 
        if sum(Board(i,1:5)==2)==5 || sum(Board(i,2:6)==2)==5 
            player1win=1;
        elseif sum(Board(i,1:5)==3)==5 || sum(Board(i,2:6)==3)==5
            player2win=1;
        elseif sum(Board(i,1:5)==1)==5 || sum(Board(i,2:6)==1)==5
            comwin=1;
        end
    end
    
    for j=1:6 % j refers to column 1 to 6 
        if sum(Board(1:5,j)==2)==5 || sum(Board(2:6,j)==2)==5
            player1win=1;
        elseif sum(Board(1:5,j)==3)==5 || sum(Board(2:6,j)==3)==5
            player2win=1;
        elseif sum(Board(1:5,j)==1)==5 || sum(Board(2:6,j)==1)==5
            comwin=1;
        end
    end
    
    % diag is a built in function that has a diagonal index of the matrix (k=0 is main diagonal, k<0 are diagonals below main diagonal and vice versa)
    for k=-1:1 % For 6x6 only k=-1 to k=1 has at least 5 entries in a diagonal (possibility for a win to be found) 
        d=diag(Board,k); % diagonals of Board 
        e=diag(rot90(Board),k); % anti-diagonals of Board (rot90 of anti diagonals is diagonals)
        if k==0 
            if sum(d(1:5)==2)==5 || sum(e(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(e(2:6)==2)==5
                player1win=1;
            end
        elseif sum(d(1:5)==2)==5 || sum(e(1:5)==2)==5
            player1win=1;
        end
        if k==0
            if sum(d(1:5)==3)==5 || sum(e(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(e(2:6)==3)==5
                player2win=1;
            end
        elseif sum(d(1:5)==3)==5 || sum(e(1:5)==3)==5
            player2win=1;
        end
        if k==0
            if sum(d(1:5)==1)==5 || sum(e(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(e(2:6)==1)==5
                comwin=1;
            end
        elseif sum(d(1:5)==1)==5 || sum(e(1:5)==1)==5
            comwin=1;
        end
    end
    win=[comwin player1win player2win]; % concatenates variables of win states of all players into a row vector win 
%% For Pentago 9x9, we do the corresponding winning checks for all rows, column, diagonals and anti-diagonals.
elseif c==9
    for i = 1:9 % i refers to row 1 to 9
        if sum(Board(i,1:5)==1)==5 || sum(Board(i,2:6)==1)==5 || sum(Board(i,3:7)==1)==5 || sum(Board(i,4:8)==1)==5 || sum(Board(i,5:9)==1)==5
            player1win=1;
        elseif sum(Board(i,1:5)==2)==5 || sum(Board(i,2:6)==2)==5 || sum(Board(i,3:7)==2)==5 || sum(Board(i,4:8)==2)==5 || sum(Board(i,5:9)==2)==5
            player2win=1;
        elseif sum(Board(i,1:5)==3)==5 || sum(Board(i,2:6)==3)==5 || sum(Board(i,3:7)==3)==5 || sum(Board(i,4:8)==3)==5 || sum(Board(i,5:9)==3)==5
            player3win=1;
        elseif sum(Board(i,1:5)==4)==5 || sum(Board(i,2:6)==4)==5 || sum(Board(i,3:7)==4)==5 || sum(Board(i,4:8)==4)==5 || sum(Board(i,5:9)==4)==5
            player4win=1;
        end
    end
    for j=1:9 % j refers to column 1 to 9 
        if sum(Board(1:5,j)==1)==5 || sum(Board(2:6,j)==1)==5 || sum(Board(3:7,j)==1)==5 || sum(Board(4:8,j)==1)==5 || sum(Board(5:9,j)==1)==5
            player1win=1;
        elseif sum(Board(1:5,j)==2)==5 || sum(Board(2:6,j)==2)==5 || sum(Board(3:7,j)==2)==5 || sum(Board(4:8,j)==2)==5 || sum(Board(5:9,j)==2)==5
            player2win=1;
        elseif sum(Board(1:5,j)==3)==5 || sum(Board(2:6,j)==3)==5 || sum(Board(3:7,j)==3)==5 || sum(Board(4:8,j)==3)==5 || sum(Board(5:9,j)==3)==5
            player3win=1;
        elseif sum(Board(1:5,j)==4)==5 || sum(Board(2:6,j)==4)==5 || sum(Board(3:7,j)==4)==5 || sum(Board(4:8,j)==4)==5 || sum(Board(5:9,j)==4)==5
            player4win=1;
        end
    end
    
    for k=-4:4 % Similarly, k is the diagonal index of Board. k=-4 to k=4 has at least 5 entries in a diagonal for a win to be found 
        d=diag(Board,k); % diagonals of Board
        e=diag(rot90(Board),k); % anti-diagonals of Board 
        if k==-4 || k==4
            if sum(d(1:5)==1)==5 || sum(e(1:5)==1)==5
                player1win=1;
            elseif sum(d(1:5)==2)==5 || sum(e(1:5)==2)==5
                player2win=1;
            elseif sum(d(1:5)==3)==5 || sum(e(1:5)==3)==5
                player3win=1;
            elseif sum(d(1:5)==4)==5 || sum(e(1:5)==4)==5
                player4win=1;
            end
        elseif k==-3 || k==3
            if sum(d(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(e(1:5)==1)==5 || sum(e(2:6)==1)==5
                player1win=1;
            elseif sum(d(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(e(1:5)==2)==5 || sum(e(2:6)==2)==5
                player2win=1;
            elseif sum(d(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(e(1:5)==3)==5 || sum(e(2:6)==3)==5
                player3win=1;
            elseif sum(d(1:5)==4)==5 || sum(d(2:6)==4)==5 || sum(e(1:5)==4)==5 || sum(e(2:6)==4)==5
                player4win=1;
            end
        elseif k==-2 || k==2
            if sum(d(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(d(3:7)==1)==5 || sum(e(1:5)==1)==5 || sum(e(2:6)==1)==5 || sum(e(3:7)==1)==5
                player1win=1;
            elseif sum(d(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(d(3:7)==2)==5 || sum(e(1:5)==2)==5 || sum(e(2:6)==2)==5 || sum(e(3:7)==2)==5
                player2win=1;
            elseif sum(d(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(d(3:7)==3)==5 || sum(e(1:5)==3)==5 || sum(e(2:6)==3)==5 || sum(e(3:7)==3)==5
                player3win=1;
            elseif sum(d(1:5)==4)==5 || sum(d(2:6)==4)==5 || sum(d(3:7)==4)==5 || sum(e(1:5)==4)==5 || sum(e(2:6)==4)==5 || sum(e(3:7)==4)==5
                player4win=1;
            end
        elseif k==-1 || k==1
            if sum(d(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(d(3:7)==1)==5 || sum(d(4:8)==1)==5 || sum(e(1:5)==1)==5 || sum(e(2:6)==1)==5 || sum(e(3:7)==1)==5 || sum(e(4:8)==1)==5
                player1win=1;
            elseif sum(d(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(d(3:7)==2)==5 || sum(d(4:8)==2)==5 || sum(e(1:5)==2)==5 || sum(e(2:6)==2)==5 || sum(e(3:7)==2)==5 || sum(e(4:8)==2)==5
                player2win=1;
            elseif sum(d(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(d(3:7)==3)==5  || sum(d(4:8)==3)==5 || sum(e(1:5)==3)==5 || sum(e(2:6)==3)==5 || sum(e(3:7)==3)==5 || sum(e(4:8)==3)==5
                player3win=1;
            elseif sum(d(1:5)==4)==5 || sum(d(2:6)==4)==5 || sum(d(3:7)==4)==5  || sum(d(4:8)==4)==5 || sum(e(1:5)==4)==5 || sum(e(2:6)==4)==5 || sum(e(3:7)==4)==5 || sum(e(4:8)==4)==5
                player4win=1;
            end
        elseif k==0
            if sum(d(1:5)==1)==5 || sum(d(2:6)==1)==5 || sum(d(3:7)==1)==5 || sum(d(4:8)==1)==5 || sum(d(5:9)==1)==5 || sum(e(1:5)==1)==5 || sum(e(2:6)==1)==5 || sum(e(3:7)==1)==5 || sum(e(4:8)==1)==5 || sum(e(5:9)==1)==5
                player1win=1;
            elseif sum(d(1:5)==2)==5 || sum(d(2:6)==2)==5 || sum(d(3:7)==2)==5 || sum(d(4:8)==2)==5 || sum(d(5:9)==2)==5 || sum(e(1:5)==2)==5 || sum(e(2:6)==2)==5 || sum(e(3:7)==2)==5 || sum(e(4:8)==2)==5 || sum(e(5:9)==2)==5
                player2win=1;
            elseif sum(d(1:5)==3)==5 || sum(d(2:6)==3)==5 || sum(d(3:7)==3)==5  || sum(d(4:8)==3)==5 || sum(d(5:9)==3)==5  || sum(e(1:5)==3)==5 || sum(e(2:6)==3)==5 || sum(e(3:7)==3)==5 || sum(e(4:8)==3)==5 || sum(e(5:9)==3)==5 
                player3win=1;
            elseif sum(d(1:5)==4)==5 || sum(d(2:6)==4)==5 || sum(d(3:7)==4)==5  || sum(d(4:8)==4)==5 || sum(d(5:9)==4)==5  || sum(e(1:5)==4)==5 || sum(e(2:6)==4)==5 || sum(e(3:7)==4)==5 || sum(e(4:8)==4)==5 || sum(e(5:9)==4)==5
                player4win=1;
            end
        end
    end
    win=[player1win player2win player3win player4win]; % concatenates all win states of at most 4 players into vector win (2-4 Player Mode) 
end
end








