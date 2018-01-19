import time
#设计一个装饰器，作用在任何函数上，打印当前函数的执行时间

def RequestMapping(url):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(time.localtime(time.time()))
            print('url=',url,'funcname=',func.__name__)
            func(*args,**kwargs)
        return wrapper
    return decorator

@RequestMapping('mydemo')
def output():
    print('it\'s a decorator demo')

output()