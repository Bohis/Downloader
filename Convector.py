import os

class Convector:
    def __init__(self):
        pass
    def Convert(self,fileName,newFileName):
        try:
            os.system(f'ffmpeg -i "{fileName}" "{newFileName}"')
            return "completed"
        except Exception as ex:
            return str(ex)