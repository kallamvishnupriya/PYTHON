#print factors of numbers
n=int(input("enter the number"))
for i in range( 1,n+1):
    if n % i==0:
        print(i)


#print even numbers from 2 to 10 using while loop .
for i in range(2,11):
    if i%2==0:
        print(i,"even numbers")
    else:
        print(i,"odd numbers")


#sum of numbers from 1 to 5 .
sum=0
for i in range(1,6):
    sum=sum+i
print("sum:",sum)


#take a single string check the string is upper case or not if it is upper print upper else lower case .
n='V'
if 'A'<=n<='Z':
    print("given string is in upper case")
else:
    print("lower case")



#take a single char check that string upper or not if it is upper convert to lower else print it is already lower case
n=input("enter a charcater:")
for i in n:
   if 'A'<=n<='Z':
      res=chr(ord(i)+32)
      print(res)
   else:
      print("already in lower case")
