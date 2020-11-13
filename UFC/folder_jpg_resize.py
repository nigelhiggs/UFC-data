import PIL
from PIL import Image
import os
import glob

basewidth = 416
hsize = 416

path = os.chdir(r"C:\Users\Me\Desktop\UFC_split\New_Datasets\Additional_ST\Standing")
file_path = "C:/Users/Me/Desktop/UFC_split/New_Datasets/Additional_ST/Standing/"

for fn in os.listdir(path):

    img = Image.open(file_path+fn)

    wpercent = (basewidth / float(img.size[0]))
    #hsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    print(wpercent,hsize,img)
    img.save(file_path+fn)
    
