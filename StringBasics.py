from posixpath import split


str = "Shreyasi Sinha"
str1 = "My name is"
print(str[1]) # h

# print substring
print(str[0:5])

# concatenate two strings with keyword 'concatenate'
str2=str1+" "+str
print (str2) # My name is Shreyasi Sinha

# in -> keyword used to check one string is present in other string
str3  = "Shreyasi"
print(str3 in str) # True

# split the string based upon any character
str4="shreyasi22knp@gmail.com"
var=str4.split("@")
print(var) # ['shreyasi22knp', 'gmail.com']
print(var[0]) # shreyasi22knp

# strip : it is a method to trim space in the beggining and end
str5= "great "
print(str5.strip()) # great
print(str.strip())

# lstrip()-> removes starting white spaces
# rstrip() -> removes ending white spaces