 # use def then function name() : ->tells that you are done with the function name

 #function Declartion 
def GreetMe():
    print("Hello")

# function calling: 
GreetMe()
#Hello

def GreetMe(name):
    print(name+" Hello")

GreetMe("Shrey")
# Shrey Hello

# function that adds two integers
def add(a,b):
    print(a+b)

add(2,3) # 5
print(" ")

def sum(a,b,c):
    return a+b+c
print(sum(2,3,5)) # 10