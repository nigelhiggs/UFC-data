import os

for file in os.listdir('C:/Users/Me/Desktop/test'):
    if file.endswith('.jpg'):
        
        os.remove("C:/Users/Me/Desktop/test/"+file)
