# here file is an object where we are storing our open file object
from cgi import test
from os import read




#file = open('test.txt')



# file.close()

# with this step you don't need to write file.close() it will automatically open the file and then close it
# if you are openning the file in read mode you can give open(test.txt,'r')
# if you are openning the file in write mode you can give open(test.txt,'w')

# read the file and store all the lines in list
# reverse the list and write it back to the test file
with open('test.txt' , 'r') as reader:
     val=reader.readlines() # [abcksks, b, c, d, e]
     reversed(val) # [e, d, c, b, abcksks]
     with open('test.txt' , 'w') as writer:
         for line in reversed(val):
             writer.write(line)

with open('test.txt','w') as reader:
    reader.write("Shreyasi")
L= ["1\n","dhjkfhdkf\n","39398\n"]




# Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises the I/O error. This is also the default mode in which a file is opened.
# Read and Write (‘r+’): Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exist.
# Write Only (‘w’) : Open the file for writing. For the existing files, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exist.
# Write and Read (‘w+’) : Open the file for reading and writing. For an existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
# Append Only (‘a’): Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
# Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

