import youtube_dl
import os

class Loader:
    listQual = ["best","worst","bestvideo","worstvideo","bestaudio","worstaudio"]
    
    def __init__(self):
        pass
    
    def Load(self,url,location,fileName,option):
        try:
            os.system(f'youtube-dl -o "{location}/{fileName}.mkv" {url} -f {option}')
            return "completed"
        except Exception as ex:
            return str(ex)