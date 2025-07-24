#find if 3 numbers are equal
n=int(input("enter number1:"))
m=int(input("enter number1:"))
o=int(input("enter number1:"))
if n==m==o:
    print("those 3 numbers are euqal")
else:
    print("not equal")


# Print pass/fail based on minimum marks.
n=int(input("enter marks:"))
min_marks=35
if n>min_marks:
    print("pass")
else:
    print("fail")


#Print which digit is larger in a two-digit number.
n=input("enter 2 digit number:")
if n[0]<n[1]:
    print("2nd digit is greater",n[1])
elif n[0]>n[1]:
    print("1st digit is larger",n[0])
else:
    print("both are same")



#Check if number is divisible by 9 but not 6.
n=int(input("enter number:"))
if n%9==0 and n%6!=0:
    print("divisible by 9 but not 6")
else:
    print("doesnt divisble by both")


# Identify if input is integer or float (using input check).
n=input("enter anything")
if '.' in n:
    print("float")
else:
    print("integer")


#Print day of week from number (1–7).
n=int(input("enter a number between 1-7"))
if n==1:
    print("monday")
if n==2:
    print("tuesday")
if n==3:
    print("wednesday")
if n==4:
    print("thureday")
if n==5:
    print("friday")
if n==6:
    print("saturday")
if n==7:
    print("sunday")


#Check if number is divisible by 4 or ends with 0.
n =input("enter a number")
if int(n)%4==0 or n[-1]=='0':
    print("yes")
else:
    print("no")


#Check if a triangle is valid (3 sides).
a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalied")



