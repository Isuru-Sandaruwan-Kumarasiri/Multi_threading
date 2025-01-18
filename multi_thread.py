from threading import Thread
import requests

class ImageDownloader(Thread):

    def __init__(self,thread_id,name,urls):
        super(ImageDownloader,self).__init__()
        self.id=thread_id
        self.name=name
        self.urls=urls

    def run(self):
        for i,url in enumerate(self.urls):
            self.download_image(url,f'{self.id}_{i}')


    def download_image(self,url,image_number):

        res = requests.get(url, stream = True)


        if res.status_code == 200:
            res.raw.decode_content = True # Content Decompression
            file_name = f'image_downloader/Images/{image_number}.jpg'

            with open(file_name,'wb') as f:
                f.write(res.content)
            print('Image sucessfully Downloaded: ',file_name)
            
        else:
            print('Image Couldn\'t be retrieved')

        