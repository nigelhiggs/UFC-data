#we are making a script that will allow for easy access to print loads of address
#locations to .txt files through a for loop.


file = open('C:/Users/Me/Desktop/train.txt','w+')


for x in range(1161,1324):
    file.write('/content/darknet/build/darknet/x64/data/obj/fighter'+str(x)+'.jpg'+'\n') 
    #print('/content/darknet/data/photos/fighter'+str(x)+'.jpg'+'\n')
file.close() #to change file access modes 
  

