%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% WELCOME TO PENTAGO! %%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This is our Pentago Game. It has 2 game boards, 6x6 and 9x9. 
% This is the start menu where the user chooses the game type and Settings.
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% Gets pentago icon from pentago folder 
icon=imread('Game.png','png');
% Loads message box welcoming users to Pentago 
q=msgbox('WELCOME TO PENTAGO','Pentago','custom',icon);
set(q,'color','white');
% Only if users click 'Ok', then main menu appears 
uiwait(q)
% Loads Main Menu 
boot=menu('WELCOME TO PENTAGO','6x6', '9x9 (PENTAGO XL)','Settings');

%% This set of variables below are global as its values needs to be saved upon launching Pentago subsequently. 
%   This is to maintain the settings set by the user such as the Theme
%   and Controls. This settings are set through the Settings GUI below. 
%   The Tile pieces are also global so that they can
%   be passed to the graphics subfunction to image the G_board. 
%   The variables are global so that users can actually save these settings. 
%   Variables global are also separate between 6x6 and Pentago XL so that
%   users can change the theme for 6x6 but not change theme for 9x9 or
%   change a different theme for 9x9. 
global tile1
if isempty(tile1)
    tile1='blue1.png';
end
global tile2
if isempty(tile2)
    tile2='blueblack.png';
end
global tile3
if isempty(tile3)
    tile3='bluewhite.png';
end
global tile4
if isempty(tile4)
    tile4='onepiece1.png';
end
global tile5
if isempty(tile5)
    tile5='onepiece2.png';
end
global tile6
if isempty(tile6)
    tile6='onepiece3.png';
end
global tile7
if isempty(tile7)
    tile7='onepiece4.png';
end
global tile8
if isempty(tile8)
    tile8='empty2.png';
end
global tileud
if isempty(tileud)
    tileud='blueud.png';
end
global tilelr
if isempty(tilelr)
    tilelr='bluelr.png';
end
global tilerl
if isempty(tilerl)
    tilerl='bluerl.png';
end
global tiledu
if isempty(tiledu)
    tiledu='bluedu.png';
end
global tileborder
if isempty(tileborder)
    tileborder='blueborder.png';
end
global arrow1
if isempty(arrow1)
    arrow1='onepiecedu.png';
end
global arrow2
if isempty(arrow2)
    arrow2='onepiecelr.png';
end
global arrow3
if isempty(arrow3)
    arrow3='onepiecerl.png';
end
global arrow4
if isempty(arrow4)
    arrow4='onepieceud.png';
end
global arrowborder
if isempty(arrowborder)
    arrowborder='border.png';
end

% Here, m is a variable that defines control inputs (Keyboard or Mouse)
global m
if isempty(m)
    m=0; % Mouse clicking is default setting 
end
%%

% Choose the size of the board
switch boot 
    case 1 % board of size 6-by-6
        Board=uint8(zeros(6));
        game=menu('PENTAGO', 'Start a New Game', 'Load Existing Game');
        % Choose to load existing game or start a new game
        switch game
            case 1 % start a new game
                six=menu('PENTAGO 6x6', 'Human Vs Computer', 'Human Vs Human');
                switch six
                    case 1
                        mode=menu('Human Vs Computer','Easy','Medium','Hard');
                        switch mode
                            case 1
                                d='e';
                                x='C'; % Loads menu for Human Vs AI.
                                start=menu('PENTAGO 6x6', 'Human goes first', 'Computer goes first');
                                switch start
                                    case 1
                                        who_to_play=2; % Human foes first
                                    case 2
                                        who_to_play=1; % AI goes first
                                end
                                uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                                % G_board is the display function for the graphical interface of the board.
                                G_board=graphics(Board);
                                % This then calls another function to initialise the start of the game.
                                Begin(Board,who_to_play,x,d)
                            case 2
                                d='m';
                                x='C'; % Loads menu for Human Vs AI.
                                start=menu('PENTAGO 6x6', 'Human goes first', 'Computer goes first');
                                switch start
                                    case 1
                                        who_to_play=2; % Human foes first
                                    case 2
                                        who_to_play=1; % AI goes first
                                end
                                uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                                % G_board is the display function for the graphical interface of the board.
                                G_board=graphics(Board);
                                % This then calls another function to initialise the start of the game.
                                Begin(Board,who_to_play,x,d)
                            case 3
                                d='h';
                                x='C'; % Loads menu for Human Vs AI.
                                start=menu('PENTAGO 6x6', 'Human goes first', 'Computer goes first');
                                switch start
                                    case 1
                                        who_to_play=2; % Human foes first
                                    case 2
                                        who_to_play=1; % AI goes first
                                end
                                uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                                % G_board is the display function for the graphical interface of the board.
                                G_board=graphics(Board);
                                % This then calls another function to initialise the start of the game.
                                Begin(Board,who_to_play,x,d)
                        end
                    case 2
                        x='H'; % 2 Player Mode
                        human=menu('PENTAGO 6x6', 'Player 1 goes first', 'Player 2 goes first');
                        switch human
                            case 1 
                                who_to_play=2; % Player 1 starts first
                                d='n';
                            case 2
                                who_to_play=3; % Player 2 starts first 
                                d='n';
                        end
                        uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                        % G_board is the display function for the graphical interface of the board.
                        G_board=graphics(Board);
                        % This then calls another function to initialise the start of the game.
                        Begin(Board,who_to_play,x,d)
                end
            case 2 % load existing game
                try
                    [Board,sg]=loadfile();
                catch
                    return
                end
                who_to_play=sg.b;
                x=sg.c;
                [g,h]=size(Board);
                if g==6
                    d=sg.d;
                    uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                    % G_board is the display function for the graphical interface of the board.
                    G_board=graphics(Board);
                    % This then calls another function to initialise the start of the game.
                    Begin(Board,who_to_play,x,d)
                elseif h==9
                    waitfor(msgbox('Saved Game is for Pentago XL... Loading Pentago XL','Pentago','custom',icon))
                    uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                    % G_board is the display function for the graphical interface of the board.
                    G_board=graphicsnine(Board);
                    % This then calls another function to initialise the start of the game.
                    Begin9(Board,who_to_play,x)
                end
        end
    case 2 % board of size 9-by-9
        Board=uint8(zeros(9)); % unsigned 8 bit 9x9 matrix of zeros 
        game=menu('PENTAGO', 'Start a New Game', 'Load Existing Game');
        switch game
            case 1 % Select 2 Player, 3 Player and 4 Player Modes 
                nine=menu('PENTAGO XL', '2 Player', '3 Player','4 Player');
                switch nine
                    case 1
                        x=2; % 2 Player Mode 
                        fun=menu('2 Player','Player 1 goes first','Player 2 goes first');
                        switch fun
                            case 1
                                who_to_play=1; % Player 1 goes first 
                            case 2
                                who_to_play=2; % Player 2 goes first 
                        end
                    case 2
                        x=3; % 3 Player mode 
                        who_to_play=randi([1,3]); % Randomly selects which player goes first 
                        switch who_to_play
                            case 1
                                disp('Player 1 goes first')
                            case 2
                                disp('Player 2 goes first')
                            case 3
                                disp('Player 3 goes first')
                        end
                    case 3
                        x=4; % 4 Player Mode 
                        who_to_play=randi([1,4]); % Randomly selects which player goes first 
                        switch who_to_play
                            case 1 
                                disp('Player 1 goes first')
                            case 2
                                disp('Player 2 goes first')
                            case 3
                                disp('Player 3 goes first')
                            case 4
                                disp('Player 4 goes first')
                        end
                end
                uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                % Loads graphical Board for Pentago XL 
                G_board=graphicsnine(Board);
                % Starts Game by calling subfunction 
                Begin9(Board,who_to_play,x)
            case 2 % load existing game
                try
                    [Board,sg]=loadfile();
                catch
                    return
                end
                who_to_play=sg.b;
                x=sg.c;
                [g,h]=size(Board);
                if g==6
                    waitfor(msgbox('Saved Game is for Pentago 6x6.. Loading 6x6 Pentago','Pentago','custom',icon))
                    uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                    % G_board is the display function for the graphical interface of the board.
                    G_board=graphics(Board);
                    % This then calls another function to initialise the start of the game.
                    Begin(Board,who_to_play,x,d)
                elseif h==9
                    uiwait(msgbox('Game will autosave at every turn. Please exit only when you have completed your move.','Pentago','custom',icon))
                    % G_board is the display function for the graphical interface of the board.
                    G_board=graphicsnine(Board);
                    % This then calls another function to initialise the start of the game.
                    Begin9(Board,who_to_play,x)
                end
        end
    case 3 % This is the Settings UI
        settings=menu('Settings','Select Theme','Controls','Back to Main Menu');
        switch settings
            case 1 % Select Theme of tile pieces
                Theme=menu('Theme','6x6','9x9');
                switch Theme
                    case 1 % 6x6 tile pieces
                        tilepieces=menu('Theme','Red and Blue','Simple Blue(Default)','One Piece','Back');
                        switch tilepieces
                            case 1 % The default red and blue tile pieces provided by Prof Thomas
                                tile1='empty.png';
                                tile2='red.png';
                                tile3='blue.png';
                                tileborder='norot.png';
                                tileud='rotud.png';
                                tilelr='rotlr.png';
                                tilerl='rotrl.png';
                                tiledu='rotdu.png';
                                PENTAGO()
                            case 2 % Simple Blue
                                tile1='blue1.png';
                                tile2='blueblack.png';
                                tile3='bluewhite.png';
                                tileborder='blueborder.png';
                                tileud='blueud.png';
                                tilelr='bluelr.png';
                                tilerl='bluerl.png';
                                tiledu='bluedu.png';
                                PENTAGO()
                            case 3 % One Piece Theme 
                                tile1='empty2.png';
                                tile2='onepiece1.png';
                                tile3='onepiece2.png';
                                tileud='onepieceud.png';
                                tilelr='onepiecelr.png';
                                tilerl='onepiecerl.png';
                                tiledu='onepiecedu.png';
                                tileborder='border.png';
                                PENTAGO()
                            case 5 % Returns to main menu 
                                PENTAGO()
                        end
                    case 2 % Choose tile pieces for Pentago XL 
                        tilepick=menu('Select Theme','RGBY','One Piece(Default)');
                        switch tilepick
                            case 1 % It applies the tile pieces to all 4 (just in case 3 or 4 Player Mode) 
                                tile4='red.png';
                                tile5='blue.png';
                                tile6='yellow.png';
                                tile7='green.png';
                                tile8='empty.png';
                                arrow1='rotdu.png';
                                arrow2='rotlr.png';
                                arrow3='rotrl.png';
                                arrow4='rotud.png';
                                arrowborder='norot.png';
                                PENTAGO()
                            case 2 % It applies the tile pieces to all 4 (just in case 3 or 4 Player Mode) 
                                tile4='onepiece1.png';
                                tile5='onepiece2.png';
                                tile6='onepiece3.png';
                                tile7='onepiece4.png';
                                tile8='empty2.png';
                                arrow1='onepiecedu.png';
                                arrow2='onepiecelr.png';
                                arrow3='onepiecerl.png';
                                arrow4='onepieceud.png';
                                arrowborder='border.png';
                                PENTAGO()
                            case 3 % Returns to Main Menu 
                                PENTAGO()
                        end
                end
            case 2 % This is a Simple Controls UI to select mouse or keyboard input 
                control=menu('Controls','Keyboard','Mouse Clicking (Default)','Back');
                switch control
                    case 1
                        m=1; % c=1 enables Keyboard Controls 
                        o=msgbox('Keyboard Control Selected. Moves are played by Linear Indexing and Rotation IDs.','Keyboard Input','help');
                        waitfor(o)
                        PENTAGO()
                    case 2
                        m=0; %c=0 enables Mouse controls 
                        disp('Mouse Input Selected.')
                        PENTAGO()
                    case 3 % Returns to Main Menu 
                        PENTAGO()
                end
            case 3 % Returns to Main Menu 
                PENTAGO()
        end
end
    






