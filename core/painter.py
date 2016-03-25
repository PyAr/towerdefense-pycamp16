#!/usr/bin/python3
# coding: utf8
import pyglet 

width = height = 160
max_row = max_col = 5
pyglet.resource.path = ['media/images']
pyglet.resource.reindex()
img_tower = pyglet.resource.image('tower.png')
img_grass = pyglet.resource.image('grass.png')
img_route = pyglet.resource.image('route.png')
img_monster = pyglet.resource.image('monster.png')

       
game_window = pyglet.window.Window(width*max_row, height*max_col)        

class Drawables():
    board=[]
    towers=[]
    monsters=[]
    score=0

drawables=Drawables()

def draw_field(b,t):
    drawables.board = b
    drawables.towers = t          
    
    game_window.push_handlers(on_draw)
    pyglet.app.run()

    
def on_draw():
    for y, line in enumerate(drawables.board):
        for x, value in enumerate(line):
            if value == 'G':
                img = img_grass
            else:
                img = img_route
            paint_sprite(img,x*width,(y+1)*height)
    for tower in drawables.towers:
        paint_sprite(img_tower,
            tower.position[0]*8-20,
            tower.position[1]*8+20
            )
                
def paint_sprite(img,col,row):
    sprite = pyglet.sprite.Sprite(img, 
        x=col,
        y=(max_row*height-row))
    sprite.draw()

if __name__=="__main__":
    from main import board
    draw_field(board,[])
