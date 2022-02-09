import urllib.request
import time
import os

p = os.getcwd()

projectList = {"hangman": 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/hangman.py',
               "cc": 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/Ceasar%20cipher.py',
               }

gameList = {1: p + '\\python project\\hangman.py',
            2: p + '\\python project\\cc.py',
            3: p + '\\python project\\rps.py',
            4: p + '\\python project\\snake.py',
            5: p + '\\python project\\wordle.py',
            }

while not os.path.exists(p + '\\python project\\cc.py'):
    try:
        for key, value in projectList.items():
            path = p + "/python project/" + key + ".py"
            while not os.path.exists(path):
                urllib.request.urlretrieve(value, path)
                print("Sucess")
    except:
        print("Failed")
        time.sleep(2)


def pick():
    for index, key in enumerate(projectList.keys()):
        print(index+1, key)
    print("Enter the number of the game you want to play: ")
    x = int(input())
    exec(open(gameList.get(x)).read())


pick()
