import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
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
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        self.line_sprite.set_position(Player_Line_X,Player_Line_Y) #set deathline position
        self.Lane_line_sprite = arcade.Sprite('images/laneline.png') #insert laneline picture
        self.Lane_line2_sprite = arcade.Sprite('images/laneline.png')
        self.Lane_line_sprite.set_position(200,450) #set laneline position
        self.Lane_line2_sprite.set_position(400,450)
    def on_draw(self):
        arcade.start_render()
        self.line_sprite.draw()
        self.Lane_line_sprite.draw()
        self.Lane_line2_sprite.draw()

def main():
    window = ClosecallWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()