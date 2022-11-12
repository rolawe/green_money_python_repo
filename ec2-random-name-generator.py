# Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
import random
import string

x = 6 #Initialize size of string
n = int(input("Number of EC2 instances needed: ")) #Allow use to input how many EC2 instances

while n != 0:
    EC2_random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=x)) #generate random strings
    n -= 1
    
    print("EC2_" + EC2_random_name) #return n number of random strings
         


#Allow the user to input the name of their department that is used in the unique name
department = input("Enter Department: Marketing, Accounting, FinOps: ") #Input Department: Marketing, Accounting or FinOps

for _ in department:
    if department == "Marketing" or department.lower() == "marketing":
        print("Good to proceed")
        break
    
    elif department == "Accounting" or department.lower() == "accounting":
        print("Good to proceed")
        break

    elif department == "FinOps" or department.lower() == "finops":
        print("Good to proceed")
        break
    
    else:
        print("Error, please enter name correctly.")
        raise SystemExit
        sys.exit()


#Generate random characters and numbers that will be included in the unique name

    





