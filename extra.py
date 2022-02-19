def fvalue(x):
    return x
def error(cur,prev):
    return abs((cur-prev)/cur)*100

print(fvalue(1))
print(error(1,1))