import pgzrun

WIDTH = 700
HEIGHT = 1000

square = Rect ((400,250), (50, 50))

def draw():
    screen.clear()
    screen.draw.filled_rect(square,'red')

def update():
    square.x += 1
    print(square.x)

pgzrun.go()