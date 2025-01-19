from threading import Thread
import requests

class ImageDownloader(Thread):

    def __init__(self,thread_id,name,urls,results):
        super(ImageDownloader,self).__init__()
        self.id=thread_id
        self.name=name
        self.urls=urls
        self.results=results
        self.success_count=0

    def run(self):
        for i,url in enumerate(self.urls):
   
            if self.download_image(url,f'{self.id}_{i}'):
                self.success_count+=1	
        self.results.put(self.success_count)


    def download_image(self,url,image_number):

        res = requests.get(url, stream = True)


        if res.status_code == 200:
            res.raw.decode_content = True # Content Decompression
            file_name = f'image_downloader/Images/{image_number}.jpg'

            with open(file_name,'wb') as f:
                f.write(res.content)
            print('Image sucessfully Downloaded: ',file_name)
            return True
            
        else:
            print('Image Couldn\'t be retrieved')
            return False

        