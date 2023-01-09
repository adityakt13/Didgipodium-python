from random import randint , choice
import pgzrun

WIDTH = 900
HEIGHT = 500

box1 = Rect((100,100),(50,50))
box2 = Rect(( 140,200),(50,50))
b1x = 3
b2x = 3

def draw() :
    screen.clear()
    screen.draw.filled_rect(box1, 'Red')
    screen.draw.filled_rect(box2, 'Blue')

# we can read global variable inside a function but can't changed
# but we can use global keyword to access and manipulate a global variable 
# indside a function 
def update ():
    global b1x , b2x
    box1.x += b1x
    box2.x += b2x
    if box2.right > WIDTH or box2.left <0 :
        sounds.tappukepapa.play()
        b2x = - b2x
    if box1.right > WIDTH or box1.left <0 :
        sounds.saatvifail.play()
        b1x = - b1x
pgzrun.go()