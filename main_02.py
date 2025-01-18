
#                                         


#https://picsum.photos/id/237/200/300

import requests
import time
import multi_thread

def get_image_urls(count):

    if count<=0:
       print('Count should be greater than 0')
       return

    for i in range(count):
      url=f'https://picsum.photos/id/{i}/200/300'
      yield url ## creates a generator object

start=time.time_ns()

    
urls=list(get_image_urls(100))

urls_list=[]
num_threads=10



for i in range(0,len(urls),num_threads):
   l=urls[i:i+num_threads]
   urls_list.append(l)

threads=[]

for i in range(0,num_threads):
   thread=multi_thread.ImageDownloader(i,f'Thread-{i}',urls_list[i])
   thread.start()
   threads.append(thread)

for thread in threads:
    thread.join()




   
diff=time.time_ns()-start

print('Time taken to download 100 images: ',diff/1e9,' seconds')