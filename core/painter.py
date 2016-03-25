#!/usr/bin/python3
# coding: utf8
import pyglet 
import os, glob

pyglet.clock.set_fps_limit(60)

width = height = 160
max_row = max_col = 5
pyglet.resource.path = ['media/images']
pyglet.resource.reindex()
img_tower = pyglet.resource.image('tower.png')
img_tower.anchor_x=img_tower.width//2
img_tower.anchor_y=img_tower.height//2
img_grass = pyglet.resource.image('grass.png')
img_route = pyglet.resource.image('route.png')


img_monsters={}
for filename in glob.glob("media/images/monster*.png"):
    filename=os.path.split(filename)[1]
    name_file=os.path.splitext(filename)[0]

    attribs=name_file.split('-')
    attribs.remove('monster')
    attribs.sort()
    key=''.join([k[0] for k in attribs])
    img_monster = pyglet.resource.image(filename)
    img_monster.anchor_x=img_monster.width//2
    img_monster.anchor_y=img_monster.height//2
    img_monsters[key]=img_monster
    
game_window = None       

class Drawables():
    board=[]
    towers=[]
    monsters=[]
    sprites=[]
    score=0

drawables=Drawables()

def draw_field(board,towers):
    global game_window

    drawables.board = board
    drawables.towers = towers          
    game_window = pyglet.window.Window(width*max_row, height*max_col)        

    game_window.push_handlers(on_draw)
    refresh()

def draw(monsters,score):
    drawables.monsters = monsters
    drawables.score = score
    refresh()
    
def on_draw():
    paint_background()
    
    for tower in drawables.towers:
        sprite=paint_sprite(img_tower,
            tower.position
            )
        label = pyglet.text.Label(tower.type,
                              font_name='Times New Roman',
                              font_size=11,
                              x=sprite.x+img_tower.anchor_x, y=sprite.y,
                              anchor_x='center', anchor_y='top')
        label.draw()

    for monster in drawables.monsters:
        key=''
        if monster.life < 80:
            key+='d' #damaged
        if monster.freeze:
            key+='f'
        if monster.poison:
            key+='p'
        if monster.rage:
            key+='r'
        
        sprite=paint_sprite(img_monsters[key],
            monster.position)
        sprite.opacity=monster.opac()
            
    label = pyglet.text.Label('Score:'+str(drawables.score),
                          font_name='Times New Roman',
                          font_size=16,
                          x=game_window.width-5, y=game_window.height-5,
                          anchor_x='right', anchor_y='top')
    label.draw()

def paint_background():
    for row, line in enumerate(drawables.board):
        for col, value in enumerate(line):
            if value == 'G':
                image = img_grass
            else:
                image = img_route
            x=col*width
            y=max_row*height-(row+1)*height
            image.blit(x,y)
    

def paint_sprite(img,pos):
    x=pos[0]*8#-20
    y=max_row*height-pos[1]*8#-20
    sprite = pyglet.sprite.Sprite(img, 
        x=x,
        y=y)
    sprite.draw()
    return sprite

   
def draw_(monsters,score):
    for monster in monsters:
        if not monster in drawables.monsters:
            sprite=paint_sprite(img_monster,
                monster.position[0]*8-20,
                monster.position[1]*8+20
                )
            #drawables.monsters.append(monster)
            drawables.sprites.append(sprite)
            print ('hola mundo',monster.position)
        else:
            idx = drawables.monsters.index(monster)
            sprite = drawables.sprites[idx]
            sprite.x=monster.position[0]*8-20
            sprite.y=monster.position[1]*8+20

def refresh():
    pyglet.clock.tick()
    game_window.dispatch_events()
    game_window.dispatch_event('on_draw')
    game_window.flip()


if __name__=="__main__":
    from main import board
    draw_field(board,[])
