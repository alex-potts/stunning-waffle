import urllib.request
import time
import os

projectList = {"hangman": 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/hangman.py',
               "cc": 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/Ceasar%20cipher.py',
               }


while not os.path.exists('N:\\Documents\\python project\\cc.py'):
    try:
        for key, value in projectList.items():
            path = "N:/Documents/python project/" + key + ".py"
            while not os.path.exists(path):
                urllib.request.urlretrieve(value, path)
                print("Sucess")

    except:
        print("Failed")
        time.sleep(2)

exec(open('N:/Documents/python project/hangman.py').read())
