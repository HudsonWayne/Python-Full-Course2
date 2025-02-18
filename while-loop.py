# while-loop = execute some code while some conditions remains true


# age = int(input("Enter your age:"))

# while age < 0:
#     print("Age cant be negative")
# age = int(input("Enter your age:"))

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print (f"you like{food}")
#     food = input("Enter a food you like (q to quit): ")


num = int( input("Enter the number between 1 -10:"))

while num <1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter number between 1 - 10:"))
    
print(f"your number is {num}")