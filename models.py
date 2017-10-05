import arcade
import random
Player_Line_X = 300
Player_Line_Y = 100

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def update(self, delta):
        self.y -= 5


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture

        self.block = Block(100, 500)
 
 
    def update(self,delta):
        self.block.update(delta)