'''
Suppose that you'd like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these 
methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. 
If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie 
jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar's capacity, though, deposit should instead 
raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren't that many cookies in the cookie jar, though, withdraw 
should instead raise a ValueError.
capacity should return the cookie jar's capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
Structure your class per the below. You may not alter these methods' parameters, but you may add your own methods.

Either before or after you implement jar.py, additionally implement, in a file called test_jar.py, four or more functions that collectively 
test your implementation of Jar thoroughly, each of whose names should begin with test_ so that you can execute your tests with: 
pytest test_jar.py

'''

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid number.")
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 or self.cookies + n > self._capacity:
            raise ValueError("Invalid number.")
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or self.cookies - n < 0:
            raise ValueError("Invalid number.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies