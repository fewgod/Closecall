import arcade
import arcade.key
from random import randint
PLAYER_LINE_Y = 100
LANE1_X = 100 #center_x of lane1,2,3
LANE2_X = 300
LANE3_X = 500
LANE_Y = 750
BLOCK_SCALE = 1
PERFECT_Y = 33 #distance from player line when press for perfect score
UPPER_PRESS_AREA = 163
LOWER_PRESS_AREA = 115
INSTRUCTION_STATE = 0
GAME_RUNNING_STATE = 1
GAME_OVER_STATE = 2

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
        self.score = 0 #Initial Score = 0
        self.block_list1 = [] #สร้างlist ไว้เก็บบล็อคที่อยู่ในเลน 1,2,3ตามลำดับ
        self.block_list2 = []
        self.block_list3 = []
        self.Lane1_Waittime = 0 #init Lane Waittime
        self.Lane2_Waittime = 0
        self.Lane3_Waittime = 0
        self.gain_score = 0 #เอาไว้แสดงคะแนนที่ได้
        self.combo = 0
        self.multiplier = 1 #เอาไว้คูณกับcombo เวลาได้comboเยอะๆจะได้คะแนนยิ่งสูง
        self.current_state = INSTRUCTION_STATE #set up the current state

        self.instruction_sprite = arcade.Sprite('assets/images/instruction.png')#show instruction when start game
        self.instruction_sprite.set_position(325,450)
        self.gameover_sprite = arcade.Sprite('assets/images/gameover.png')#show game over image when
        self.gameover_sprite.set_position(295,450)
        #self.hit_sfx = arcade.sound.load_sound('assets/sound/')
        #arcade.sound.play_sound(self.hit_sfx)

    '''Button'''
    def on_key_press(self, key, key_modifiers):

        if (self.current_state == GAME_RUNNING_STATE and key == arcade.key.A):
            if(self.block_list1 and round(self.block_list1[0].center_y - PLAYER_LINE_Y)<= PERFECT_Y):
                self.gain_score = 200 + round(self.multiplier*self.combo) #gain perfect score when press almost pass the player line
                self.score += self.gain_score
                self.combo += 1
                del self.block_list1[0]
            elif(self.block_list1 and self.block_list1[0].center_y <= UPPER_PRESS_AREA and self.block_list2[0].center_y >= LOWER_PRESS_AREA):
                self.gain_score = round(100 + ((self.multiplier*self.combo) *0.2))
                self.score += self.gain_score
                self.combo += 1
                del self.block_list1[0]
            else: #When press outside PRESS AREA
                self.gain_score = -50 #score deduction when press outside
                self.score += self.gain_score
                self.combo = 0 #reset combo if press outside PRESS_AREA
        
        if (self.current_state == GAME_RUNNING_STATE and key == arcade.key.S):
            if(self.block_list2 and round(self.block_list2[0].center_y - PLAYER_LINE_Y)<= PERFECT_Y):
                self.gain_score = 200 + round(self.multiplier*self.combo)
                self.score += self.gain_score
                self.combo += 1
                del self.block_list2[0]
            elif(self.block_list2 and self.block_list2[0].center_y <= UPPER_PRESS_AREA and self.block_list2[0].center_y >= LOWER_PRESS_AREA):
                self.gain_score = round(100 + ((self.multiplier*self.combo) *0.2))
                self.score += self.gain_score
                self.combo += 1
                del self.block_list2[0]
            else:
                self.gain_score = -50
                self.score += self.gain_score
                self.combo = 0

        if (self.current_state == GAME_RUNNING_STATE and key == arcade.key.D):
            if(self.block_list3 and round(self.block_list3[0].center_y - PLAYER_LINE_Y)<= PERFECT_Y):
                self.gain_score = 200 + round(self.multiplier*self.combo)
                self.score += self.gain_score
                self.combo += 1
                del self.block_list3[0]
            elif(self.block_list3 and self.block_list3[0].center_y <= UPPER_PRESS_AREA and self.block_list2[0].center_y >= LOWER_PRESS_AREA):
                self.gain_score = round(100 + ((self.multiplier*self.combo) *0.2))
                self.score += self.gain_score
                self.combo += 1
                del self.block_list3[0]
            else:
                self.gain_score = -50 
                self.score += self.gain_score
                self.combo = 0
        
        if (self.current_state == INSTRUCTION_STATE and key == arcade.key.S):
            self.current_state = GAME_RUNNING_STATE

        if (self.current_state == GAME_OVER_STATE and key == arcade.key.S):
            self.combo = 0
            self.gain_score = 0
            self.score = 0
            self.block_list1 = []
            self.block_list2 = []
            self.block_list3 = []
            self.current_state = INSTRUCTION_STATE
        
        output_gain = f"+ {self.gain_score}" #ทำป้ายคะแนน
        self.score_gain_text = arcade.create_text(output_gain, arcade.color.BLACK, 14)
        arcade.render_text(self.score_gain_text, 20, 20)

    def update(self,delta):
        '''combo multiplier'''
        if(self.combo>8 and self.combo <= 15):
            self.multiplier = 1.15
        elif(self.combo <= 25):
            self.multiplier = 1.25
        elif(self.combo <= 45):
            self.multiplier = 1.35
        elif(self.combo < 70):
            self.multiplier = 1.5
        elif(self.combo >= 100):
            self.multiplier = 1.75
        
        '''spawn block'''
        if(randint(1,100)<5 and self.current_state == GAME_RUNNING_STATE):
            Spawn_Lane = randint(1,3)
            if(Spawn_Lane == 1 and self.Lane1_Waittime <5):
                self.block = Block('images/block.png', BLOCK_SCALE) # Block scale คือเอาขนาดภาพเท่าไหร่เทียบกับขนาดoriginal 1=100%
                self.block.setup(LANE1_X, LANE_Y) #สร้างblock
                self.block_list1.append(self.block) #add blockเข้าไปในlist block_list1
                self.Lane1_Waittime = 20
            if(Spawn_Lane == 2 and self.Lane2_Waittime <5): #ไม่ให้ออกติดกันเกินไปในช่องเดียวกัน
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(LANE2_X, LANE_Y)
                self.block_list2.append(self.block)
                self.Lane2_Waittime = 20 #สร้างblockแล้วก็ใส่เวลารอของLaneนี้ใหม่ รอ1frame
            if(Spawn_Lane == 3 and self.Lane3_Waittime <5):
                self.block = Block('images/block.png', BLOCK_SCALE)
                self.block.setup(LANE3_X, LANE_Y)
                self.block_list3.append(self.block)
                self.Lane3_Waittime = 20
        
        '''Check if block passed player line'''
        for block in self.block_list1:
            if self.current_state == GAME_RUNNING_STATE:
                block.update(delta)
            if(block.center_y<115):
                self.current_state = GAME_OVER_STATE
        for block in self.block_list2:
            if self.current_state == GAME_RUNNING_STATE:
                block.update(delta)
            if(block.center_y<115):
                self.current_state = GAME_OVER_STATE
        for block in self.block_list3:
            if self.current_state == GAME_RUNNING_STATE:
                block.update(delta)
            if(block.center_y<115):
                self.current_state = GAME_OVER_STATE
        self.Lane1_Waittime -=1
        self.Lane2_Waittime -=1
        self.Lane3_Waittime -=1
