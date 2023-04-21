# datatypes in python
b, c, d = 5, 6.4, "Great"
#print("value of b is" + b) #throws an error
"{} {}".format("value of b is",b) # {} {}-> infroming that I am going to get two values 
# format -> method that will give the values
print("{}{}".format("value of b is ",b)) #value of b is 5

#get the data type
print(type(b)) #<class 'int'>
print(type(d)) #<class 'str'>

# List datatypes and their operations to manipulate
# pyhton list can have multiple datatypes with it
values = [1,2,"Shreyasi",4,5]
print(values) #[1, 2, 'Shreyasi', 4, 5]
print(values[2]) #Shreyasi (it will print the element at index 2)
print(values[-1]) # 5 (it will print the element at the last index)
# so if you want the elements at the first index and the 3rd index
print(values[1:4]) # [2, 'Shreyasi', 4] (: will capture only from 1st till 3rd because last index is -1)
# insert "Sinha" after Shreyasi
#print(values.insert(3,"Sinha")) # None
values.insert(3,"Sinha")
print(values) #[1, 2, 'Shreyasi', 'Sinha', 4, 5]
# if you want to add values at the end use append
values.append("end")
print(values) #[1, 2, 'Shreyasi', 'Sinha', 4, 5, 'end']
# delete any value
del values[1]
print(values) #[1, 'Shreyasi', 'Sinha', 4, 5, 'end']
values[1]=2
print(values) #[1, 2, 'Sinha', 4, 5, 'end']

# Tupple -> same as list but are immutable i.e they can not be updates
val=(1,2,3,"hello")

#val[2]="fhf" #TypeError: 'tuple' object does not support item assignment

# Dictionary->  gives key value pair
dic={"a":2, 1:"abc", 4:5} # it is not based upon index but key
print(dic["a"]) # 2

# how to create dictionary at run time
dict= {}
dict["firstname"]="Shreyasi"
dict["lastname"]="Sinha"
print(dict) #{'firstname': 'Shreyasi', 'lastname': 'Sinha'}

txt="//input[contains(@id, 'col1') and contains(@id, 'field-card-type-0') and contains(@id, 'subform-field-image-entity') and not(contains(@id, 'target')) and contains(@id, 'edit-field-body-0')]"
txt=txt.replace("col1","col2")
txt=txt.replace("edit-field-body-0","edit-field-body-2")
print(txt)