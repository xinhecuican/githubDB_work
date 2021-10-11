function T=importCSV()

fileID = fopen('Rydin1988.csv');
C = textscan(fileID,'%s %f %f %f %f',...
    'HeaderLines',1,'Delimiter',',');
fclose(fileID);

Area = C{1,4}; Species = C{1,5};
T=table(Area,Species);
end