# #control statements => control the flow of execution of code.
# #1.conditional statement => if,else, elif ,if else
# #2.loops(to repeat the same code) => for ,while
# #3.jumping statements(to jump 1 statement to another statement easily) => continue,pass,break


#if statement
age =21
if age >= 18:
    print("right to vote")
print("can't vote")#this will also executes because i wasnt follow the "if "indentation.


#assignment qus to find the number is even or odd using only if
num=6
if num % 2 ==0 :
    print("num is even number")
if num %2 != 0:
    print("num is odd number")


#to know weather the given number is 7 multiple or not
num1=15
if num1 % 7 == 0:
    print("num1 is a 7 multiple")
if num1 % 7 != 0:
    print("num1 is not a 7 multiple")


#to print weather if the passward character id >10 it is strong passward,else weak passward
passward=str(input("enter a passward"))
if len(passward) >= 10:
    print ("strong passward")
if len(passward) < 10:
    print("weak passward")


#if else statement
age =21
if age >= 18:
    print("right to vote")
else :
    print("can't vote")

#to peint weather is number is positive or nagaive
num2 = 3
if num2 > 0:
    print("positive number")
else:
    if num1==0:
        #to check the 0 condition also without having any elif.but this will give you a bug where if we give 0 then it will print zero and negative number also thats why we need to use elif
        print("zero")
    print("negative number")


# to print the given number is 3 dogit or not
num3=567
if num3 >= 100 and num3 <=999 :
  print("yes")
else:
  print("no")



