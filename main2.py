"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 640              #sets screen parameters for screen width
SCREEN_HEIGHT = 480             #sets screen parameters for screen height
SCREEN_TITLE = "Move Keyboard Example"  #makes  the popup window named move keyboard example
MOVEMENT_SPEED = 10         #sets movement speed


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = 1
        self.position_y = 1
        self.change_x = 0
        self.change_y = 0
        self.radius = 10
        self.color = arcade.color.YELLOW

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:       
            self.position_x = SCREEN_WIDTH - self.radius               

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)              #sets background color to grey

        # Create our ball
        self.ball = Ball(1, 600, 0, 0, 15, arcade.color.AUBURN)         #sets where the ball starts and also the color

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()      #starts game engine render process 
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED             #sets the specific  movement speed to whatever you do with the directional keys
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0                          #at 0 it does nothing but if you set it to a number it will slowly drag itself to the right half of the screen 
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = -9.8                         #at 0 it does nothing but if you add a number it will kind of drag itself towards the top of the screen slowly after you first release the arrow key
                #oh my god i added gravity

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()