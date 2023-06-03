from fastapi import UploadFile,Request
import datetime

#convert filename
def name_files_products(images:list[UploadFile]) -> list[str]:
    names_files = []
    for i in images:
        i.filename = f'{datetime.datetime.now().timestamp()}.{i.filename.split(".")[-1]}'  
        names_files.append(i.filename)  
    return names_files    

#create file image
def create_files(images:list[UploadFile],name_file) -> None:
    for i,image in enumerate(images):
        with open(f'public/imgProducts/{str(name_file[i])}','wb') as a:
                a.write(image.file.read())
    
                
