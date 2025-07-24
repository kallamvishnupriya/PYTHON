#Append an element to the list. (adding to the last value)
list1=[1,2,3,4,5]
list1.append(3)
print(list1)

#Remove an element by value.
list1=[1,2,3,4,5]
list1.remove(3)
print(list1)


#Loop through a list and print each item.
list1=[1,2,3,4,5]
for i in list1:
    print(i)


#Sort a list in ascending order.
list1=[1,2,6,4,5]
list1.sort()
print(list1)


#sort list in decending order
list1=[1,2,6,4,5]
list1.sort( reverse=True)
print(list1)


#Reverse a list using reverse().
list1=[1,2,3,4,5]
list1.reverse()
print(list1)


#Count occurrences of a number.
list1=[1,2,3,4,4,4,4,4]
count=list1.count(4)
print(count)


#find the index of numbers
list1=[1,2,3,4,5,6,7,8]
index=list1.index(2)
print(index)



#Concatenate two lists.
list1=[1,2,3,4,5]
list2=[4,5,3,2,1]
concat=list1+list2
print(concat)


#repeat the list 3 times
list1=[1,2,3,4,5]
repeat=list1*3
print(repeat)


#Print every second element.
list1=[1,2,3,4,5]
second=list1[::2]
print(second)


#Check if all elements are positive.
list1=[1,2,-3,4,5]
for i in list1:
   if i >0:
    print("all elements are positive")
   else:
    print("not")


#Convert list to a string with commas.
list1=[1,2,3,4,5]
string=str(list1)
print(string)



#Find the max element.
list1=[1,2,3,4,5]
max=max(list1)
print(max)


#without max
list1=[1,2,3,4,5]
max=list1[0]
for i in list1:
    if i>max:
      max=i
print(i)


#Sum all numbers in a list.
list1=[1,2,34,5,5,6,6]
sum=0
for i in list1:
    sum=sum+i
print(sum)