# 4. Take in input of two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

number_1 = float(input("Enter a Number : "))
number_2 = float(input("Enter a Number : "))
operator = input("Enter an operator(+, -, *, /) : ")

if(operator=="+"):
    print(f"Addition of {number_1} and {number_2} is {number_1+number_2}")
elif(operator=="-"):
    print(f"Subtraction of {number_1} from {number_2} is {number_1-number_2}")
elif(operator=="*"):
    print(f"Multiplication of {number_1} and {number_2} is {number_1*number_2}")
elif(operator=="/"):
    print(f"Division of {number_1} from {number_2} is {number_1/number_2}")
else:
    print("Wrong Input...")

# We are not considering edge cases and wrong inputs that can give error. For Eg. input "hello" for first input and we will get an error.
# We will be able to manage errors after learning Exceptional handling in Python...

