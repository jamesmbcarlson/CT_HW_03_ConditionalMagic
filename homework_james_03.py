# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 2 Assignment: The Magic of Conditional Statements

### 1. Decisions at the Crossroad ###

number = int(input("Enter a number: "))     # typecast input to int

if number > 0:
    print("The number is positive.")
elif number == 0:                           # changed = to ==
    print("The number is zero.")
else:                                       # removed condition; else does not evaluate conditions
    print("The number is negative.")

print()

### 2. The Greatest Showdown ###
    
print("Now enter three numbers!")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))

largest_num = 0
smallest_num = 0
is_all_equal = False
two_equal_numbers = "none"

# evaluate if all three are equal
if num1 == num2 == num3:
    is_all_equal = True

# evaluate if num1 and num2 are equal
elif num1 == num2:
    two_equal_numbers = "Your first two numbers are the same!"
    largest_num = num1 if num1 > num3 else num3
    smallest_num = num1 if num1 < num3 else num3

# evaluate if num1 and num3 are equal
elif num1 == num3:
    two_equal_numbers = "Your first and third numbers are the same!"
    largest_num = num1 if num1 > num2 else num2
    smallest_num = num1 if num1 < num2 else num2

# evaluate if num2 and num3 are equal
elif num2 == num3:
    two_equal_numbers = "Your last two numbers are the same!"
    largest_num = num1 if num1 > num2 else num2
    smallest_num = num1 if num1 < num2 else num2

# if no numbers are equal, determine largest and smallest from all three values
else:
    largest_num = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
    smallest_num = num1 if num1 < num2 and num1 < num3 else num2 if num2 < num3 else num3

# print results
if is_all_equal:
    print("All three numbers are equal!")
elif two_equal_numbers != "none":
    print("You have two equal numbers!")
    print(two_equal_numbers)

if not is_all_equal:
    print(f"The smallest number is {str(smallest_num)}.")
    print(f"The largest number is {str(largest_num)}.")

print()

### 3. Leap Year Explorer ### 
# this blew my mind; I had no idea that some leap years are skipped!

year = int(input("Enter a year: "))
if(year % 4 == 0):
    is_leap_year = True
if(year % 100 == 0):
    is_leap_year = False
if(year % 400 == 0):
    is_leap_year = True

print(f"{year} is a leap year!") if is_leap_year else print(f"{year} is not a leap year.")