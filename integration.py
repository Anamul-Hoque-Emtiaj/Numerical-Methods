import numpy as np
import matplotlib.pyplot as plt

def error(cur, prev):
    return abs((cur-prev)/cur)*100
def fvalue(x):
    numerator = 140000
    denominator = 140000 - (2100*x)
    return (2000*np.log(numerator/denominator)) - (9.8*x)

def plotGraph(xArray, yArray):
    plt.plot(xArray, yArray, marker="o")
    plt.xlabel("Oxygen concentration(moles/cc)")
    plt.ylabel("Time(s)")
    plt.show()
def TrapezoidalRuleSingleSegment(a,b):
    print("For ({:f},{:f}) ".format(a, b))
    print("a = {:f}, b = {:f}".format(a, b))
    print("f(a) = {:f}, f(b) = {:f} ".format(fvalue(a), fvalue(b)))
    res = ((b-a)*(fvalue(a)+fvalue(b)))/2
    print("({:f},{:f}) = {:f}\n".format(a, b, res))
    return res
def TrapezoidalRule(a,b,n):
    print("{:f} to {:f} integration with TrapezoidalRule".format(a, b))
    h = (b-a)/n
    print("I ", end="= ")
    for i in range(n):
        print("({:f},{:f}) ".format(a + (i * h), a + ((i + 1) * h)), end="+ ")
    print("\n\n")
    s = 0
    for i in range(n):
        s = s + TrapezoidalRuleSingleSegment(a+(i*h),a+((i+1)*h))
    return s

def SimpsonsOneThirdRuleSingleSegment(a,b):
    print("For ({:f},{:f}) ".format(a,b))
    print("a = {:f}, b = {:f}, (a + b / 2) = {:f} ".format(a,b,((a+b)/2)))
    print("f(a) = {:f}, f(b) = {:f}, f(a + b / 2) = {:f} ".format(fvalue(a), fvalue(b), fvalue((a + b) / 2)))
    res = (((b-a)*(fvalue(a)+(4*fvalue((a+b)/2))+fvalue(b)))/6)
    print("({:f},{:f}) = {:f}\n".format(a,b,res))
    return res

def SimpsonsOneThirdRule(a,b,n):
    print("{:f} to {:f} integration with SimpsonsOneThirdRule".format(a,b))
    h = (b - a) / (2 * n)
    print("I ",end="= ")
    for i in range(n):
        print("({:f},{:f}) ".format(a + (i*2*h),a + ((i+1)*2*h)), end=" +")
    print("\n\n")
    s = 0
    for i in range(0,n):
        s = s + SimpsonsOneThirdRuleSingleSegment(a+(i*h*2),a+((i+1)*2*h))
    return s

def task1(a,b):
    print("Solved with TrapezoidalRule:\n")
    print("n  --  Result  --  Error")

    prev = TrapezoidalRule(a, b, 1)
    print(1, prev, "N/A", sep="  --  ")
    for i in range(2,6):
        cur = TrapezoidalRule(a, b, i)
        err = error(cur, prev)
        prev = cur
        print(i, cur, err, sep="  --  ")

    print("\n\n")

def task2(a,b):
    print("Solved with SimpsonsOneThirdRule:\n")
    print("n  --  Result  --  Error")

    prev = SimpsonsOneThirdRule(a, b, 1)
    print(1, prev, "N/A", sep="  --  ")
    for i in range(2,6):
        cur = SimpsonsOneThirdRule(a, b, i)
        err = error(cur, prev)
        prev = cur
        print(i, cur, err, sep="  --  ")

    print("\n\n")

def task3(b):
    x = np.array([1.22, 1.20, 1.0, 0.8, 0.6, 0.4, 0.2])
    y = np.empty(shape=(len(x)),dtype=np.float64)
    for i in range(0,len(x)):
        x[i] = x[i]*pow(10,-4)
    for i in range(0,len(x)):
        y[i] = SimpsonsOneThirdRule(x[i],b,5)
    plotGraph(x,y)

a = 2
b = 6
#No. of sub section
n = 4
#print("{:f} to {:f} integration with TrapezoidalRule = {:f}".format(a,b,TrapezoidalRule(a,b,n)))
print("{:f} to {:f} integration with SimpsonsOneThirdRule = {:f}".format(a,b,SimpsonsOneThirdRule(a,b,n)))
"""
r1 = SimpsonsOneThirdRule(8,20,2)
print("A. with simpson's: ",r1)
r2 = TrapezoidalRule(20,30,2)
print("B. with Trapezoidal's: ",r2)
print("C = A + B = ", r1+r2)
"""