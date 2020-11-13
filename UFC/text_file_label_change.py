import os
import glob

def listToString(s):  
    
    # initialize an empty string 
    str1 = "" 
    
    # return string   
    return (str1.join(s))




#folder which you would like to extract.
path = "C:/Users/Me/Desktop/test/"

#holds the text file during loop phase.
#hold = ""

temp_array = []

#enter the directory based on path
for x in os.listdir(path):
    #condition finds only txt files.
    if x.endswith(".txt"):
        
        #open and read
        with open(path+x, 'r') as reader:

            #load into a var the text file.    
            hold = reader.read()
            hold = hold.splitlines()
            #reader.close()
            print(hold)
            
        for y in range(len(hold)):
            
            check = list(hold[y])
            #im lazy, this is to remove the 15 from my label in txt file. 
            check.pop(0)
            check.pop(0)

            print(check)

            #insert the change i want.
            check.insert(0, '0')
            #convert back to string
            result = listToString(check)
            
            temp_array.append(result)

        #very hacky, running this just to clear the text file for the next step.
        with open(path+x, "w") as file1:
            file1.write("")
            file1.close()
            
##        #now its time to write my array to the text file.
        with open(path+x, 'w') as filehandle:
            for listitem in temp_array:
                filehandle.write('%s\n' % listitem)

        temp_array = []






























