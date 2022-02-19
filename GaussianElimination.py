import numpy as np

def show(A,B):
    print("\nArr A: ")
    for i in range(0,n):
        for j in range(0,n):
            print("{:.4f}".format(A[i][j]), end="  ")
        print("")
    print("\nArr B: ")
    for i in range(0, n):
        print("{:.4f}".format(B[i]))
    print("    ----\n")

def max(A,t):
    maxi = t
    for i in range(t+1,n):
        if(abs(A[i][t])>abs(A[maxi][t])):
            maxi = i
    return maxi

def GaussianElimination(A,B,pivot=True,showall=True):
    if (showall):
        show(A, B)
    # forward elemination
    for i in range(0, n - 1):
        if (showall):
            print("\nStep:",i+1)

        if(pivot): #for partial pivoting
            mx = max(A, i)
            if(mx!=i):
                print("swap between {:d} and {:d} rows".format(i,mx))
            A[[i, mx]] = A[[mx, i]]
            B[i], B[mx] = B[mx], B[i]
            show(A, B)
        for j in range(i + 1, n):
            if (showall):
                print("Sub-step:",j-i)
            print("row = {:d}, col = {:d}".format(j, i))
            print("Multiplier = A[{:d}][{:d}] / A[{:d}][{:d}] = {:f}".format(j,i,i,i,(A[j][i] / A[i][i])))
            print("A[{:d}] = ".format(j), A[j])
            print("B[{:d}] = ".format(j), B[j])
            print("A[{:d}] = ".format(i), A[i])
            print("B[{:d}] = ".format(i), B[i])
            print("A[{:d}] = A[{:d}] - Multiplier * A[{:d}]".format(j,j,i))
            print("B[{:d}] = B[{:d}] - Multiplier * B[{:d}]".format(j,j,i))
            tArr = A[i] * (A[j][i] / A[i][i])
            cons = B[i] * (A[j][i] / A[i][i])
            A[j] = np.subtract(A[j], tArr)
            B[j] -= cons
            print("A[{:d}] = ".format(j), A[j])
            print("B[{:d}] = ".format(j), B[j])
            if (showall):
                show(A, B)

    # back substituition
    X = np.empty(shape=(n), dtype=np.float64, order='F')
    for i in reversed(range(n)):
        sum = 0
        for j in range(i + 1, n):
            sum += X[j] * A[i][j]
        X[i] = (B[i] - sum) / A[i][i]
    return X


n = int(input())
A = np.empty(shape=(n,n),dtype=np.float64,order='C');
B = np.empty(shape=(n),dtype=np.float64,order='F');
for i in range(0,n):
    s = input().split()
    for j in range(0,n):
        A[i][j] = float(s[j])

for i in range(0,n):
    B[i] = float(input())


X = GaussianElimination(A,B)
print("Values  of  constants:")
for i in range(0,n):
    print("{:.4f}".format(X[i]))

"""
  𝑥^2  +  𝑦^2  +  𝑎𝑥  +  𝑏𝑦  +  𝑐  =   0...(i)
  putting (-2,0) at (i) we find the eqn,
  2a+0b-c = 4
  putting (-1,7) at (i) we find the eqn,
  a-7b-c = 50
  putting (5,-1) at (i) we find the eqn,
  5a-b+c = -26
  so the input for this programme will be,
  
  3
  2 0 -1
  1 -7 -1
  5 -1 1
  4
  50
  -26
  
  output:
  -4.0000
  -6.0000
  -12.0000
"""
