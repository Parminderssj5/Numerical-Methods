clear all;
clc;

h = 0.1; k = 0.1;
x = 3.0; y = 2.4;

cols = floor(x/h)+1;
rows = floor(y/k)+1;

nx = floor(x/h);
ny = floor(y/k);

M = zeros(rows, cols);
u = zeros(rows, cols);

tvalue = 300; bvalue = 50;
lvalue = 75; rvalue = 100;

for i = 1:rows
    M(i,1) = lvalue;
    M(i,cols) = rvalue;
end
for j = 1:cols
    M(1,j) = tvalue;
    M(rows,j) = bvalue;
end
for i = 1:rows
    u(i,1) = lvalue;
    u(i,cols) = rvalue;
end
for j = 1:cols
    u(1,j) = tvalue;
    u(rows,j) = bvalue;
end

N = 50;
tic;
for num = 1:N
    for j = 2:cols-1
        for i = 2:rows-1
            M(i,j) = 0.25*(M(i+1,j)+M(i-1,j)+M(i,j+1)+M(i,j-1));
        end
    end
end
disp("time taken for gauss seidel :")
toc;

X = zeros(rows,cols);
Y = zeros(rows,cols);
for i = 1:rows
    for j = 1:cols
        Y(i,j) = (rows-i)*k;
        X(i,j) = (j-1)*h;
    end
end

tic;
for num = 1:N
    A = -4*eye(nx-1);
    for t = 1:nx-2
        A(t,t+1) = 1;
    end
    for k = 2:nx-1
        A(k,k-1) = 1;
    end
    for i = 2:ny
        b = zeros(nx-1,1);
        for j = 1:nx-1
            b(j) = -1*(u(i-1,j+1) + u(i+1,j+1));
        end
        b(1) = b(1) - u(i,1);
        b(nx-1) = b(nx-1) - u(i,nx);
        sol = A\b;
        for r = 2:nx
            u(i,r) = sol(r-1); 
        end
    end

    A = -4*eye(ny-1);
    for t = 1:ny-2
        A(t,t+1) = 1;
    end
    for k = 2:ny-1
        A(k,k-1) = 1;
    end
    for j = 2:nx
        b = zeros(ny-1,1);
        for i = 1:ny-1
            b(i) = -1*(u(i+1,j-1) + u(i+1,j+1));
        end
        b(1) = b(1) - u(1,j);
        b(ny-1) = b(ny-1) - u(ny,j);
        sol = A\b;
        for r = 2:ny
            u(r,j) = sol(r-1); 
        end
    end       
end
disp("time taken for alternative direction implicit")
toc;
surf(X,Y,M);