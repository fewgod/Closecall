import arcade
from random import randint
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
        self.blocks = []
        Spawn_Lane = randint(1,3)
        if(Spawn_Lane == 1):
            block = Block(100, 700)
            self.blocks.append(block)
        if(Spawn_Lane == 2):
            block = Block(300, 700)
            self.blocks.append(block)
        if(Spawn_Lane == 3):
            block = Block(500, 700)
            self.blocks.append(block)

    def update(self,delta):
        if(randint(1,100) == 1):
            block = arcade.Sprite("images/block.png")
            Spawn_Lane = randint(1,3)
            if(Spawn_Lane == 1):
                block = Block(100, 700)
                self.blocks.append(block)
            if(Spawn_Lane == 2):
                block = Block(300, 700)
                self.blocks.append(block)
            if(Spawn_Lane == 3):
                block = Block(500, 700)
                self.blocks.append(block)
        for block in world.blocks:
            self.block.update(delta)
