# 1. Write a program to print whether a number is even or odd, also take input from the user.

num = int(input("Enter a number : "))
if(num%2==0):
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")