n=int(input("enter a busticket number:"))
n1=str(n)
n2=n1[::-1]
n3=int(n2)
if n3==n:
    print("lucky ticket")
else:
    print("not lucky ")



# Palindromic Bus Ticket with length check
n = input("Enter a bus ticket number: ")

if len(n) < 1 or len(n) > 10:
    print("Invalid ticket number length")
else:
    
    num = int(n)
    original = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    if reverse_num == original:
        print("Lucky Ticket")
    else:
        print("Not Lucky")





n=int(input("enter a number:"))
square=0
sum=0
for i in range(1,n+1):
    square=i**2
    sum=sum+square
print(sum)




secret_number = 42
while True:
    guess = int(input("enter a value:")) 
    if guess == secret_number:
        print("Treasure Found!")
        break
    else:
        print("Try Again!")




n=100
square=0
for i in range(1,n+1):
    square=i**2
    if square <= n:
        print(square)
    else:
        break
        



n = 100
for i in range(1, n + 1):
    cube = i ** 3
    if cube <= n:
        print(cube)
    else:
        break
