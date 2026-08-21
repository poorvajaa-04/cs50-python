'''

In Massachusetts, home to Harvard University, it's possible to request a vanity license plate for your car, with your choice of letters and 
numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
AAA22A would not be acceptable. The first number used cannot be a '0'.”
“No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid 
if it does not. Assume that any letters in the user's input will be uppercase. Structure your program per the below, wherein is_valid returns 
True if s meets all requirements and False if it does not. Assume that s will be a str. You're welcome to implement additional functions for 
is_valid to call (e.g., one function per requirement).

'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Must be 2–6 characters
    if not 2 <= len(s) <= 6:
        return False

    # Must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Numbers must be at the end, and the first number cannot be 0
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i == 2:
                return False
            if not s[i:].isdigit():
                return False
            break

    return True


main()