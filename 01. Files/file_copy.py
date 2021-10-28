import shutil

# copy file, must create folder2 first
shutil.copy("folder1/hello.txt", "folder2")

# recursively copy an entire directory
# error if the destination folder already exist
#shutil.copytree("folder2", "folder2_backup")

# move file, must create folder first
#shutil.move("folder2/hello.txt","folder2/anotherfolder")

# move and rename file
#shutil.move("folder2/anotherfolder/hello.txt","folder2/anotherfolder/newhello.txt")
