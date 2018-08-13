from graphics import *
import time
import random

#generate a random point to be eaten by the snake
def generatePoint(snake):
    x = random.randrange(30,580,10)
    diff = 0
    while (diff < len(snake)):
        diff = 0
    
        for i in range(len(snake)):
            if (x != snake[i].getX()):
                diff = diff + 1

        if (diff < len(snake)):
            x = random.randrange(30,580,10)

    y = random.randrange(30,580,10)
    diff = 0
    while (diff < len(snake)):
        diff = 0
    
        for i in range(len(snake)):
            if (y != snake[i].getY()):
                diff = diff + 1

        if (diff < len(snake)):
            y = random.randrange(30,580,10)
    return Point(x,y)

#create a border for the game
def createBorder():
    rect = Rectangle(Point(win.getWidth() / 2 - 280, win.getHeight() / 2 + 280), Point(win.getWidth() / 2 + 280, win.getHeight() / 2 - 280))
    rect.draw(win)
    rect.setOutline('white')

#generate a list of lines for the snake
def generateSnake(line, snake):
    for i in range(len(snake) - 1):
        line.append(Line(snake[i], snake[i+1]))        

#generate and draw game over message
def GameOver():
    gameOver = Text(Point(win.getWidth() / 2, win.getHeight() / 2), "GAME OVER")
    gameOver.draw(win)
    gameOver.setOutline('white')
    gameOver.setFace('courier')
    gameOver.setSize(50)

win = GraphWin('Snakes', 600, 600)
win.yUp()
win.setBackground('black')

snake = [Point(80,500), Point(70,500), Point(60,500), Point(50,500), Point(40,500), Point(30,500)]
dx = 10
dy = 0
state = 'horizontal'

pointCenter = generatePoint(snake)
createBorder()

eaten = False
level = 1

#check that snake has not eaten itself and it is still within the border
while (eaten == False and snake[0].getX() > win.getWidth() / 2 - 280 and snake[0].getX() < win.getWidth() / 2 + 280 and snake[0].getY() > win.getHeight() / 2 - 280 and snake[0].getY() < win.getHeight() / 2 + 280):

    #create an empty list to be filled with lines that make up the snake
    line = []
    
    #generate and draw level message
    levelMessage = Text(Point(win.getWidth() - 60, win.getHeight() - 10), "Level {}".format(level))
    levelMessage.draw(win)
    levelMessage.setOutline('white')
    levelMessage.setFace('courier')

    pointHit = False

    #draw the randomly generated point
    point = Circle(pointCenter, 1)
    point.draw(win)
    point.setOutline('white')
    point.setFill('white')
    point.setWidth(4)

    #generate the snake
    generateSnake(line, snake)

    #draw the snake
    for i in range(len(line)):
        line[i].draw(win)
        line[i].setOutline('green')
        line[i].setWidth(3)

    #generate and draw head of the snake
    head = Circle(Point(snake[0].getX(),snake[0].getY()),1)
    head.draw(win)
    head.setWidth(4)
    head.setOutline('red')

    #move the whole snake by 10 pixels in a certain direction
    for i in range(len(snake)-1,0,-1):
        snake[i]= Point(snake[i-1].getX(), snake[i-1].getY())
    snake[0].move(dx,dy)

    #make a delay to show snake before deleting
    time.sleep(0.15)

    #delete the snake and its head
    for i in range(len(line)):
        line[i].undraw()
    head.undraw()

    #get which key is pressed, if any
    key = win.checkKey()

    #change direction of snake depending on key pressed
    if (state == 'horizontal'):
        if (key == 'Down' or key == 's'):
            dx = 0
            dy = -10
            state = 'vertical' 
        elif (key == 'Up' or key == 'w'):
            dx = 0
            dy = 10
            state = 'vertical'
    
    elif (state == 'vertical'):
        if (key == 'Left' or key == 'a'):
            dx = -10
            dy = 0
            state = 'horizontal'
        elif (key == 'Right' or key == 'd'):
            dx = 10
            dy = 0
            state = 'horizontal'

    #check if snake hits the point
    if (snake[0].getX() == pointCenter.getX() and snake[0].getY() == pointCenter.getY()):
        pointHit = True
        level = level + 1   #player levels up   
        pointCenter = generatePoint(snake)   #generate a new random point
        snake.append(Point(2 * snake[len(snake)-1].getX() - snake[len(snake)-2].getX(), 2 * snake[len(snake)-1].getY() - snake[len(snake)-2].getY()))   #increase length of the snake

    #check if snake has eaten itself
    i = 1
    while (i < len(snake) and eaten == False):
        if (snake[0].getX() == snake[i].getX() and snake[0].getY() == snake[i].getY()):
            eaten = True
        i = i + 1

    #delete the point and level message
    point.undraw()
    levelMessage.undraw()

#generate and draw snake and head one more time to show crash
generateSnake(line, snake)  
for i in range(len(line)):
    line[i].draw(win)
    line[i].setOutline('green')
    line[i].setWidth(3)

head = Circle(Point(snake[0].getX(),snake[0].getY()),1)
head.draw(win)
head.setWidth(4)
head.setOutline('red')

#make a short delay, then delete snake and head
time.sleep(0.5)
for i in range(len(line)):
    line[i].undraw()
head.undraw()

#draw level message showing final level
levelMessage = Text(Point(win.getWidth() - 60, win.getHeight() - 10), "Level {}".format(level))
levelMessage.draw(win)
levelMessage.setOutline('white')
levelMessage.setFace('courier')

#show game over message
GameOver()

#waits for user to press the Enter button
while(win.checkKey() != 'Return'):
    pass

win.close()

