# 5. Take 2 numbers as input and print the largest number.

number_1 = float(input("Enter a number : "))
number_2 = float(input("Enter a number : "))

if(number_1 > number_2):
    print(f"{number_1} is greater than {number_2}.")
else:
    print(f"{number_2} is greater than {number_1}.")
    
# Here we didn't specify a condition when numbers will be equal...