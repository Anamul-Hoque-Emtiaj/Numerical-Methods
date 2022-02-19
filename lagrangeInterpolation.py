import numpy as np

def error(cur, prev):
    return abs((cur-prev)/cur)*100

def printNearestPoint(l,s,x):
    print("We have to take {:d} Nearest Points for {:d} order interpolation. They are".format(s,s-1))
    for i in range(s):
        print("x{:d} = {:f}, f(x{:d}) = {:f}".format(i,xArray[l+i],i,yArray[l+i]))
    print("x = {:f}".format(x))

def lagrangeInterpolaion(x,n,s):
    for i in range(0,n):
        if(xArray[i]>x):
            h = i
            l = i-1
            break
    for i in range(2,s):
        if(l==0):
            h=h+1
        elif(h==n-1):
            l = l-1
        elif(abs(xArray[l-1]-x)<abs(xArray[h+1]-x)):
            l = l-1
        else:
            h = h+1
    sum = 0
    print("Write ideal equation like y = L0(x)f(x0) + L1(x)f(x1) + L2(x)f(x2)")
    printNearestPoint(l,s,x)
    print("Constant:")
    for i in range(s):
        r = 1
        for j in range(s):
            if(i!=j):
                r = r*(((x-xArray[l+j])/(xArray[l+i]-xArray[l+j])))
        print("L{:d} = {:f}".format(i,r))
        sum = sum + (r*yArray[l+i])
    return sum


n = int(input())
xArray = np.empty(shape=(n),dtype=np.float64)
yArray = np.empty(shape=(n),dtype=np.float64)
for i in range(0,n):
    s = input().split()
    #print(s,float(s[1]))
    xArray[i] = float(s[0])
    yArray[i] = float(s[1])
x = 4
s = 4
print("Approximate value for {:f} is {:f}\n".format(x,lagrangeInterpolaion(x,n,s)))

