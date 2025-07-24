#assignment => for loop with list set dict tuple
n=[1,3,63,62]
for i in str(n[2]):
    print(i)


#example to check the upper case or lower case
#ascii vakues => ord(),chr()
#ord()
print(ord('A'))#if we give the character it gives ASCII value
#chr()
print(chr(57))#here if we give the ASCII value it will gives it character



#example to print weather the character is uppercase or lowercase
n='visHnu'
for i in n:
   if 'A'<=i<='Z':
      print(i,"uppercase")
   else:
      print(i,"lowercase")



#example to conver upper to lower
n='A'
if 'A'<=n<='Z':
   convert =n.lower()
   print(convert)
else:
   print("lower")


#other way
n=input("enter a charcater:")
for i in n:
   if 'A'<=n<='Z':
      res=chr(ord(i)+32)
      print(res)
   else:
      print("already in lower case")


#to print even numbers in list and count how many odd numbers and how many even numbers
list1=[2,3,4,5,6,7,8]
odd_count=0
even_count=0
for i in list1:
    if i %2==0:#(for odd another logic is i%2==1)
      even_count+=1
      print(i,"even number")
    else:
       odd_count+=1
       print(i,"odd number")
print(odd_count,"odd count")
print(even_count,"even count")