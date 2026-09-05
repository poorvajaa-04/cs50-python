'''
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how 
old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any 
and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight 
(i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, 
assume that it's actually midnight, on the same date. Use datetime.date.today to get today's date, per 
docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:
from datetime import date
def main():
    ...
...
if __name__ == "__main__":
    main()

You're welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input 
a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.
Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your
implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your 
tests with: pytest test_seasons.py

'''
from datetime import date
import inflect
import sys


def get_total_minutes(birth_date, today):
    return (today - birth_date).days * 24 * 60


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")

    total_minutes = get_total_minutes(birth_date, date.today())
    p = inflect.engine()
    print(
        f"{p.number_to_words(total_minutes, andword='').capitalize()} {p.plural('minute', total_minutes)}"
    )


if __name__ == "__main__":
    main()