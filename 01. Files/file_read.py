# make sure you have a hello.txt in your current working directory
# same directory as your python script
helloFile = open("hello.txt")
content = helloFile.read()
print(content)
helloFile.close()

# make sure you have a hello.txt in the specified director 
# same directory as your python script
helloFile = open("hello.txt")

content = helloFile.readlines()
print(content)
