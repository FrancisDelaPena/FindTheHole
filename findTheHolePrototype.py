from graphics import *
import random

def makeHole(point, radius, win):
    hole = Circle(point, radius)
    hole.setFill('green')
    hole.setOutline('green')
    hole.draw(win)

    return hole

def getDistance(point1, point2):
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return ((dx*dx + dy*dy)**.5)

def makeRect(corner, width, height, color, win):
    ''' Return a Rectangle drawn in win with the upper left corner
    and color specified.'''

    corner2 = corner.clone()  
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def main():
    win = GraphWin("Find the Hole", 400, 400)
    win.yUp()
    win.setBackground('green')

    makeRect(Point(0, 400), 65, 20, 'yellow', win)
    counts = 0
    tries = Text(Point(win.getWidth()/12, 390),'Tries: {}'.format(counts))
    tries.draw(win)

    radius = random.randrange(10, 100)
    x = random.randrange(5, 395)
    y = random.randrange(5, 395)
    center = Point(x, y)

    hole = makeHole(center, radius, win)
    
    makeRect(Point(100, 400), 200, 40, 'white', win)
    instructions = Text(Point(win.getWidth()/2, 390),'Click around to find the hole')
    instructions.draw(win)
    chances = Text(Point(win.getWidth()/2, 375),'You have 10 chances')
    chances.draw(win)

    pt = win.getMouse()
    pt.draw(win)
    counts = counts + 1
    tries.undraw()
    tries = Text(Point(win.getWidth()/12, 390),'Tries: {}'.format(counts))
    tries.draw(win)
    
    distance = getDistance(center, pt)
    
    while distance > radius:
        pt = win.getMouse()
        pt.draw(win)
        distance = getDistance(center, pt)
        counts = counts + 1
        tries.undraw()
        tries = Text(Point(win.getWidth()/12, 390),'Tries: {}'.format(counts))
        tries.draw(win)

        if counts >= 10:
            hole.setOutline('red')
            makeRect(Point(100, 225), 200, 50, 'red', win)
            lost = Text(Point(win.getWidth()/2, 200),'Better luck next time...')
            lost.draw(win)
        
            closer = Text(Point(win.getWidth()/2, 20),'Click anywhere to quit')
            closer.draw(win)
            win.getMouse()
            win.close()
    
    hole.setFill('black')
    makeRect(Point(100, 215), 200, 50, 'blue', win)
    won = Text(Point(win.getWidth()/2, 200),'You won!')
    won.draw(win)
            
    closer = Text(Point(win.getWidth()/2, 20),'Click anywhere to quit')
    closer.draw(win)
    win.getMouse()
    win.close()

main()
