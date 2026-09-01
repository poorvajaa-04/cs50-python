'''

In a file called professor.py, implement a program that:

Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. 
No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one 
math question at a time (e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt 
the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, 
the program should output the correct answer.
The program should ultimately output the user's score: the number of correct answers out of 10.


'''

import random

def main():

    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        ans = str(x+y)
        res = 0

        for i in range(4):
            if i == 3:
                print(x, '+', y, '=', ans)
                break

            print(x, '+', y, '=', end=' ')
            res = input()
            if res!=ans:
                print('EEE')
            else:
                score+=1
                break

    print('Score: ', score)

def get_level():
    while True:
        try:
            level = input('Level: ')
            if level.isnumeric():
                level = int(level)
            else:
                raise Exception
            if 0 < level and level < 4:
                return level
            else:
                raise Exception
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()