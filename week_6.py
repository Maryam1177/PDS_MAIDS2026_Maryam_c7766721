File_object = open("MyFile1.txt","r")
print(File_object.read())
File_object.close()

File_object = open("MyFile1.txt","a")
File_object.write("Today \n")
File_object.close()


File_object = open("MyFile1.txt","r")
print(File_object.read())
File_object.close()