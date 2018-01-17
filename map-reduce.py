from functools import  reduce
def add (x,y):
    return x*10+y;
#sum = reduce(add,[1,2,3,4,5])
#print(sum)
def build(x,y):
    return lambda :x*x+y*y
s=build(1,2)
print(s())