#logical operators => and,or,not 
#bitwise operators => &(if both are 1 then 1 else 0),|(if any 1 then 1 else 0),^(same ithey 0 else 1),<<,>>,~

print(12&22)#4(if both are 1 then 1 else 0)
print(12|22)#30(if any 1 then 1 else 0)
print(12^22)#26(is same then 0 else 1)

#leftshift bitwise
print(9<<1)#18
print(9<<2)#36(it doubles)

#right shift bitwise
print(9>>1)#4
print(12>>1)#6

#NOt operator
print(~5)#-6
print(~10)#-11



num1=10
num2=10
print(id(num1))
print(id(num2))#to print the "id" if both the values are same then their id also same



#identity operators => it tells us if 2 varibles are refering to the same values are not(is,is not)
num1=12
num2=23
print(num1 is num2)#it gives false because num1 and num2 is not same
print(num1 is not num2)#it gives true because num1 and num2 is not same


#control statements => to control the flow of code 
#1.condition statements(based on condition) =>if,else,if else,elif
#2.loops(to repeat the same code) => for ,while
#3.jumping statements(to jump 1 statement to another statement easily) => continue,pass,break