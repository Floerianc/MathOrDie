import os
import sys
import random
import subprocess


def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])

install()
operator_list = [
    '+',
    '-',
    '*',
    '/',
]
def randomize():
    global number1 
    global number2 
    global number3
    global operator1
    global operator2
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    number3 = random.randint(1,100)
    operator1 = random.choice(operator_list)
    operator2 = random.choice(operator_list)


def ask():
    print("Was ist die Loesung fuer -> ", number1, operator1, number2, operator2, number3,)
    solution = eval(f"{number1}{operator1}{number2}{operator2}{number3}")
    solution = str(round(solution, 2))
    x = eval(input("Deine Antwort > "))
    x = str(round(x, 2))
    if x == solution:
        print("correct! You survived... for now.")
        randomize()
        ask()
    else:
        print("You will die now!")
        os.system('shutdown /s /t 20 /c "Du hast in Mathe verkackt. lol"')
        pass

randomize()
ask()