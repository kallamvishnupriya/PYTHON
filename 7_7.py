#sequence datatypes
#list1 => [1,2.3,5,7.0,'hello',2+3j,[5,6,7]],any type of datatypes
#to access the nested list number (list[4][1])
#print(list1[::-1])#to print reverse order
# list is mutable and we can change the value or delete it
list1=[1,3,5.6,'str1',[5,6,2,7,8],3+2j]
print(len(list1))
print(list1[4][2])
print(list1[::-1])
print(list1[7:])#gives empty string
list1[3]=5
print(list1)



#tuple => () tuple is immutable
tup1=(1,2,3,"string",5.6)
tup1=(2,2,3,"string",5.6,[4,5,6,7])# we can give list inside tuple
#item assignment is not allowerd in tuple (tup1[4]=5)
print(tup1[5][2])
#iteration is faster in tuple compared to list



#range => range(0,10)
print(range(0,10))#here numbers will not print due to print 
print(list(range(0,10,2)))#to see the numbers either use the for loop or use list datatype
print(list(range(10,0,-2)))#reverse
print(list(range(1,50,2)))#to print first 25 odd numbers
print(list(range(0,50,2)))#to print first 25 even 
print(list(range(0,50,5)))#to print 5 multiples



#dict => {key:value} ,mutable
#after python3.7 version dict is orderd
dict1={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'four'
}
print(dict1)
print(dict1[1])