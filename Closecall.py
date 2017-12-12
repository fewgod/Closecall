import arcade
from random import randint
from models import World,Block
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 780
INSTRUCTION_STATE = 0
GAME_RUNNING_STATE = 1
GAME_OVER_STATE = 2

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class ClosecallWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.background = arcade.load_texture("assets/images/bgwithpressarea.jpg") #ใส่bg
        self.world = World(width, height)
        self.score = 0
        self.combo = 0

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        '''draw bg''' #draw background before scoreboard otherwise you cannot see the scoreboard(will bring bg to the front of scoreboard)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        '''Score Board'''
        output = f"Score: {self.world.score}" #ทำป้ายคะแนน
        self.score_text = arcade.create_text(output, arcade.color.BLACK, 14)
        arcade.render_text(self.score_text, 10, 20) #วาดป้ายคะแนน
        output_gain = f"+ {self.world.gain_score}" #ทำข้อความเวลาได้คะแนน
        output_gain_minus = f" {self.world.gain_score}" #ทำข้อความเวลาได้คะแนนติดลบ
        self.score_gain_text = arcade.create_text(output_gain, arcade.color.BLACK, 14)
        self.score_gain_minus_text = arcade.create_text(output_gain_minus, arcade.color.BLACK, 14)
        if self.world.gain_score != 0:
            if self.world.gain_score >0:
                arcade.render_text(self.score_gain_text, 150, 20)
            else:
                arcade.render_text(self.score_gain_minus_text, 150, 20)

        output_combo = f"Combo {self.world.combo} !" #ขึ้นคำว่าCombo +จำนวนcombo หากกดอยู่ในช่วง
        output_perfect_combo = f"Perfect {self.world.combo} !" #ขึ้นคำว่าPerfectแทนคำว่าCombo +จำนวนcombo หากกดอยู่ในช่วงPerfect
        self.combo_text = arcade.create_text(output_combo, arcade.color.BLACK, 16)
        self.perfect_combo_text = arcade.create_text(output_perfect_combo, arcade.color.BLACK, 16)
        if self.world.combo >=3:
            if self.world.gain_score >= 200:
                arcade.render_text(self.perfect_combo_text, 250, 65)
            else:
                arcade.render_text(self.combo_text, 250, 65)

        ''' draw block in each lane'''
        for block in self.world.block_list1:
            block.draw()
        for block in self.world.block_list2:
            block.draw()
        for block in self.world.block_list3:
            block.draw()

        '''draw instruction and gameover page'''
        if self.world.current_state == INSTRUCTION_STATE:
            self.world.instruction_sprite.draw()
        if self.world.current_state == GAME_OVER_STATE:
            self.world.gameover_sprite.draw()
            final_score = f"You've score {self.world.score} pts"
            self.total_score_text = arcade.create_text(final_score, arcade.color.BLACK, 15)
            arcade.render_text(self.total_score_text, 215, 300)
        
    def update(self, delta):
        self.world.update(delta)

def main():
    window = ClosecallWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
 
if __name__ == '__main__':
    main()