import arcade
from random import randint
from models import World,Block
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 780
Player_Line_X = 300
Player_Line_Y = 100
 
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
        self.block_sprite = arcade.Sprite('images/block.png')
        #self.background = arcade.load_texture("images/background.jpg") หาทางใส่bg
        self.world = World(width, height)
        self.score = 0

        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        self.line_sprite.set_position(300,100) #set deathline position
        self.Lane_line_sprite = arcade.Sprite('images/laneline.png') #insert laneline picture
        self.Lane_line2_sprite = arcade.Sprite('images/laneline.png')
        self.Lane_line_sprite.set_position(200,450) #set laneline position
        self.Lane_line2_sprite.set_position(400,450)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.block_sprite.draw()
        output = f"Score: {self.world.score}" #ทำป้ายคะแนน
        self.score_text = arcade.create_text(output, arcade.color.BLACK, 14)
        arcade.render_text(self.score_text, 10, 20)
        self.line_sprite.draw() #ใส่ฉากหลังแบบไม่ใช่bg
        self.Lane_line_sprite.draw()
        self.Lane_line2_sprite.draw()
        for block in self.world.block_list1:
            block.draw()
        for block in self.world.block_list2:
            block.draw()
        for block in self.world.block_list3:
            block.draw()
    
    def update(self, delta):
        self.world.update(delta)

def main():
    window = ClosecallWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
 
if __name__ == '__main__':
    main()