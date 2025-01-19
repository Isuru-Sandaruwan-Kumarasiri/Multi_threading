
                                      


#https://picsum.photos/id/237/200/300

import requests
import time
import multi_processing
##from queue import Queue ## for multi threading
## in multi threading we use queue.Queue because it is thread safe and used one memory space for all threads.
##if we use queue from multiprocessing then it will create separate memory space for each thread and they can't communicate with each other.


## so we want socket communication between sperate memory spaces then we use multiprocessing.Queue or any other data structure from multiprocessing module.
## as the solution is to use multiprocessing.Queue for multi processing and queue.Queue for multi threading.
from multiprocessing import Queue ## for multi processing

## Note:this Queue has a same functionality as queue.Queue but it is used for multi processing.
## It works as pipe between different processes.

##******multi processing.manager is give any other data structure like list,dict etc. which can be shared between different processes.

def get_image_urls(count):

    if count<=0:
       print('Count should be greater than 0')
       return

    for i in range(count):
      url=f'https://picsum.photos/id/{i}/200/300'
      yield url ## creates a generator object

## block of madking process of downloading images is run in main thread.

if __name__=='__main__':

    start=time.time_ns()

        
    urls=list(get_image_urls(100))

    urls_list=[]
    num_threads=10



    for i in range(0,len(urls),num_threads):
        l=urls[i:i+num_threads]
        urls_list.append(l)

        threads=[]
        results=Queue()

    for i in range(0,num_threads):
        thread=multi_processing.ImageDownloader(i,f'Thread-{i}',urls_list[i],results)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join() ## waits for the thread to finish


    total=0
    while not results.empty():
        total+=results.get()

    
    diff=time.time_ns()-start

    print('Time taken to download 100 images: ',diff/1e9,' seconds')
    print('Total images downloaded: ',total)

                                    #IMPORTANT

    ##In  Multi thread process program,one memory space is shared between threads and the threads can communicate with each other.
    ## it differs from multi processing where each process has its own memory space and they can't communicate with each other. 