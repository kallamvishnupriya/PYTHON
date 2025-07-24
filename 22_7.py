# loops
# advantages of loops => code readability
# for => when we know how may time we want to loop

for i in range(0,11):
    print(i,"hello")
    print("good morning")
print("hi")#this in out of block so it print only one time


#example to print n natural numbers
n=int(input("enter a number"))
for i in range(n):
    print(i)


#example to print even numbers => method1
for i in range(0,11):
    if i % 2 == 0:
        print(i)
    #print(i)

#example to print even numbers => method2
n=int(input("enter a number:"))
for i in range(0,n,2):
        print(i)



#while loop => when we dont know how many times it loops
i=5
while i>3:
    print("hello")
    i = i - 1
print("hi")

#example
n=True
while n:
    print("gud mrng")
    n=False


#example method 1
n=9
while n<10:
    if n==0:
        break
    print(n)
    n-=1


#method 2
n=9
while n<10 and n>=0:
    print(n)
    n-=1


#table using while loop
n=1
while n<=10:
    print("17 *",n,"=",17*n)
    n+=1
    

