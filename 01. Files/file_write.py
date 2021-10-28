
helloFile = open("hello.txt", "w")
helloFile.write("This is also another line\n")
helloFile.close()

# reopen to display content
helloFile = open("hello.txt")
print(helloFile.read())
helloFile.close()
 
# open the file for adding next text
helloFile = open("hello.txt", "a")
helloFile.write("Hello world again\n")
helloFile.close()

# reopen to display content
helloFile = open("hello.txt")
print(helloFile.read())
helloFile.close()
