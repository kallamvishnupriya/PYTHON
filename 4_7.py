str1="python class"
str2=""
print(str1)
print(len(str1))#length
print(len(str1)-1)#toget the last value index number
print(str2)
print(len(str2))

print(str1[3])#indexing

str="em antivi em antivi........"
print(len(str)-1)# to get last element number index
print(str[0])
print(str[6])
print(str[len(str)-1])#indexing to get last character
print(str[-1])
print(str[-2])#to get easy from above method there is an negative indexing to get last but one element
print(str[-len(str)])# to get 1st character from negative indexing  

name="vishnu"
#print(name[8]) index out of range error
print(name[1:3])#this is called slicing to get the group of characters in sequence
print(name[:-1])#to get all element s from last element with negative slicing
print(name[-4:-1])# negative slicing to get elements in reverse order
print(name[2:])#to get all elements from 2nd 
print(name[1:5:2])#that last part refers to difference between elements just like jumping
print(name[-1:-5])#this will not work if we put -1 in last part then it will work
print(name[-1:-5:-1])# this is used to work with negative direction
print(name[ : ])# to print total string
print(name[ : : -1])# to print total string in reverse order
#index out of bound error will only come in indexing not in slicing in slicing we can give any big number







