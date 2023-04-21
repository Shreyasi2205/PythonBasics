# if else condition in python
greeting="Good Morning"
if greeting=="Morning":
    print("Condition Matches")
else:
    print("Condtion do not match")
print("if else code is completed")
#Condtion does not match
greeting="Good Morning"
if greeting=="Good Morning":
    print("Condition Matches")
else:
    print("Condtion do not match") 
#Condition Matches
print("if else code is completed") 

# for loop
obj=[2,3,5,7,9]
for i in obj: 
    print(i)
# 2
# 3
# 5
# 7
# 9
# print the list with multiples of 2
for i in obj:
    print(i*2)
# 4
# 6
# 10
# 14
# 18

#sum of first natural numbers
# for(i=1;i<=5;i++)
sum=0
for j in range(1,6): # range(i:j) it will iterate from i to j-1
    sum+=j
print(sum)  #15
print(" ")
# now for i in range(1,6) it will start from 1 and go till 5 by incrementing +1 
#now what if it has to increment +2???
# you can give it as third argument
for k in range(1,11,2):
    print(k)
# 1
# 3
# 5
# 7
# 9
print(" ")
for k in range(1,11,5):
    print(k)
# 1
# 6

for k in range(10): # it will treat starting index as 0 and it will go till 9
    print(k)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
print(" ")
# print no. in reverse from 10 to 0
for i in reversed(range(11)):
    print(i)
print(" ")
for i in range(10,-1,-1):
    print(i)
print(" ")
# # Python3 code to demonstrate
# # backward iteration
# # using slice syntax

# # Initializing number from which
# # iteration begins
N = 6


# Using slice syntax perform the backward iteration
N=10
k = range(N+1)[::-1]
print("The reversed numbers are : ",end='')
for i in k:
	print(i, end=' ')
