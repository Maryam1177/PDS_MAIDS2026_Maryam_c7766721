#opening and closing a file
File1 = open("MyFile1.txt","a")
File1.close()

#industry standard practice
with open("MyFile1.txt", "r") as f:
    data = f.read()
    print(data)

 # Program to show various ways to read and
# write data in a file.
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access mode


file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()
