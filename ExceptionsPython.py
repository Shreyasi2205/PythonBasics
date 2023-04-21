

# lets say cart can only have 2 items, otherwise it will raise an expception

itemCart=0
# 2 items will be added to cart
# if itemCart!=2:
#     raise Exception("Products cart count not matching")

# if you give keyword pass  the above if keyword or function does nothing

if itemCart==2:
    pass
# assert is a methode in python that always expects a condition and that condtion should
# return true

#assert(itemCart==2) # assert(itemCart==2)
# AssertionError

# try catch mechanism
# try block -> when exception fails in try block test goes to catch block, it will raise an
# exception and send it to the catch block
# catch block will tell what is the exception

try:
    with open('file.log', 'r') as reader:
        reader.read()
except:
    print("somehow I reached this block") #somehow I reached this block

try:
    with open('test.txt', 'r') as reader:
        print(reader.read())
        #ed
# c
# b
# abcksks
except:
    print("somehow I reached this block")

# to check the atcual error that python got

try:
    with open('files.log','r') as reader:
        reader.read()
except Exception as e:
    print(e) #[Errno 2] No such file or directory: 'files.log'

# another method is finally which is used with try and expect and it will execute no matter what
finally: 
    print("djfjd")  #djfjd