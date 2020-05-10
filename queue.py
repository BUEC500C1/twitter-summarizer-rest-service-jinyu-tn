#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:05:12 2020

@author: taimaame
"""


import Queue
import time
import threading
from imagestovideo import imagetovideo


def worker(i):
    while True:
        item=q.get()
        if item is None:
            f.write("The task of thread %s is None, relax for a moment\n" %i)
            print("The task of thread %s is None, relax for a moment" %i)
            break
        f.write("Thread %s is processing on %s's task\n" %(i,item))
        print("Thread %s is processing on %s's task" %(i,item))
        imagetovideo(item,'USA')
        f.write("Thread %s finished %s's task\n"%(i, item))
        print("Thread %s finished %s's task"%(i, item))
        q.task_done()
    
if __name__ == '__main__':
    
    
    

    
    
    f = open('./test.txt','w')
    
    username =['brad','suli','mulla','pig','cat','dog']
    #keyword = ['juul','alcohol','star','cooking','miao','wang']
    #source = (('brad','juul'),('suli,''alcohol'),('Mulla','star'))
    
    num_of_threads = 3
    # build a new FIFO queue:
    q = Queue.Queue()
    # build a threadspool:
    threads = []
    # build threads and put them into threads pool
    for i in range(1,num_of_threads+1):
        t = threading.Thread(target=worker,args=(i,))
        threads.append(t)
        t.start()
    
    # put username and keywords into the queue:
    for item in username:
        time.sleep(0.5)     # release a task every 0.5s
        q.put(item)
        
    # block the queue until of all the tasks in the queue finished
    q.join()
    

    # stop the thread
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
    f.write('All the tasks finished\n')
    print('All the tasks finished')
    print(threads)
    f.close()