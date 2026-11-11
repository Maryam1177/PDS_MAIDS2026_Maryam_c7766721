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
# \n is placed to indicate EOL (End of Line
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access mode


file1 = open("myfile.txt","r+")

print("Output of Read function is ")
print(file1.read())
print()


# seek(n) takes the file handle to the nth

# byte from the beginning.
file1.seek(0)
print( "Output of Readline function is ")
print(file1.readline())
print()


file1.seek(0)
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()


file1.seek(0)
print("Output of Readline(9) function is ")
print(file1.readline(9))




file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


# Python program to illustrate
# Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()


# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()


# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()


import pandas as pd
df = pd.read_csv('data.csv', index_col=0)
print(df)



# Write an Excel file
df.to_excel('data.xlsx')
# Read an Excel file
df = pd.read_excel('data.xlsx', index_col=0)
print(df)


# JASON  files
df = df.reset_index()
df.to_json('data-columns.json')
df.to_json('data-index.json', orient='index')
print(df)



# Explain how this would scale in real-world data systems.
#In the real world, in big companies data is much bigger,
# people cannot check big files by hands so code must read clean and save them automatically.
# and as different systems use different formats, we need to change data between CSV , Excel and JSON.



# Reflection & Discussion
# 1. In a real system all the part are connected like a chain.
# If one part has an error, and it is not handle,
#it can affect the other parts and cause a much bigger problem.
# So exception handling is really important because it stops the error
# from spreading and the rest of the system can keep working.


# 2. A full file address works only on my computer, not on other computers,
# or if the file moves , Python can not find it and gives an error.
# so using just the file name is safer.

# 3. Data from other people can be messy and wrong.
# It can have empty cells or repeated values that can affect the results we are looking for,
# so it is important to check it before using it.

# 4. Automation helps because it does exactly the same steps every time.
# So anyone who runs the code gets the same result.