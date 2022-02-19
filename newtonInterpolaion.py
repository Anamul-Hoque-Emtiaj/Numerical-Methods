import numpy as np

def error(cur, prev):
    return abs((cur-prev)/cur)*100

def constant(r,c):
    if(b[r][c]!=0):
        return b[r][c]
    if(r-c==1):
        b[r][c] = (yArray[r] - yArray[c]) / (xArray[r] - xArray[c])
    else:
        x = constant(r, c + 1)
        y = constant(r - 1, c)
        b[r][c] = ((x - y) / (xArray[r] - xArray[c]))
    return b[r][c]
def printConstant(l,s):
    print("Constant")
    for i in range(s):
        print("b{:d} = {:f}".format(i,b[l+i][l]))

def printNearestPoint(l,s,x):
    print("We have to take {:d} Nearest Points for {:d} order interpolation. They are".format(s,s-1))
    for i in range(s):
        print("x{:d} = {:f}, f(x{:d}) = {:f}".format(i,xArray[l+i],i,yArray[l+i]))
    print("x = {:f}".format(x))
def newtonInterpolaion(x,n,s):
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
    constant(n - 1, 0)
    print("Write ideal equation like y = b0 + b1x + b2x2")
    printNearestPoint(l,s,x)
    printConstant(l,s)
    sum=b[l][l]
    r=1
    for i in range(1,s):
        r = r*(x-xArray[i-1+l])
        sum = sum + r*b[l+i][l]
    return sum


n = int(input())
xArray = np.empty(shape=(n),dtype=np.float64)
yArray = np.empty(shape=(n),dtype=np.float64)
b = np.zeros(shape=(n,n),dtype=np.float64)
for i in range(0,n):
    s = input().split()
    #print(s,float(s[1]))
    xArray[i] = float(s[0])
    yArray[i] = float(s[1])
    b[i][i] = float(s[1])
x = 16
s = 4
print("Approximate value for {:f} is {:f}\n".format(x,newtonInterpolaion(x,n,s)))

