import os
import shutil

source = "/Users/moizmasood/Downloads"
destination = "/Users/moizmasood/Downloads/downloadedfiles"

list_of_files = os.listdir(source)


for filename in list_of_files:
    name,extension = os.path.slplittext(filename
                                        
   if extension == '':
   continue
extension in['.png,'.jpg,'.jpeg,'jfif]:
path1 = source+'/'+filename
path2 destination+'/'+"image_files"
path3 destination+'/'+"image_files"+'/'+filename

   if os.path.exists(path2):
   print("moving")
   shutil.move(path1,path3)
else
os.makedirs(path2)
shutil.move(path1,path3)

/Users/moizmasood/Downloads