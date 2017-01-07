"""File containing the Shape and Row abstractions that will be
displayed in the main game screen."""

from kivy.uix.button import Button

class Shape(Button):
    def __init__(self, shape_type, side_length, color_str, timer=None, clear_method='tap', health=1):
        self.shape_type = shape_type
        """ shape_type will be a string describing the type of shape_type
        i.e. triangle, hexagon, or square that will be tesselated to form the grid"""

        self.side_length = side_length
        """ side_length is an attribute that describes the length of the side of the shape.
        The side_length will need to be determined such that the tesselation fits within
        the width and height of the row. To do this, you will need to mathematically
        determine how long the side of a given shape will be using the size of the row."""

        self.color_str = color_str
        """ color will be a string describing the actual color that a shape will have.
        This string will be the key to a dictionary of colors where the corresponding
        values are RGBA lists as used by kivy.
        Additionally, there will be a list of color strings that can be randomly pulled
        from in order to randomize colors."""

        self.timer = timer
        """ Describes how much time is left to clear the shape. Default is None for
        game modes where no timer is required."""

        self.clear_method = clear_method
        """ A string that desribes how the given shape will be cleared, i.e. by tapping, swiping,
        or shaking. This leaves room for future gamemodes.
        You must check the clear_method of the shape. """

        self.health = 1
        """ health describes how many time a given shape has to be 'cleared' using its
        clear_method before it is actually removed from the board."""

    def on_press(self):
        pass
        """ This method will call decrement_health. In the case that the clear_method
        is not a tap, then on_press will be overridden in the constructor with an
        appropriate empty lambda function. The clear behavior will be implemented in
        the main game class and the update behavior will be implemented in the row class."""

    def decrement_health(self):
        pass
        """ This method will decrement the health."""

# Evan's work goes below, Jason's Work goes above
