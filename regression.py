import numpy as np
import matplotlib.pyplot as plt
import math

def fvalue(x):
    # y = e^a0 + e^(a1*x)
    return C[0] + C[1]*x

def plotGraph(xArray, yArray):
    xArr = np.arange(0,10,0.5)
    yArr = np.empty(shape=(len(xArr)), dtype=np.float64, order='F')
    for i in range(len(xArr)):
        yArr[i] = fvalue(xArr[i])
    plt.plot(xArr, yArr, color='green')
    for i in range(len(xArray)):
        plt.plot(xArray[i], yArray[i], marker="o", color='red')
    plt.xlabel("Blood alcohol level ")
    plt.ylabel("Relative Risk of Crashing")
    plt.show()

def plotPoint(xArray, yArray):
    for i in range(len(xArray)):
        plt.plot(xArray[i], yArray[i], marker="o", color='red')
    plt.xlabel("Blood alcohol level ")
    plt.ylabel("Relative Risk of Crashing")
    plt.show()

def max(A,t,n):
    maxi = t
    for i in range(t+1,n):
        if(abs(A[i][t])>abs(A[maxi][t])):
            maxi = i
    return maxi

def X(x):
    # X = x
    return x
def Y(y):
    # Y = log y
    return y

def GaussianElimination(A,B,n):
    # forward elimination
    for i in range(0, n - 1):
        mx = max(A, i,n) #for partial pivoting
        A[[i, mx]] = A[[mx, i]]
        B[i], B[mx] = B[mx], B[i]
        for j in range(i + 1, n):
            tArr = A[i] * (A[j][i] / A[i][i])
            cons = B[i] * (A[j][i] / A[i][i])
            A[j] = np.subtract(A[j], tArr)
            B[j] -= cons

    # back substitution
    X = np.empty(shape=(n), dtype=np.float64, order='F')
    for i in reversed(range(n)):
        sum = 0
        for j in range(i + 1, n):
            sum += X[j] * A[i][j]
        X[i] = (B[i] - sum) / A[i][i]
    return X

# generate Coefficient of linear equation
def generateCoefficient(xArray, yArray,n,s):
    A = np.empty(shape=(s, s), dtype=np.float64, order='C')
    B = np.empty(shape=(s), dtype=np.float64, order='F')
    for i in range(s):
        for j in range(s):
            c=0
            for k in range(n):
                c = c + pow(X(xArray[k]),i+j)
            A[i][j] = c
    for i in range(s):
        c = 0
        for j in range(n):
            c = c + (pow(X(xArray[j]), i)*Y(yArray[j]))
        B[i] = c
    return A,B


lines = []
with open('data.txt') as f:
    lines = f.readlines()

n = len(lines)
xArray = np.empty(shape=(n),dtype=np.float64)
yArray = np.empty(shape=(n),dtype=np.float64)

for i in range(0,n):
    s = lines[i].split()
    xArray[i] = float(s[0])
    yArray[i] = float(s[1])


plotPoint(xArray,yArray)
"""
we can see from the plot of points. the data best fits with exponential model.
so y = Ae^Bx
    log y = log A + Bx
    let Y = log y, X = x, a0 = log A, a1 = B
    now we find the linear equation,
    Y = a0 + a1*X
    we can find out a0, a1 by solving linear equation with GaussianElimination
    also we can reconstruct the A and B from a0 and a1
    where A = e^a0, B = a1
    so final equation would be
    y = e^a0 + e^(a1*x)
"""
s = 2
print("Write equation. And covert if needed")
A,B = generateCoefficient(xArray, yArray,n,s)
print("Coefficient matrix of linear equations:")
print(A)
print("Constant matrix of linear equations:")
print(B)
C = GaussianElimination(A,B,s)
plotGraph(xArray,yArray)
print("Constant:")
print(C)
print("Reconstruct main constant if you converted your equation")
x = 10
print("For X = {:f}, f(x) = {:f} ".format(x,fvalue(x)))
"""
# A = e^a0
print("A: {:.2f}".format(math.exp(C[0])))
# B = a1
print("B: {:.2f}".format(C[1]))
print("Equation: y = {:.2f}".format(math.exp(C[0])),"e^({:.2f}".format(C[1]),"*x)",sep="")

#problem 2
print("Relative Risk of Crashing for f(x = 0.16) = {:.2f}".format(fvalue(0.16)))
"""


