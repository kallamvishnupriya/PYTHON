print(list(range(0,100,15)))# to print all common multiples of 3 and 5 (using through 15)


#set => collection of unoredred finite unique elements
set1={ 4,5,'str1',9.5,(1,2,5)}#set itself an mutable datatype and set elements are need to me immutable
print(set1)
# to change the list in set first list need to be chnages in set and then again convert it into list
list1=[1,1,2,2,3,4,4,]
print(list(set(list1)))


#frozen set => frozen set is immutable
fset1=frozenset([1,2,1,3,4,5,3,2,4])
print(fset1)