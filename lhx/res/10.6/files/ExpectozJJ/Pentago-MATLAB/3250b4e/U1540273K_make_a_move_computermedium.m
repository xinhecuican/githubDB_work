function [pos_played,rotation_played] = U1540273K_make_a_move_computermedium(Board,who_to_play)
% This function generates a move the AI can make against its opponent. This
% is the easy mode of the AI. 
% Format of Call: U1540273K_make_a_move_computereasy(Board,who_to_play)
% Returns pos_played and rotation_played
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% This function calls another function to generate possible centre tiles AI
% can play, moves that can immediately from 4 in a row,column or diagonal
% to 5 in a row,column and diagonal to win or the opposite which is find
% locations (linear indexing) such that it needs to place a tile to block
% the opponent's 4 in a row, column of diagonal sequence. 
[criticalmove,centremoves] = BasicGenius(Board,who_to_play);
winningmoves = forthewin(Board,who_to_play);

% Below are a list of persistent variables for the min-max algorithm 
persistent count
if isempty(count)
    count=1;
end
persistent commove1
if isempty(commove1)
    commove1=[];
end
persistent comrot1
if isempty(comrot1)
    comrot1=[];
end
persistent commove2
if isempty(commove2)
    commove2=[];
end
persistent comrot2
if isempty(comrot2)
    comrot2=[];
end
persistent max1
if isempty(max1)
    max1=[];
end
persistent max2
if isempty(max2)
    max2=[];
end
persistent min1
if isempty(min1)
    min1=[];
end
persistent min2
if isempty(min2)
    min2=[];
end
persistent goodrot1
if isempty(goodrot1)
    goodrot1=[];
end
persistent goodrot2
if isempty(goodrot2)
    goodrot2=[];
end
persistent badrot1 
if isempty(badrot1)
    badrot1=[];
end
persistent badrot2
if isempty(badrot2)
    badrot2=[];
end
persistent i
persistent j
persistent boardai
if isempty(boardai)
    boardai=Board;
end
persistent defense
if isempty(defense)
    defense=[];
end

% First, it searches for linear indexes of moves it can possibly take from
% the current game state. 
x=find(boardai==0);

% I implement a switch statement on count where count is the increasing
% depth it recursives. 
switch count
    case 2 % This is depth 2 (count=2)
        for i=1:length(x) % It loops through all the possible linear indexes of moves the opponent can make. 
            player1move=x(i); % It then updates the board matrix. 
            boardai(player1move)=1;  
            win=determinewin(boardai); % Similarly, it checks for any win states from both players. 
            if  win==1 % If opponent wins, it takes the winning move as a defensive move it can make to prevent the opponent from making that move. 
                defense=[defense player1move]; % So it adds the move into the defense vector.
                commove1=setdiff(commove1,x(i)); % It then removes the move from the average moves as the heuristic value is now stronger.
                min1=[min1 x(i)]; % Since it is also a move that is advantageous to the opponent, it adds the move to the min.
                boardai=Board; % Since opponent wins, it resets boardai. 
                count=1; 
                break % It leaves the loop. 
            elseif win==0 % If there appears to be no winning state yet, it continues to run for loop for opponent's rotation move.
                for a=1:8 
                    boardai=ID(a,boardai); % Similarly, it updates board matrix based on rotation played. 
                    win=determinewin(boardai); % Check for possible winning states. 
                    if win==1 % If opponent wins, 
                        boardai=Board;
                        break
                    elseif win==0
                        count=count+1; % If no winning state yet, depth(count becomes 3).
                        U1540273K_make_a_move_computermedium(boardai,who_to_play) % Recursives function
                    end
                end
            end
        end
    case 1
        for i=1:length(x) % It loops through the possible moves the AI can make. 
            boardai(x(i))=3; % Updates the board matrix. 
            win=determinewin(boardai); % Determine if any party has won the game or draw. 
            if win==3 % If AI wins
                max1=[max1 x(i)]; % The move is then one of the best moves. 
                boardai=Board; % Leaves the loop
                break
            elseif win==1 % If opponent wins.
                min1=[min1 x(i)]; % The move is then one of the worst moves. 
                boardai=Board; 
                break % Leaves the loop
            elseif win==0 % If there is still no winning state.
                commove1=[commove1 x(i)]; % Adds move to the average moves list. 
                for j=1:8 % Continues loop with all possible rotations 
                    boardai=ID(j,boardai); % Updates board with rotations. 
                    win=determinewin(boardai); % Check winning conditions 
                    if win==3 % If AI wins.
                        goodrot1=[goodrot1 j]; % Adds rotation ID to the good rotation move.
                        boardai=Board; 
                        break % Leaves the loop 
                    elseif win==1 % If opponent wins. 
                        badrot1=[badrot1 j]; % Adds rotation ID to the bad rotation move.
                        boardai=Board;
                        break % Leaves the loop
                    elseif win==0 % If no winning state is achieved. 
                        comrot1=[comrot1 j]; % Adds average rotation move to the average rotation list. 
                    end
                end
            end
        end
    case 3
        for i=1:length(x) % Loops through all possible moves in depth 3 for AI
            boardai(x(i))=3; % Updates the board matrix 
            win=determinewin(boardai); % Checks for winning conditions 
            if win==3 % If AI wins.
                commove1=setdiff(commove1,x(i)); % Removes average move from its existing list
                max2=[max2 x(i)]; % Since it wins in depth 3, it is of just a lower state than best moves. Adds the move to max2.(2nd best move)
                boardai=Board;
                break % Leaves the loop
            elseif win==1 % If opponent wins. 
                commove1=setdiff(commove1,x(i)); % Removes move from average moves. 
                min2=[min2 x(i)]; % Since opponent wins in depth 3, this move becomes the 2nd worst type of moves. 
                boardai=Board;
                break % Leaves the loop 
            elseif win==0 % If no winning state 
                commove2=[commove2 x(i)]; % The depth 3 moves become an average set of moves 
                for j=1:8 % Continues gameplay with rotation 
                    boardai=ID(j,boardai); % Updates Board matrix 
                    win=determinewin(boardai); % Check winning conditions 
                    if win==3 % If AI wins 
                        comrot1=setdiff(comrot1,j); % Remove rotation ID from average rotations 
                        goodrot2=[goodrot2 j]; % It becomes one of the 2nd best rotations. 
                        boardai=Board; 
                        break % Leaves the loop 
                    elseif win==1 % If opponent wins.
                        comrot1=setdiff(comrot1,j); % Removes rotation ID from set of average rotations.
                        badrot2=[badrot2 j]; % It then becomes the 2nd worst rotation AI can play. 
                        boardai=Board; 
                        break % Leaves the loop 
                    elseif win==0 % If no winning state. 
                        comrot2=[comrot2 j]; % Rest of the rotations become just average rotational moves.
                        break % Leaves the loop. 
                    end
                end
            end
        end
    otherwise
        return
end

if count==1 % If at depth 1.
    if isempty(max1) % If there are no best moves. 
        count=count+1; % Increase search depth to 2. 
        U1540273K_make_a_move_computermedium(boardai,who_to_play) % Recursives function. 
    else
        pos_played=max1(randi([1,length(max1)])); % Randomise a move from the list of best moves.
        while Board(pos_played)~=0 % Error check if any of the best move is an invalid move on the game state. 
            pos_played=commove1(randi([1,length(commove1)])); % Randomise any average move from the average move list. 
        end
        if isempty(goodrot1) % If there is no good rotational moves detected. 
            rotation_played=comrot1(randi([1,length(comrot1)])); % Randomise a rotation to be played from the average list.
        else 
            rotation_played=goodrot1(randi([1,length(goodrot1)])); % Randomise a rotation from the set of good rotations 
        end
        count=1; % Resets depth to 1 
    end
elseif count==3
    if numel(max2)~=0 % If there is no 2nd best move. 
        pos_played=commove1(randi([1,length(commove1)])); % Randomise an average move from the average move list. 
        while Board(pos_played)~=0 % Error check 
            pos_played=commove1(randi([1,length(commove1)]));
        end
        if isempty(goodrot1)
            rotation_played=comrot1(randi([1,length(comrot1)]));
        else 
            rotation_played=goodrot1(randi([1,length(goodrot1)]));
        end     
    end
elseif count==2
    if numel(defense)~=0
        pos_played=defense(randi([1,length(defense)]));
        while Board(pos_played)~=0
            pos_played=defense(randi([1,length(defense)]));
        end
    else
        pos_played=commove1(randi([1,length(commove1)]));
        while Board(pos_played)~=0
            pos_played=commove1(randi([1,length(commove1)]));
        end
        if isempty(goodrot1)
            rotation_played=comrot1(randi([1,length(comrot1)]));
        else
            rotation_played=goodrot1(randi([1,length(goodrot1)]));
        end
        count=1;
    end
end

if numel(winningmoves)~=0
    pos_played=winningmoves(randi([1,length(winningmoves)]));
    while Board(pos_played)~=0
        pos_played=winningmoves(randi([1,length(winningmoves)]));
    end
    clear [pos_played,rotation_played] = U1540273K_make_a_move_computer(Board,who_to_play)
    return
elseif numel(criticalmove)~=0
    pos_played=criticalmove(randi([1,length(criticalmove)]));
    while Board(pos_played)~=0
        pos_played=criticalmove(randi([1,length(criticalmove)]));
    end
    clear [pos_played,rotation_played] = U1540273K_make_a_move_computer(Board,who_to_play)
    return
elseif numel(centremoves)~=0
    pos_played=centremoves(randi([1,length(centremoves)]));
    while Board(pos_played)~=0
        pos_played=centremoves(randi([1,length(centremoves)]));
    end
    clear [pos_played,rotation_played] = U1540273K_make_a_move_computer(Board,who_to_play)
    return
else
    clear [pos_played,rotation_played] = U1540273K_make_a_move_computer(Board,who_to_play)
    return
end
end





    


