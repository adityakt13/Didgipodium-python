import pgzrun

WIDTH = 700
HEIGHT = 1000

square = Rect ((400,250), (50, 50)) # 1st square
square2 = Rect ((300,300), (60,75)) # 2nd square

square2_vx = 2 #global variable

def draw():
    screen.clear()
    screen.draw.filled_rect(square,'red')
    screen.draw.filled_rect(square2,'white')

def update():
    global square2_vx # this alows us to change the value of b_vx
    # loop aroung the screen
    square.x += 2
    if square.x > WIDTH:
        square.x = 0
    #bounc the bx
    square2.x += square2_vx
    if square2.right > WIDTH or square2.left < 0:
        square2_vx = -square2_vx # invert the direction of the box

pgzrun.go()