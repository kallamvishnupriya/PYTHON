#to print the given number is .if the number is positive then positive ,if it is zero then zero and if it is -1 then it need to print -1 and for rest of the negitive numbers need to print negative

num1=int(input("enter number:"))
if num1>0:
    print("positive")
else:
    if num1==0:
        print("zero")
    else:
           if num1==-1:
               print("-1")
           else:
               print("negative")


#elif => is used to reduce the code lines
num2 = int(input("enter number"))
if num2>0:
     print("positive")
elif num2==0:
     print("zero")
elif num2==-1:
     print("-1")
else:
     print("negative")

#we need to write first specific condition and next generic condition     
num3 = int(input("enter number:"))
if num3 == 5:
     print("5")
elif num3 > 0:
     print("positive")
elif num3==0:
     print("zero")
elif num3==-1:
     print("-1")
else:
     print("negative")   


#another example we can do this with if else and elif also
marks=int(input("enter your marks:"))
if marks >= 90:
      print("grade a")
elif marks >= 75:
      print("grade b")
elif marks >= 60:
      print("grade c")
elif  marks >= 40:
      print("grade d")
else:
      print("fail") 



#another example:here the example is if the units is 300 the it need to be int0 3(*3)if it is >200 then into 2(*2)
units=float(input("enter units:"))
if units >300:
    print(units*3)
else:
    if units >=200 :
        print(units*2)
    else:
        if units >=100:
            print(units*1)
        else:
            print(units*0)