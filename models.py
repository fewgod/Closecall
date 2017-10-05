import arcade
Player_Line_X = 300
Player_Line_Y = 100




class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.line_sprite = arcade.Sprite('images/line.png') #insert deathline picture
        self.line_sprite.set_position(Player_Line_X,Player_Line_Y) #set deathline position
        self.Lane_line_sprite = arcade.Sprite('images/laneline.png') #insert laneline picture
        self.Lane_line2_sprite = arcade.Sprite('images/laneline.png')
        self.Lane_line_sprite.set_position(200,450) #set laneline position
        self.Lane_line2_sprite.set_position(400,450)
 
 
    def update(self):
        self.line_sprite.draw()
        self.Lane_line_sprite.draw()
        self.Lane_line2_sprite.draw()