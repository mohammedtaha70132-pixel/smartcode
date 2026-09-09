 #1.Check if a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.") 

    #2.Check if a year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

    #3.Find the largest of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest number:", num1)
elif num2 > num1:
    print("Largest number:", num2)
else:
    print("Both numbers are equal.")

    #4.Find the largest of three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("Largest number:", num1)
elif num2 > num1:
    print("Largest number:", num2)
else:
    print("Both numbers are equal.") 

    #5.Check if a character is a vowel or consonant

char = input("Enter a character: ").lower()

if char in "aeiou":
    print("Vowel")
else:
    print("Consonant") 

    #6.21 Ticket Pricing : Calculate ticket price based on the customer's age.

age = int(input("enter age : "))
if age<5:
    print("ticket price = 5Rs ")
elif age > 5 and age<20 :
    print("ticket price = 10Rs")
else :
    print("ticekt price = 15Rs") 

    #7time reading

time = int(input("enter time :"))

if 5< time > 12:
    print("morning")
elif 12< time > 16 :
    print("afternoon")
elif 17 < time > 20 :
    print("evening")
else:
    print("night") 

     
