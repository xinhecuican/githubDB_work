%
% Copyright (c) 2016, Yarpiz (www.yarpiz.com)
% All rights reserved. Please read the "license.txt" for license terms.
%
% Project Code: YTEA101
% Project Title: Particle Swarm Optimization Video Tutorial
% Publisher: Yarpiz (www.yarpiz.com)
% 
% Developer and Instructor: S. Mostapha Kalami Heris (Member of Yarpiz Team)
% 
% Contact Info: sm.kalami@gmail.com, info@yarpiz.com
%

function z = Objective(x)

T=importCSV();
options = odeset('RelTol', 1e-4, 'NonNegative', [1 2]);
t=T.Time; y=[T.Zach,T.Gray];
[t,x] = ode45(@(t,y) RKx(t,y,x), [0 20], [10 10], options);
plot(t,x);
hold on;
end
