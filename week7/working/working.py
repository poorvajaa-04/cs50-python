'''
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats below and returns the 
corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there 
will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, 
etc.). But do not assume that someone's hours will start ante meridiem and end post meridiem; someone might work late and even long hours 
(e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you're welcome to modify main and/or implement other functions as you see fit, but you may not import 
any other libraries. You're welcome, but not required, to use re and/or sys.

'''

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.match(
        r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s
    ):
        st_hour, st_min, st_ap, ed_hour, ed_min, ed_ap = match.groups()

        if st_min is None and ed_min is None:
            st_min, ed_min = 0, 0
        st_hour, st_min, ed_hour, ed_min = map(int, [st_hour, st_min, ed_hour, ed_min])

        if st_ap == "PM" and st_hour != 12:
            st_hour += 12
        elif st_ap == "AM" and st_hour == 12:
            st_hour = 0

        if ed_ap == "PM" and ed_hour != 12:
            ed_hour += 12
        elif ed_ap == "AM" and ed_hour == 12:
            ed_hour = 0

        if (
            not 0 <= st_hour <= 23
            or not 0 <= st_min <= 59
            or not 0 <= ed_hour <= 23
            or not 0 <= ed_min <= 59
        ):
            raise ValueError("Invalid arguments")

        return f"{st_hour:02d}:{st_min:02d} to {ed_hour:02d}:{ed_min:02d}"
    raise ValueError("Invalid arguments")

if __name__ == "__main__":
    main()