import matplotlib.pyplot as plt
import numpy as np


#eqn-> x^3-0.18x^2+0.0004752=0

def makeGraph():
    xvalue = np.arange(0,3,0.5)
    yvalue = np.array(fvalue(xvalue))

    plt.plot(xvalue,yvalue, marker = "o", label="y=f(x)")
    plt.title("y = f(x) = x^3 - 0.18x^2 + 0.0004752 = 0")
    plt.axvline(x=0, c="red", label="x=0")
    plt.axhline(y=0, c="yellow", label="y=0")
    plt.legend()
    plt.show()
def makeTable():
    modifiedBisection(l, u, e, mi)
    #fig, ax = plt.subplots(1, 1)

    column_labels = ["Iteration", " Approx Root ", "Approx. Error (in %)"]
    plt.axis('off')
    plt.table(cellText=table, colLabels=column_labels, loc="center")

    plt.show()

def error(cur,prev):
    return abs((cur-prev)/cur)*100
def fvalue(x):
    return x*x-np.sin(x)-0.5;

def bisection(l,u,e,mi):
    print("print function")
    print("initial guess: Xl = {:.7f}, Xu = {:.7f}\n\n".format(l,u))
    for i in range(1,mi+1):
        print("Iteration No. {:d}".format(i))
        print("Xl = {:.7f}, f(Xl) = {:.7f}".format(l,fvalue(l)))
        print("Xu = {:.7f}, f(Xu) = {:.7f}".format(u,fvalue(u)))
        m = (l + u) / 2
        print("Xm = (Xu + Xl)/2 = {:.7f}, f(Xm) = {:.7f}".format(m,fvalue(m)))
        if(i==1):
            pm = m
            print("Error not possible")
        if(i>1):
            err = error(m,pm)
            print("error: {:.7f}".format(err))
            if(err<=e):
                print("error is less than or equal to expected value")
                return m
            pm = m
        if (fvalue(l) * fvalue(m) == 0):
            print("root found")
            return m
        elif (fvalue(l) * fvalue(m) < 0):
            u = m
        else:
            l = m
        print("next iteration Xu and Xl comparing fValue\n\n")
    return m

def modifiedBisection(l,u,e,mi):
    for i in range(1,mi+1):
        m = (l + u) / 2
        if(i==1):
            pm = m
        if(i>1):
            err = error(m,pm)
            row = [i,m,err]
            table.append(row)
            pm = m
        if (fvalue(l) * fvalue(m) == 0):
            return m
        elif (fvalue(l) * fvalue(m) < 0):
            u = m
        else:
            l = m
    return m
l = -1
u = 0
e = 0.0005
mi = 5
makeGraph()
root = bisection(l,u,e,mi)
print("Approximate root: ",root)
table = [[1, (u + l) / 2, "N/A"]]
#makeTable()


