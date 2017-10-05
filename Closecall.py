import arcade
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
        #self.background = arcade.load_texture("images/background.jpg") Not working
        self.world = World(width, height)

    def on_draw(self):
        arcade.start_render()
        self.block_sprite.draw()
    
    def update(self, delta):
        self.world.update(delta)
        self.block_sprite.set_position(self.world.block.x, self.world.block.y)

def main():
    window = ClosecallWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
 
if __name__ == '__main__':
    main()