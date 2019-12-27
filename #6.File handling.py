#Part 6 File handling

#1. Write Python code to open a file named demo.txt and write some random data into it
#2. Open the file, read the contents and display them as output.
#3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.

file = open('#6text.txt','w')
file.write("hi....")
file.close()

file = open('#6text.txt','a')
file.write(" this file is appended")
file.close()

file = open('#6text.txt','r')
content = file.read()
print(content)
file.close()
