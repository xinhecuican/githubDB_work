function Begin(Board,who_to_play,x,d)
% This is the function that starts the Pentago 6x6 game from the start menu.
% Just in case the loaded game already is in a winning state, it checks the
% board for any win conditions by calling victory test. 
% Format Of Call: Begin(Board,who_to_play,x) 
% where x is Human Vs AI or 2 Player Mode
% who_to_play is whose turn to play
% Board is the 6x6 Board Matrix
% It also takes in the global variable c where c is the user input from
% settings GUI. (whether the game is played by keyboard or mouse clicking)
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

global m % Uses the global variable c from Settings GUI

win=victorytest(Board); % Calls the subfunction to check winning state

if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
    disp('Draw')
    sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
    save('pentago.mat','sg','-mat')
    ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
    switch ww
        case 'Yes'
            PENTAGO()
        case 'No'
            return
    end
    return
elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
    disp('Draw')
    sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
    save('pentago.mat','sg','-mat')
    ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
    switch ww
        case 'Yes'
            PENTAGO()
        case 'No'
            return
    end
    return
elseif win(1)==1 % If AI has 5 in a row
    disp('AI wins')
    sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
    save('pentago.mat','sg','-mat')
    ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
    switch ww
        case 'Yes'
            PENTAGO()
        case 'No'
            return
    end
    return
elseif win(2)==1 % If Player 1 has 5 in a row
    disp('Player 1 wins')
    sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
    save('pentago.mat','sg','-mat')
    ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
    switch ww
        case 'Yes'
            PENTAGO()
        case 'No'
            return
    end
    return
elseif win(3)==1 % If Player 2 has 5 in a row
    disp('Player 2 wins')
    sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
    save('pentago.mat','sg','-mat')
    ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
    switch ww
        case 'Yes'
            PENTAGO()
        case 'No'
            return
    end
    return
end

if win==0 % If there is no winning state, game starts.
    if who_to_play==1 % This is the Computer's turn. 
        disp('Computer''s turn') % This calls the AI function to generate a move and rotation.
        if d=='e'
            q=find(Board==0);
            pos_played=q(randi([1,length(q)]));
            rotation_played=randi([1,8]);
        elseif d=='m'
            [pos_played,rotation_played] = U1540273K_make_a_move_computermedium(Board,who_to_play);
        elseif d=='h'
            [pos_played,rotation_played] = U1540273K_make_a_move_computerHard(Board,who_to_play);
        end
        Board(pos_played)=1; % Updates the Board matrix
        graphics(Board); % Updates the graphical interface
        pause(1)
        win=victorytest(Board); % Checks winning state again. 
        % Reads the win vector and prints the winning result if it exists
        % or else the game continues.
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        Board=ID(rotation_played,Board); % If no winning state, Computer continues to play rotation and updates Board matrix.
        graphics(Board); % Updates graphical interface again.
        pause(1)
        win=victorytest(Board); % It then checks for winning states again. 
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        who_to_play=2; % Transfers turn to Player 1
        sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
        save('pentago.mat','sg','-mat')
        Begin(Board,who_to_play,x,d) % Recursives function 
    elseif who_to_play==2 
        disp('Player 1''s turn')
        if m==0 % Mouse Clicking
            try 
                [i,j]=ginput(1); % Uses ginput built in function to get coordinates
            catch 
                return;
            end
            s=floor(i/504); % s is the columns of the Board 
            t=floor(j/504); % t is the rows of the Board 
            while s<=0 || s>=7 || t<=0 || t>=7 % No output if user clicks anywhere else 
                try
                    [i,j]=ginput(1); % Uses ginput built in function to get coordinates
                catch
                    return;
                end
                s=floor(i/504);
                t=floor(j/504);
            end
            while Board(t,s)~=0 % If Board entry is filled, Invalid Move. 
                disp('Invalid Move!')
                try
                    [i,j]=ginput(1); % Uses ginput built in function to get coordinates
                catch
                    return;
                end
                s=floor(i/504);
                t=floor(j/504);
            end
            Board(t,s)=2; % Changes Board entry with clicked move.
        elseif m==1 % KeyBoard Input Control 
            SpaceID=input('Please enter your next move: '); % Prompts for input
            while SpaceID<1 || SpaceID>36 % Error checks if user input is out of range
                disp('Invalid Move!')
                SpaceID=input('Please enter your next move: ');
            end
            while Board(SpaceID)~=0 % Error checks if user entered an invalid entry 
                disp('Invalid Move!')
                SpaceID=input('Please enter your next move: ');
            end
            Board(SpaceID)=2; % Changes Board entry with desired move 
        end
        graphics(Board); % Updates Graphics of Board 
        win=victorytest(Board); % Checks for winning state 
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        if m==0 % Mouse Clicking for Rotation input 
            try 
                r=rotationmouseclick(Board); % Calls Rotation subfunction 
            catch
                return;
            end
            Board=ID(r,Board); % Updates Rotated Board with matrix subfunction 
        elseif m==1 % Keyboard Control for Rotation input
            r=input('Please enter your rotation move: '); % Prompts for input
            while r<1 || r>8 || int32(r)~=r % Checks if input is integer or out of range 
                disp('Invalid Rotation Entered')
                r=input('Please enter your rotation move: '); % Re-prompts for input 
            end
            Board=ID(r,Board); % Updates Board with rotated matrix 
        end
        graphics(Board); % Updates Graphics
        win=victorytest(Board); % Checks for winning state again 
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        if x=='C' 
            who_to_play=1; % If game is played against AI, transfers turn to AI.
        else
            who_to_play=3; % If game is played against another player, transfers to player 2. 
        end
        sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
        save('pentago.mat','sg','-mat')
        Begin(Board,who_to_play,x,d) % Recursives function
    elseif who_to_play==3 % Player 2's turn 
        disp('Player 2''s turn')
        if m==0 % Mouse Clicking
            try
                [i,j]=ginput(1); % Uses ginput built in function to get coordinates
            catch
                return;
            end
            s=floor(i/504); % s is the columns of the Board 
            t=floor(j/504); % t is the rows of the Board 
            while s<=0 || s>=7 || t<=0 || t>=7 % No output if user clicks anywhere else 
                try
                    [i,j]=ginput(1); % Uses ginput built in function to get coordinates
                catch
                    return;
                end
                s=floor(i/504);
                t=floor(j/504);
            end
            while Board(t,s)~=0 % If Board entry is filled, Invalid Move. 
                disp('Invalid Move!')
                try
                    [i,j]=ginput(1); % Uses ginput built in function to get coordinates
                catch
                    return;
                end
                s=floor(i/504);
                t=floor(j/504);
            end
            Board(t,s)=3; % Changes Board entry with clicked move.
        elseif m==1 % KeyBoard Input Control 
            SpaceID=input('Please enter your next move: '); % Prompts for input
            while SpaceID<1 || SpaceID>36 % Error checks if user input is out of range
                disp('Invalid Move!')
                SpaceID=input('Please enter your next move: ');
            end
            while Board(SpaceID)~=0 % Error checks if user entered an invalid entry 
                disp('Invalid Move!')
                SpaceID=input('Please enter your next move: ');
            end
            Board(SpaceID)=3; % Changes Board entry with desired move 
        end
        graphics(Board); % Updates Graphics of Board 
        win=victorytest(Board); % Checks for winning state 
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        if m==0 % Mouse Clicking for Rotation input 
            try 
                r=rotationmouseclick(Board); % Calls Rotation subfunction
            catch 
                return;
            end
            Board=ID(r,Board); % Updates Rotated Board with matrix subfunction 
        elseif m==1 % Keyboard Control for Rotation input
            r=input('Please enter your rotation move: '); % Prompts for input
            while r<1 || r>8 || int32(r)~=r % Checks if input is integer or out of range 
                disp('Invalid Rotation Entered')
                r=input('Please enter your rotation move: '); % Re-prompts for input 
            end
            Board=ID(r,Board); % Updates Board with rotated matrix 
        end
        graphics(Board); % Updates Graphics
        win=victorytest(Board); % Checks for winning state again 
        if sum(win)>1 % If 2 players achieved 5 in a row simultaneously.
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif sum(win)==0 && sum(any(Board==0))==0 % If Board is full and no winning state
            disp('Draw')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(1)==1 % If AI has 5 in a row
            disp('AI wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(2)==1 % If Player 1 has 5 in a row
            disp('Player 1 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        elseif win(3)==1 % If Player 2 has 5 in a row
            disp('Player 2 wins')
            sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
            save('pentago.mat','sg','-mat')
            ww=questdlg('Would you like to play again?','Pentago','Yes','No','No');
            switch ww
                case 'Yes'
                    PENTAGO()
                case 'No'
                    return
            end
            return
        end
        who_to_play=2; % Transfers to player 1.
        sg=struct('a',Board,'b',who_to_play,'c',x,'d',d);
        save('pentago.mat','sg','-mat')
        Begin(Board,who_to_play,x,d) % Recursives fucntion
    end
end
end




    

