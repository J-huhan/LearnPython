def product(x, y,*args,**kwargs):
    s = x*y
    if len(args)>0:
        for i in args:
            s= s *i
    #print('kw=',kwargs)
    return s

def add(x,y,f):
    return f(x)+f(y)
'''
result = product(2,3,4,5,6,sum=3)
print('result =',result)
'''

print(add(-1,2,abs))