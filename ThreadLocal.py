import  threading

#创建全局变量ThreadLocal对象
local_school = threading.local()

def process_thread(name):
    local_school.student = name
    std = local_school.student
    print('hello, %s (in %s)' % (std, threading.current_thread().name))

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()