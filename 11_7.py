# #input taking method1
# num1=int(input("enter num1:"))# we need to give the specific datatype otherwise it store default as string
# num2=int(input("enter num2:"))
# print(num1+num2)

# #method2
# num1=input("enter num1:")
# num2=input("enter num2:")
# print(int(num1)+int(num2))
# print(type(num1))
# print(type(num2))
# num1=int(num1)
# print(int(num1)-int(num2))
# print(int(num1)*int(num2))

# #example
# num1=float(input("enter num1:"))
# num2=float(input("enter num2:"))
# print(num1*num2)
# print(num1//num2)
# print(num1**num2)

# #datatype conversion
# num1=4.5
# print(int(num1),num1)

# num1=5
# num1=int(num1)#5
# num1=float(num1)#5.0
# print(num1)

# num1=0+0j
# num1=str(num1)
# print(num1)
# #truthy value - when boolean gives you true value
# #falsy value - when boolean gives you flase value

# num1="vishnu"#except empty string all strings gives true
# num1=bool(num1)
# print(num1)

#operations => the symbol used in middle of the 2 operands like(+,-)
#operands => the numbers or letters that can perform operations
#arthimetic operations => +,-,*,5,/,//,**,/
#relational operators => >,<=,>=,==,!=
#logical operators => AND,OR,NOT
#assignment operators => =,+=,-=,*=,.....
#bitwise operators => &,|,^,~,!,<<,>>
#membership => in not in
# num1=5
# num1=num1+3
# num1 += 3#both are same

#convert int into binary
num1=5
binary=bin(num1)[2:]
print(binary)