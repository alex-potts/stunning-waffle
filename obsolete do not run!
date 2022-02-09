import shutil
import os
import urllib.request
import time

if not os.path.exists('N:\\Documents\\python project'):
    directory = "python project"
    parent_dir = "N:/Documents"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

if os.path.exists('N:/Documents/mywords.txt'):
    src_path = r"N:\Documents\python project\mywords.txt"
    dst_path = r"N:\Documents\mywords.txt"
    shutil.move(dst_path, src_path)
elif not os.path.exists('N:/Documents/python project/mywords.txt') and not os.path.exists('N:/Documents/mywords.txt'):
    mywords = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/mywords.txt'
    while not os.path.exists('N:/Documents/python project/mywords.txt'):
        try:
            urllib.request.urlretrieve(mywords, 'N:/Documents/python project/mywords.txt')
            print("Success")
        except:
            print("Reiterating")
            time.sleep(2)

while not os.path.exists('N:/Documents/python project/mover.py'):
    mover = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/mover.py'
    try:
        urllib.request.urlretrieve(mover, 'N:/Documents/python project/mover.py')
        print("Succeeded")
    except:
        print("Retrying....")
        time.sleep(2)

while not os.path.exists('N:/Documents/python project/master.py'):
    master = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/master.py'
    try:
        urllib.request.urlretrieve(master, 'N:/Documents/python project/master.py')
        print("Succeeded")
    except:
        print('Not much longer.....')
        time.sleep(2)


exec(open("N:\\Documents\\python project\\mover.py").read())
exec(open("N:/Documents/python project/master.py").read())
