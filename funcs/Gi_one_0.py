import pgzrun
HEIGHT = 400
WIDTH = 400

# rect with 100x100 size and 0,0 coordinates
rect = Rect ((0, 0) , (100,100))
rect2 = Rect ((250, 250), (50, 100 ))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(rect,'green')
    screen.draw.filled_rect(rect2,'maroon')

pgzrun.go()