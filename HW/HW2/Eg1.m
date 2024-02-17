% Script Eg1_1
% Spherical Surface Area Increase

% Acquire and display the input data...
r = input('Enter radius (kilometers):');
delta_r = input('Enter increase (millimeters):');
clc
fprintf('Sphere radius   = %12.6f kilometers\n',r)
fprintf('Radius increase = %12.6f millimeters\n\n',delta_r)
disp('Surface Area Increase:')

% Convert from millimeters to kilometers...
dr = delta_r/10^6;

%Calculate original SA

area = 4*pi*r^2;
fprintf('\n   Original: %15.6f square meters',area)

% Method 1
delta_A1 = (4*pi*(r + dr)^2 -  4*pi*r^2)*10^6;
fprintf('\n   Method 1: %15.6f square meters\n',delta_A1)

% Method 2
delta_A2 = (4*pi*(2*r + dr)*dr)*10^6;
fprintf('   Method 2: %15.6f square meters\n',delta_A2)

% Method 3
delta_A3 = (8*pi*r*dr)*10^6;
fprintf('   Method 3: %15.6f square meters\n',delta_A3)

%Temperature in Farenheit to Celcius
temp = input('Enter temperature (Farenheit):');
fprintf('Temperature in Farenheit  = %12.6f degrees Farenheit\n',temp)
temp_c = (5/9)*(temp - 32);
fprintf('Temperature in Celsius    = %12.6f degrees Celsius\n',temp_c)