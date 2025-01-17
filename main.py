#https://picsum.photos/id/237/200/300




import requests
import time

def get_image_urls(count):

    if count<=0:
       print('Count should be greater than 0')
       return

    for i in range(count):
      url=f'https://picsum.photos/id/{i}/200/300'
      yield url ## creates a generator object

start=time.time_ns()

    
urls=get_image_urls(10)

for i,url in enumerate(urls):
    res = requests.get(url, stream = True)


    if res.status_code == 200:
        res.raw.decode_content = True # Content Decompression
        file_name = f'image_downloader/Images/{i}.jpg'
        with open(file_name,'wb') as f:
            f.write(res.content)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

diff=time.time_ns()-start

print('Time taken to download 100 images: ',diff/1e9,' seconds')