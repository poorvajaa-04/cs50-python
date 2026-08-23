'''

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d 
(which is a common way of ending one's input to a program). Then output the user's grocery list in all uppercase, sorted alphabetically by 
item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user's input 
case-insensitively.


'''

items = {}

while True:
    try:
        item = input().upper()

        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        break

for item in sorted(items):
    print(items[item], item)