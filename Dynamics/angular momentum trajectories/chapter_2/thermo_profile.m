%Matlab script  thermo_profile.m
%This script shows simple example of reading in data and plotting a 
% monthly mean temperature profile versus pressure 

clear all        %clear the workspace
close all        % close all figures

% Note that data file to be loaded must consist entirely of columns of data
% Edit data to remove headers before loading
% In the example there are 3 columns corresponding to pressure, 
% temperature, and number of soundings respectively. each column has M rows
% A(3,M) is the matrix containing the data
% The data is at altitude interval of 0.5 km starting at z = 0 km

A = load('tropical_temp.dat');  %load the data

%plot temperature versus pressure 
figure(1)
subplot(1,2,1)
plot(A(:,2),A(:,1)) %plot 2nd row along x-axis,  first row along y-axis.
grid on
axis ij   %this statement reverses y-axis order
xlabel('Temperature (K)')
ylabel('pressure (hPa)')
title(' temperature vs pressure: tropical sounding')

%plot temperature versus altitude
%first define an altitude vector with M columns:

s = size(A);  %s is a row vector giving size of A

%note by using the size function the code will work for data files with
%different numbers of points.  
%statement below gives z with same number of rows as A

z = [.5:.5:.5*(s(1))] ; %defines row vector with z values at .5 km interval
subplot(1,2,2)
plot(A(:,2),z)
grid on
xlabel('Temperature K')
ylabel('altitude km')
title('temperature vs height: tropical sounding')

T = A(:,2)
P = A(:,1)
v = size(T)
%theta = zeros(v)
theta = T.*(1000./P).^(287/1004);
%GPH = zeros(v)
%for i = 1:v
%    theta(i) = T(i)*(1000/P(i))^(287/1004)
%    GPH(i) = 8.2*log(1000/P(i))
%end
phi = zeros(v)
for i=2:v
    phi(i)=phi(i-1)+287*(T(i-1)+T(i))/2/9.8*log(P(i-1)/P(i))
end
phi=phi./1000

figure(2)
subplot(1,2,1)
plot(T,P)
hold on
plot(theta,P)
grid on
axis ij   %this statement reverses y-axis order
xlim([0 1500])
%ylim([0 900])
xlabel('K')
ylabel('hPa')
title('T and Theta vsP: tropical sounding')

subplot(1,2,2)
plot(T,phi)
hold on
plot(theta,phi)
grid on
xlim([0 1500])
%ylim([0 45])
xlabel('K')
ylabel('km')
title('T and Theta vsGPH: tropical sounding')
