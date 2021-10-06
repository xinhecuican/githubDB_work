function yval = optimX(C)
T=importCSV();
yAtTf = [-20.0404 -11.5703];
tspan = [0 pi()/6 pi()/3];
y0 = [2;7];
[t,Y] = ode45(@(t,y) RKx(t,y,C),tspan,y0);
yval = norm(Y(3,:)-yAtTf,2);
end