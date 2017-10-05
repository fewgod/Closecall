import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
 
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
        self.line_sprite = arcade.Sprite('images/line.png')
        self.line_sprite.set_position(300,100)

    def on_draw(self):
        arcade.start_render()
        self.line_sprite.draw() 

def main():
    window = ClosecallWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()