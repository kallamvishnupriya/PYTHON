# looping statements => for,while
# for => it will repeat task no of times length of collection
# while => 


#example
n="vishnu"
for i in n:
    print(i)

#example
list1=[10,20,35,3]
for n in list1:
    print(n)

#example
tup1=(67,423,6,2,22)
for n in tup1:
    print(n)

#example
dict1={1:"one",2:"two"}
for n in dict1.items():#here we use the method called values to print only values by default it will print only keys.to print both we use method called (items())
    print(n)

#example
set1={45,64,123,8}
for n in set1:
    print(n , end=",")#end is mainly used to get the output in series format

#example
fset1={45,64,123,8}
for n in fset1:
    print(n)


#reverse the string by using for loop and to count the items
n="vishnu"
count=0#initially declaring the variable
for i in n[::-1]:
    count += 1 #increment the count corresponding to the for loop
    print(i)
print(count)


#example 
n=30
for i in range(0,n+1,2):
    print(i)

#example to print a table and to print in reverse
n=20
for i in range(1,n+1)[::-1]:
    print(" 2 *", i , "=" , 2*i)


#example to extract the vowels from a string and count them
n="hEllo python"
count=0
for i in n:
    if i in 'aeiouAEIOU':
       count +=1
       print(i,end=",")
print("\nNumber of values:",count)

#assignment
list1=[2,3,6,3,7,2]
total=0
for i in list1:
     if i>0:       
       total += i  
       print(i)
print(total)


list1=[2,5,3,4,6,8,12,14]
for i in list1:
    if i %2==0:
        print(i)


odd_count=0
even_count=0
for j in range(0,11):
    if j%2!=0:
     count=count+1
    else:
       count1=count1+1
print("odd:",odd_count)
print("even:",even_count)

n=12322
sum=0
for m in range(5):
    sum=sum+m
print(sum)
n=123
sum=1
for i in range(1,4):
    sum=sum*i
print(sum)

