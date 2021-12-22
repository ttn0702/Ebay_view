import io
class File_Interact():
    def __init__(self,file_name):
        self.file_name =file_name
    
    def read_file_list(seft):
        f = io.open(seft.file_name, 'r',encoding = 'utf-8')
        ndung=f.read()
        f.close()
        return ndung.split('\n')