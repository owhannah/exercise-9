# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers


def is_palindrome(number):
     # Convert the number to a string for easier comparison
    str_number = str(number)

    # Check if the string representation is the same when reversed
    return str_number == str_number[::-1]

# Given example:
number1 = 121
number2 = 125

# Check and the display results
print(f"original number {number1}")
if is_palindrome(number1):
    print("Yes. given number is a palindrome number")
else:
    print("No. given number is not a palindrome number")

print(f"\noriginal number {number2}")
if is_palindrome(number2):
    print("Yes. given number is a palindrome number")
else:
    print("No. given number is not a palindrome number")