function T=importCSV()

fileID = fopen('file.csv');
C = textscan(fileID,'%f %s %f %f',...
    'HeaderLines',2,'Delimiter',',');
fclose(fileID);

Time = C{1,1}; Event = C{1,2}; Zach=C{1,3}; Gray=C{1,4};
T=table(Time,Event,Zach,Gray);
end