function r=rotationmouseclick(Board)
% This function converts the coordinates of the mouse clicks of the user
% for rotation into the (i,j) entries of the 9x9 Board matrix 
% Format of Call: rotationmouseclick(Board)
% Returns r
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% ginput is the built in function to capture coordinates of the figure from
% mouse clicks by the user.
% Here, ginput(1) means it only allows user to capture one click. (Player
% only can rotate once). 
try
    [i,j]=ginput(1); % Uses ginput built in function to get coordinates
catch
    return;
end
s=ceil(i/504); % Since each empty tile image is of 504x504, we take the ceiling of the coordinates/504 which will be the column of the matrix.
t=ceil(j/504); % Since each empty tile image is of 504x504, we take the ceiling of the coordinates/504 which will be the row of the matrix.
[a,b]=size(Board); % Store the size of the Board into variables 

if a==6 % If Board is 6x6, then it executes an if else for 6x6's 8 Board rotations.
    % The if else below takes the s and t coordinates of ginput and returns
    % the corresponding rotation ID. 
    if s==5 && t==1
        r=1;
    elseif s==8 && t==4
        r=2;
    elseif s==8 && t==5
        r=3;
    elseif s==5 && t==8
        r=4;
    elseif s==4 && t==8
        r=5;
    elseif s==1 && t==5
        r=6;
    elseif s==1 && t==4
        r=7;
    elseif s==4 && t==1
        r=8;
    else % If r is none of the above, it recursives ginput until a valid input is captured. 
        r=rotationmouseclick(Board);
    end
elseif b==9 % If Board is 9x9, then it executes an if else for 9x9's 18 Board rotations
    % The if else below takes the s and t coordinates of ginput and returns
    % the corresponding rotation ID.
    if s==5 && t==1
        r=1;
    elseif s==7 && t==1
        r=2;
    elseif s==1 && t==6
        r=3;
    elseif s==11 && t==6
        r=4;
    elseif s==1 && t==7
        r=5;
    elseif s==1 && t==5
        r=6;
    elseif s==1 && t==4
        r=7;
    elseif s==4 && t==1
        r=8;
    elseif s==8 && t==1
        r=9;
    elseif s==11 && t==4
        r=10;
    elseif s==11 && t==5
        r=11;
    elseif s==11 && t==7
        r=12;
    elseif s==11 && t==8
        r=13;
    elseif s==8 && t==11
        r=14;
    elseif s==7 && t==11
        r=15;
    elseif s==5 && t==11
        r=16;
    elseif s==4 && t==11
        r=17;
    elseif s==1 && t==8
        r=18;
    else % If r is none of the above, it recursives ginput until a valid input is captured. 
        r=rotationmouseclick(Board);
    end
end
        
        