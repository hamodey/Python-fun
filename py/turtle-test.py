import turtle
import random
import math
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1000)
john = turtle.Turtle()
k = int(input("Enter your radius: "))
dotTot = int(input("Enter the arracy of your appox. (larger the more accurate): "))
def drawTriangle(aColour,size,turt):
    for i in [0,1,3]:
        turt.shape('turtle')
        turt.color(aColour)
        turt.left(120)
        turt.forward(size)

def drawSquare(aColour,size,turt):
    turt.shape('turtle')
    turt.color(aColour)
    for i in range(4):
        turt.forward(size)
        turt.left(90)

def randomI(start, end): 
    x = random.randrange(start,end)
    #print(x)
    return x
def placeDot(n, turt):
    w = 0
    for i in range(n):
        x = randomI(0,k)
        y = randomI(0,k)
        turt.pu()
        turt.goto(x,y)
        j = turt.dot(5,"black")
        turt.pd()
        dist = math.hypot(x, y)
        if dist > k:
            w += 1
            #print(w)
            turt.dot(5,'red')
    u = n - w
    h = u/n
    h = h*4
    print("Your pi approx is:",h)

def main():
    drawSquare('blue',k,alex)
    john.goto(k,0)
    john.left(90)
    john.circle(k,90)
    placeDot(dotTot,alex)

main()
