import arcade
import arcade.key
from random import randint
PLAYER_LINE_X = 100
LANE1_X = 100
LANE2_X = 300
LANE3_X = 500
LANE_Y = 750
BLOCK_SCALE = 1
PERFECT_Y = 75 #distance when press for perfect score
GAME_OVER = False
class Block(arcade.Sprite):
    def setup(self, x, y):
        self.center_x = x
        self.center_y = y
 
    def update(self, delta):
        self.center_y -= 5


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        self.score = 0 #Initial Score = 0
        self.block_list1 = [] #สร้างlist ไว้เก็บบล็อคที่อยู่ในเลน 1,2,3ตามลำดับ
        self.block_list2 = []
        self.block_list3 = []
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            if(round(self.block_list1[0].center_y - PLAYER_LINE_X)<= PERFECT_Y): #ประมาณว่าถ้ากดใกล้เส้นตายมากๆจะได้คะแนนพิเศษ
                self.score += 200
            else:
                self.score += round((780 -self.block_list1[0].center_y) *0.13)   
            del self.block_list1[0] #ลบข้อมูลตัวแรกในblock_list1 ซึ่งก็คือตัวที่ใกล้เส้นมากที่สุด
        
        if key == arcade.key.S:
            if(round(self.block_list2[0].center_y - PLAYER_LINE_X)<= PERFECT_Y):
                self.score += 200
            else:
                self.score += round((780 -self.block_list2[0].center_y) *0.13)   
            del self.block_list2[0]

        if key == arcade.key.D:
            if(round(self.block_list3[0].center_y - PLAYER_LINE_X)<= PERFECT_Y):
                self.score += 200
            else:
                self.score += round((780 -self.block_list3[0].center_y) *0.13)   
            del self.block_list3[0]

    def update(self,delta):
        #self.block.update(delta)
        if(randint(1,100)<4):
            Spawn_Lane = randint(1,3)
            if(Spawn_Lane == 1):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(LANE1_X, LANE_Y) #สร้างblock
                self.block_list1.append(self.block) #add blockเข้าไปในlist block_list1
            if(Spawn_Lane == 2):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(LANE2_X, LANE_Y)
                self.block_list2.append(self.block)
            if(Spawn_Lane == 3):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(LANE3_X, LANE_Y)
                self.block_list3.append(self.block)
        for block in self.block_list1:
            block.update(delta)
            if(block.center_y<115):
                self.block_list1.remove(block) #blockของlane1เลยขอบแล้วจะลบblockนั้นออก
        for block in self.block_list2:
            block.update(delta)
            if(block.center_y<115):
                self.block_list2.remove(block)
        for block in self.block_list3:
            block.update(delta)
            if(block.center_y<115):
                self.block_list3.remove(block)