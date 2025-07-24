#datatypes
# data is a collection of informantion
#numeric datatypes -> integer,float,complex,complex numbers(m + nj),boolean
#sequence datatypes -> list,tuple,range,string
#list -> n=[1,4,-5,'hello'] in this list we can have any type of datatypes togeather it is a hetrogenics collection of data. lits is mutable datatype
#tuple -> tuple is same as list but in tuple we cant change it is  not allowed to chnage and tuple is immutable datatype but we can reassign the tuple. n=(12,2345,77,3)
#string -> it basically sequence of characters in this we are having an indexing and slicing.this 2 methods are also used in list nad tuple as well.string is immutable,and we can reassign strings
    #item assignment are not allowed in string but reassignment is allowed .we can change total string but not assign the single character
# range -> it is mainly used to generate values r1=range(1,10) it will generate the sequence values between 1-10.r1=range(1,10,2),jump 2 numbers
# dictionary datatype -> key value pairs .in this keys should not repeate but values can repeate,after 3.7 version dict is ordered
   # eg of dict -> (dict={ 1:'vishnu',2:'priya',3:'kallam'})if we give same key another time it will update to the new value
#set datatype -> it is a "finite collection" of unique elements , it is an "unordered collection" of unique elements(unordered,unique,finite)
    # eg of set -> (set={1,2,34,25,6,4,})   ,it will not allow duplicates,we cant do indexing because it is unordered
    # Frozenset -> it is the usb type of set ,we cant change the frozen setafter assignment, we can reassign but not change the particular items
#None datatype -> nothing



#numeric types -> integer,float,coplex
n=5
print(type(n))#to know the datatype of the value

n=2+3j
m=4j
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n**m)
#print(n//m)these are not executable because these are not defined in maths officially
#print(n%m)these are not executable because these are not defined in maths officially
# In complex numbers floor divison and modules is not allowed,complex numbers are in the form of 




