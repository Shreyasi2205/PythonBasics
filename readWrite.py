# we can read and write in the text file

# 1. open the text  file
file= open('test.txt')  # pass the path of the text file
# now this file has information about this text file
# make sure to close the text file

# read the contents of file using read method
#print(file.read()) #a
# b
# c
# d
# e
# now we have to read the first two characters contents of the file
#print(file.read(2))
# read one single line
#print(file.readline()) # it will read whatever is written in the first line



# print line by line using readline
line = file.readline()
while line!="":
    print(line)
    line=file.readline()

# readlines() will create a list and at 0th index first line will get stored, 1st index second line will get stored.....
for line in file.readline():
    print(line)
file.close()