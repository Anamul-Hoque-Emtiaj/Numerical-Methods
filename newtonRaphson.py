import matplotlib.pyplot as plt
import numpy as np

# f(x) = x^3-0.18x^2+0.0004752 = 0
# f'(x) = 3x^2-0.36x = 0
def fvalue(x):
    return x*x*x - 0.18*x*x + 0.0004752
def f1value(x):
    return 3*x*x - 0.36*x

def showGraph():
    xvalue = np.arange(0,0.13,0.01)
    yvalue = np.array(fvalue(xvalue))

    plt.plot(xvalue,yvalue, marker="o", c="green", label="y=f(x)")
    plt.title("f(x) = x^3-0.18x^2+0.0004752 = 0")
    plt.axvline(x=0, c="red", label="x=0")
    plt.axhline(y=0, c="red", label="y=0")
    plt.legend()
    plt.show()

def error(cur,prev):
    return abs((cur-prev)/cur)*100.00

def newtonRaphson(x1,ee,mi):
    print("print f(x)")
    print("print f'(x)")
    print("initial guess: X1 = {:f}\n\n".format(x1))
    for i in range(1,mi+1):
        print("Iteration No.(i) {:d}".format(i))
        print("xi = {:f}, f(xi) = {:f}, f'(xi) = {:f}".format(x1,fvalue(x1),f1value(x1)))
        x2 = x1-(fvalue(x1)/f1value(x1))
        print("Xi+1 = {:f}".format(x2))
        err = error(x2,x1)
        print("error: {:f}".format(err))
        if(err<=ee):
            print("error is less than or equal to expected value")
            return x2
        x1=x2
        if (fvalue(x2) == 0):
            print("root found")
            return x2
        print("\n\n")
    return x2

def showTable(mi):
    collab = ["It. No.", "Root", "Relative approx. Error"]
    plt.axis("off")
    plt.table(cellText=errorTable, colLabels = collab, loc="center")
    plt.title("Absolute Relative Approximate Error")
    plt.show()

def modifiedNewtonRaphson(x1,mi):
    for i in range(1,mi+1):
        x2 = x1-(fvalue(x1)/f1value(x1))
        row = [i, x2, error(x2,x1)]
        errorTable.append(row)
        x1 = x2
    showTable(mi)

x = 0.05
ee = 1
mi = 20
errorTable = []

showGraph()
print("Approximate root: ", newtonRaphson(x,ee,mi))
#modifiedNewtonRaphson(x,mi)
