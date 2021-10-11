function [Board,sg]=loadfile()
% This function is to load a valid saved game of Pentago to continue
% playing.
% Format of Call: loadfile()
% Returns Board and sg data structure
% Created by WEE JUNJIE U1540273K
% AY2015/16 Sem 1 
% MH1401 ALGORITHMS & COMPUTING I Project

% This command opens the open file dialog box. 
filename = uigetfile;
% From here, filename is the variable with the string value of the name of
% the file in mat extension. 
try
    load(filename) % Load data structure sg from valid file 
catch
    o=questdlg('No Saved Game Selected!!','Error','Return to Main Menu','Exit','Exit'); % If invalid file detected, it prompts for dialog box
    switch o
        case 'Return to Main Menu'
            Pentago % This recursives the function back to the main Pentago script.
            return
        case 'Exit' % Ends function 
            return
    end
end

try
    Board=sg.a; % Board matrix is the first array of the data structure. 
catch
    z=questdlg('Invalid File Detected!! File must contain structure sg.','Error','Load another file','Return to Main Menu','Exit','Exit');
    switch z % This prompts another dialog box to load another file or return to main menu or exit. 
        case 'Load another file'
            [Board,sg]=loadfile(); % This recursives this load file function again. 
        case 'Return to Main Menu'
            Pentago % This recursives back to the Pentago main script. 
            return
        case 'Exit' % This ends the function 
            return
    end
end
end