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
##ATM Withdrawal
    balance = int(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient Balance")
elif amount % 100 != 0:
    print("Amount should be multiple of 100")
else:
    print("Withdrawal Successful")
    print("Remaining Balance:", balance - amount)
   
    # BMI Calculator

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
   ## Movie Ticket Price
age = int(input("Enter age: "))

if age < 5:
    print("Free Ticket")
elif age <= 18:
    print("Ticket Price = ₹150")
elif age <= 60:
    print("Ticket Price = ₹250")
else:
    print("Ticket Price = ₹100")