import arcade

SPRITE_SCALING = 1

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Fish Game"

MOVEMENT_SPEED = 5
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

# Index of textures, first element faces left, second faces right

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1
class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()


        self.scale = SPRITE_SCALING

        self.textures = []

        # Load a left facing texture and a right facing texture.

        # flipped_horizontally=True will mirror the image we load.

                # Add the screen title
        texture = arcade.load_texture("assets/pictures/mac_left.png")

        self.textures.append(texture)

        texture = arcade.load_texture("assets/pictures/mac_left.png",
                                      flipped_horizontally=True)

        self.textures.append(texture)



        # By default, face right.

        self.texture = texture


    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


        # Figure out if we should face left or right

        if self.change_x < 0:

            self.texture = self.textures[TEXTURE_LEFT]

        elif self.change_x > 0:

            self.texture = self.textures[TEXTURE_RIGHT]



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        arcade.load_font("assets/fonts/LuckiestGuy-Regular.ttf")

        # Call the parent class initializer
        super().__init__(width, height, title, fullscreen=True)

        # Variables that will hold sprite lists
        self.player_sprite_list = None

        self.background = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.text_title = arcade.Text(
            "FISH GAME",120.0,300.0, arcade.color.GREEN, 40, 80, 'center', 
            font_name="Luckiest Guy"
        )

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.background = arcade.load_texture("assets/pictures/backrooms.png")

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_sprite_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        # Draw all the sprites.
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player_sprite_list.draw()
        self.text_title.draw()
        
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_sprite_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()