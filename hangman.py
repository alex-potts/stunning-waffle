import random
import turtle
import time
import shutil
import os 

p = os.getcwd()
exec(open(p + "\\python project\\mover.py").read())
t = turtle.Turtle()
t.x = -50
t.y = 100
# pencil reveals the info
pencil = turtle.Turtle()
pencil.penup()
pencil.ht()
# pencil2 writes wrong guesses
pencil2 = turtle.Turtle()
pencil2.ht()
pencil2.penup()
pencil2.goto(50, 100)
pencil.style = ('Courier', 30, 'italic')
pencil.x = -200
t.speed(10)
t.ht()


def draw(lives):
    if lives == 1:
        drawHead()
    if lives == 2:
        drawBody()
    if lives == 3:
        drawLegs()
    if lives == 4:
        drawArms()
    if lives == 5:
        drawFrame()
    if lives == 6:
        drawNoose()
    else:
        pass


def drawHead():
    t.penup()
    t.goto(t.x, t.y)
    t.pendown()
    t.circle(50)


def drawBody():
    t.penup()
    t.goto(t.x, t.y)
    t.pendown()
    t.right(90)
    t.forward(50)
    t.forward(100)


def drawLegs():
    t.goto(t.x, t.y - 150)
    position = t.pos()
    t.right(30)
    t.forward(100)
    t.goto(position)
    t.left(60)
    t.forward(100)


def drawArms():
    t.penup()
    t.goto(t.x, t.y - 50.00)
    t.pendown()
    t.left(60)
    t.forward(50)
    t.left(180)
    t.forward(100)
# ends at (-50, 50)


def drawFrame():
    t.penup()
    t.goto(t.x - 50, t.y - 50)
    t.forward(100)
    t.pendown()
    t.left(90)
    t.forward(200)
    t.right(180)
    t.forward(500)
    t.right(90)
    t.forward(300)


def drawNoose():
    t.speed(1)
    t.penup()
    t.goto(t.x, t.y + 250.00)
    t.pendown()
    t.right(90)
    t.forward(150)


wrongGuesses = 0
wrongGuessesList = []


with open("mywords.txt", "r") as mywords:
    words = mywords.read().splitlines()
    word = random.choice(words)
    word = list(word)


correctguess = set({})
wrongguess = []


# this creates a list of te letters in the chosen word without duplicates
ndword = []
for i in word:
    if i not in ndword:
        ndword.append(i)


def revealinfo(x):
    correctguess.add(x)

    pencil.x = -200
    pencil.clear()

    for i in word:
        pencil.penup()
        pencil.goto(pencil.x, -220)
        pencil.pendown()
        pencil.x += 50
        if i in correctguess:
            pencil.write(i, font=pencil.style, align='center')
        else:
            pencil.write("__", font=pencil.style, align='center')


def userguess():
    global wrongGuesses
    guess = turtle.textinput("Guess", "Guess a letter")
    if guess in word:
        revealinfo(guess)
    else:
        wrongGuessesList.append(guess)
        wrongGuesses += 1
        draw(wrongGuesses)
        pencil2.write(guess)
        pencil2.forward(20)
        print("You have :", wrongGuesses, "incorrect guesses")


def lose():
    t.clear()
    pencil2.clear()
    pencil.clear()
    pencil.penup()
    pencil.goto(0, 0)
    pencil.pendown()
    pencil.write("You Lose XD", font=pencil.style, align='center')
    time.sleep(5)


def win():
    t.clear()
    pencil2.clear()
    pencil.clear()
    pencil.penup()
    pencil.goto(0, 0)
    pencil.pendown()
    pencil.write("You Win XD", font=pencil.style, align='center')
    time.sleep(5)


def show_blanks():
    pencil.x = -200
    for i in word:
        pencil.goto(pencil.x, -220)
        pencil.write("__", font=pencil.style)
        pencil.x += 50


show_blanks()
while wrongGuesses < 6:
    userguess()
    if len(correctguess) == len(ndword):
        print("you win")
        # you win screen
        win()
        break


if wrongGuesses >= 6:
    lose()
    print("game over")
    print("your word was", "".join(word))
    
dst_path = p + "/python project/mywords.txt"
src_path = p + "/mywords.txt"
shutil.move(src_path, dst_path)
