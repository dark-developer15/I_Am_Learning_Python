# 3. Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

principal = float(input("Enter the principal : "))
time = float(input("Enter time(in months) : "))
rate = float(input("Enter the rate of interest : "))
simple_interest = (principal * (time/12) * rate) / 100
print(f"Interest for {int(time)//12} years and {int(time)%12} months is {simple_interest}.")