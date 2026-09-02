'''

In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects 
a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each 
of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py


'''

from week5.test_twttr.twttr import shorten


def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("twitter") == "twttr"
    assert shorten("tWitTer") == "tWtTr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("1a2be") == "12b"