import shutil
import os
import urllib.request
import time

pa = os.getcwd()


def install(p):
    if not os.path.exists(p + '\\python project'):
        directory = "python project"
        parent_dir = p
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

    if os.path.exists(p + '/mywords.txt'):
        src_path = p + "\python project\mywords.txt"
        dst_path = p + "\mywords.txt"
        shutil.move(dst_path, src_path)
    elif not os.path.exists(p + '/python project/mywords.txt') and not os.path.exists(p + '/mywords.txt'):
        mywords = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/mywords.txt'
        while not os.path.exists(p + '/python project/mywords.txt'):
            try:
                urllib.request.urlretrieve(mywords, p + '/python project/mywords.txt')
                print("Success")
            except:
                print("Reiterating")
                time.sleep(2)

    while not os.path.exists(p + '/python project/mover.py'):
        mover = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/mover.py'
        try:
            urllib.request.urlretrieve(mover, p + '/python project/mover.py')
            print("Succeeded")
        except:
            print("Retrying....")
            time.sleep(2)

    while not os.path.exists(p + '/python project/master.py'):
        master = 'https://raw.githubusercontent.com/alex-potts/stunning-waffle/main/master.py'
        try:
            urllib.request.urlretrieve(master, p + '/python project/master.py')
            print("Succeeded")
        except:
            print('Not much longer.....')
            time.sleep(2)


if os.path.exists(pa + "\\python project\\hangman.py"):
    exec(open(pa + "\\python project\\mover.py").read())
    exec(open(pa + "/python project/master.py").read())
else:
    print("You are about to install some python files to your computer!")
    print("They will be installed to the same directory as where this file is saved")
    check = input("If you want to continue type y: ")
    if check.lower()[0] == "y":
        install(pa)
        exec(open(pa + "\\python project\\mover.py").read())
        exec(open(pa + "/python project/master.py").read())
    else:
        print("Hope to see you again!")
        exit()
