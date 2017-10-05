import arcade
import arcade.key
from random import randint
Player_Line_X = 300
Player_Line_Y = 100

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def update(self, delta):
        self.y -= 5
        #if(self.y<100):
            #insert game over function


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        Spawn_Lane = randint(1,3)
        if(Spawn_Lane == 1):
            self.block = Block(100, 700)
        if(Spawn_Lane == 2):
            self.block = Block(300, 700)
        if(Spawn_Lane == 3):
            self.block = Block(500, 700)
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.block.kill()
    #def randomlane(self):

    def update(self,delta):
        self.block.update(delta)