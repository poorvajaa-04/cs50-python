'''
QUESTION:

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( 
was a sad face. In a file called faces.py, implement a function called convert that accepts a str as 
input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be 
returned unchanged. Then, in that same file, implement a function called main that prompts the user 
for input, calls convert on that input, and prints the result. You’re welcome, but not required, to
prompt the user explicitly, as by passing a str of your own as an argument to input. 

'''

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

def main():
    text = input("Enter a text: ")
    converted = convert(text)
    print(converted)

main()