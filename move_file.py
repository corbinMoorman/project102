import os
import shutil


from_dir = "C:/Users/spitc/Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)



for i in from_dir:
    name, extension = os.path.splitext(i)
    if(extension == ""):
        continue
    if(extension in [".txt", ".doc", ".pdf", ".docx"]):
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + i
    if(os.path.exists(path2)):
        print("Moving" + name + "...")
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        shutil.move(path1, path3)
        print("Moving" + name + "...")
        
