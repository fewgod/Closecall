import arcade
import arcade.key
from random import randint
Player_Line_X = 300
Player_Line_Y = 100
BLOCK_SCALE = 1
class Block(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y
 
    def update(self, delta):
        self.center_y -= 5
        #if(self.y<100):
            #insert game over function
        if(self.center_y<200): #ตอนนี้ทำแค่เลยเส้นแล้วขึ้นไปบนใหม่
            self.center_y = 700


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        self.score = 0 #Initial Score = 0
        self.block_list = []
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if(round(780 -self.block.center_y)>=550): #ประมาณว่าถ้ากดใกล้เส้นตายมากๆจะได้คะแนนพิเศษ
                self.score += 200
            else:
                self.score += round((780 -self.block.center_y) *0.13)
    #def randomlane(self): #หาทางใส่ฟังก์ชั่นสุ่มสร้างบล็อคมาเรื่อยๆ

    def update(self,delta):
        #self.block.update(delta)
        if(randint(1,100)<4):
            Spawn_Lane = randint(1,3)
            if(Spawn_Lane == 1):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(100, 700)
                self.block_list.append(self.block)
            if(Spawn_Lane == 2):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(300, 700)
                self.block_list.append(self.block)
            if(Spawn_Lane == 3):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(500, 700)
                self.block_list.append(self.block)