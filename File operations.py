import os
print ("Checking if My_File exists")
if os.path.exists("My_File.txt"):
    print("My_File exists")
else:
    print("My_File does not exist")
    # Create the file if it does not exist
    open("Codingal Task.txt", "w").close()
    print("Codingal Task.txt has been created.")

#Spliting the words

with open ("Codingal Task.txt","r")as file:
    data = file.readlines()
    print ("Words in this file are....")
    for line in data:
        word= line.split()
        print (word)
        file.close()
#Removing the file
os.remove("Codingal Task.txt")

