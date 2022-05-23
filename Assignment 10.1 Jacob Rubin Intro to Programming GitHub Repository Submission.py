import os
import sys
#importing necessary modules

directory = input("Please enter the name of the directory you would like to save your file to: ")
path = directory
isExist = os.path.exists(directory)
filename = input("Enter the name of the file: ")
name = input("Please enter the name of the user you would like to save: ")
address = input("Enter the address you would like to save: ")
phone_number = input("Next, enter the phone number of the user you would like to save: ")
#the above will save a file containing entered information to an entered directory 
if os.path.isdir(directory):
    writeFile = open(os.path.join(directory,filename),'w')
    writeFile.write(name+ ', ')
    writeFile.write(address+ ', ')
    writeFile.write(phone_number)
    writeFile.close()
#opens the file created to read the contents
    print("Contents of the file: ")
#prints the contents of the created file
    readFile = open(os.path.join(directory,filename), 'r')
    for line in readFile:
        print(line)
    readFile.close()
else:

    if not isExist:
   
        os.makedirs(path)
        print("The new directory is created!")
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+ ', ')
        writeFile.write(address+ ', ')
        writeFile.write(phone_number)
        writeFile.close()
#makedirs creates a new directory if the one entered doesn't exist
        print("Contents of the file: ")

        readFile = open(os.path.join(directory,filename), 'r')
        for line in readFile:
            print(line)
        readFile.close()
