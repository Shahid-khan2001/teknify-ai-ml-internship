#open, read and close the file
# general structure => f = open("file name", "mode")

#for reading all of the data present in a file
# f = open("demo1.txt", "r")
# data = f.read()
# print(data)

#reading data line by line
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

#for appending the data at the end of text file and to remove all of the text and new
#we have to replace 'a' with 'w'
# f = open("demo1.txt", "a")
# f.write("\nMy long term goals are to start real state business in uae")
# f.close()

#if we want to create a file and than write in it
# f=open("sample.txt", "a")
# f.write("this is a new file")
# f.close()

#with syntax
# with open("sample.txt", "r") as f:
#     data=f.read()
#     print(data)

#this is for write mode
# with open("sample.txt","w") as f:
#     f.write("new data")

import os
os.remove("sample.txt")