from multiprocessing import Process,Queue
import os, time

def write(q):
    print("启动write子进程：%s" %os.getpid())
    for i in ["A","B","C",'D']:
        q.put(i)
        time.sleep(1)
    print("结束write子进程：%s" %os.getpid())

def read(q):
    print("启动read子进程：%s" % os.getpid())
    while True:
        value = q.get(True)
        print(value)
    print("结束read子进程：%s" % os.getpid())

if __name__ == "__main__":
    #父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
    print('父进程结束')
