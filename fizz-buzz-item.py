value = int(input("Enter an integer value: "))
if value % 5 == 0 and value % 3 == 0:    
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:    
    print(f"{value} is not a multiple of 3 or 5")