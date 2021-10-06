function Board=ID(r,Board)
% This function rotates a 3-by-3 sub-board based on the number chosen,r
% which is the rotation ID input by user
% Format of Call: ID(r,Board)
% Returns Board 
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Stores dimensions of board in variables 
[a,b]=size(Board);

% Board of size 6-by-6: Executes rotation for IDs 1 to 8    
if a==6
    switch r % r refers to the rotation ID 
        case 1  
            Board(1:3,4:6)=rot90(Board(1:3,4:6),-1);
        case 2
            Board(1:3,4:6)=rot90(Board(1:3,4:6));
        case 3
            Board(4:6,4:6)=rot90(Board(4:6,4:6),-1);
        case 4
            Board(4:6,4:6)=rot90(Board(4:6,4:6));
        case 5
            Board(4:6,1:3)=rot90(Board(4:6,1:3),-1);
        case 6
            Board(4:6,1:3)=rot90(Board(4:6,1:3));
        case 7
            Board(1:3,1:3)=rot90(Board(1:3,1:3),-1);
        case 8
            Board(1:3,1:3)=rot90(Board(1:3,1:3));
        otherwise % Error check for any invalid keyboard entry 
            disp('Invalid Rotation ID')
            r=input('Please enter your rotation move: ');
            Board=ID(r,Board);
    end
% Board of size 9-by-9: Executes rotation for IDs 1 to 18    
elseif b==9
    switch r 
        case 1
            Board(1:3,4:6)=rot90(Board(1:3,4:6),-1);
        case 2
            Board(1:3,4:6)=rot90(Board(1:3,4:6));
        case 3
            Board(4:6,4:6)=rot90(Board(4:6,4:6),-1);
        case 4
            Board(4:6,4:6)=rot90(Board(4:6,4:6));
        case 5
            Board(4:6,1:3)=rot90(Board(4:6,1:3),-1);
        case 6
            Board(4:6,1:3)=rot90(Board(4:6,1:3));
        case 7
            Board(1:3,1:3)=rot90(Board(1:3,1:3),-1);
        case 8
            Board(1:3,1:3)=rot90(Board(1:3,1:3));
        case 9
            Board(1:3,7:9)=rot90(Board(1:3,7:9),-1);
        case 10
            Board(1:3,7:9)=rot90(Board(1:3,7:9));
        case 11
            Board(4:6,7:9)=rot90(Board(4:6,7:9),-1);
        case 12
            Board(4:6,7:9)=rot90(Board(4:6,7:9));
        case 13
            Board(7:9,7:9)=rot90(Board(7:9,7:9),-1);
        case 14
            Board(7:9,7:9)=rot90(Board(7:9,7:9));
        case 15
            Board(7:9,4:6)=rot90(Board(7:9,4:6),-1);
        case 16
            Board(7:9,4:6)=rot90(Board(7:9,4:6));
        case 17
            Board(7:9,1:3)=rot90(Board(7:9,1:3),-1);
        case 18
            Board(7:9,1:3)=rot90(Board(7:9,1:3));
        otherwise % Error check for invalid keyboard entry
            disp('Invalid Rotation ID')
            r=input('Please enter your rotation move: ');
            Board=ID(r,Board); % Recursives function 
    end
    
end

        