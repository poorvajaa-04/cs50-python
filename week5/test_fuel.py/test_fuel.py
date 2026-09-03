'''
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein X is a non-negative integer and Y is a positive integer, and returns that fraction as a 
percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert 
should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.

def main():
    ...
def convert(fraction):
    ...
def gauge(percentage):
    ...
if __name__ == "__main__":
    main()

Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge 
thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_fuel.py

'''

import pytest

from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")


def test_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("1/-2")