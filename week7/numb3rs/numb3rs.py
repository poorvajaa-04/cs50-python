'''
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False,
respectively, if that input is a valid IPv4 address or not.
Structure numb3rs.py as follows, wherein you're welcome to modify main and/or implement other functions as you see fit, but you may not import 
any other libraries. You're welcome, but not required, to use re and/or sys.

import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    ...
...
if __name__ == "__main__":
    main()

Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions 
that collectively test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your 
tests with: pytest test_numb3rs.py

'''
import re


def validate(ip):
    if not re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", ip):
        return False

    return all(0 <= int(part) <= 255 and not (len(part) > 1 and part[0] == "0")
               for part in ip.split("."))


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()