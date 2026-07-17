name = input("enter your name:")
print(name)
a= int(input("enter 1 st number:"))
b= int(input("enter 2 nd number:")) 
print(a==b)

num = int(input("Enter a number: "))

if num < 2:
    print(False)
else:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    print(prime)
    