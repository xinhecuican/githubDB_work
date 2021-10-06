clear all
close all

% Select years 1908-1935
T=importCSV();
mytime = T.Time;
mydata(:,1) = T.Zach;
mydata(:,2) = T.Gray;


objfun = @(x) least_squares(x,mydata, mytime);

%% Optimisation using PSOPC with the same upper/lower bounds used in
%% simplex method
[k lest_squares] = PSOPC(objfun, 4, [0 0 0 0], [0.8 0.8 0.8 0.8], 500)

%% Plot model with estimated parameters
y0(1) = 2; y0(2) = 7;
[t,y] = ode45(@Lotka_Volterra_Model,mytime,y0,[],k);

subplot(2,1,1)
hold on
plot(mydata(:,1),'O');
plot(y(:,1),'--b')

subplot(2,1,2)
hold on
plot(mydata(:,2),'rO');
plot(y(:,2),'--r')

