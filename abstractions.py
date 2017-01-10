"""File containing the Shape and Row abstractions that will be
displayed in the main game screen."""

from kivy.uix.button import Button

class Shape(Button):
    """The Shape class is a generalized abstraction for the individual shapes that
    will appear on the game screen. Each Shape has certain properties that will
    be used by the GameState and Row class in order to construct the screen and keep
    track of individual shape objects.

    There are properties that have been defaulted to provide for future game modes,
    such as timer, clear_method, and health.

    Look in the __init__ constructor for more specific descriptions of each attribute.

    Keep in mind that while some properties of each Shape objects describe visual
    properties, all handling of graphics are abstracted and will occur in the
    GameState."""

    def __init__(self, shape_type, side_length, color_str, game_state=None, timer=None, clear_method='tap', health=1):

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

        self.game_state = game_state
        """game_state is a reference to the GameState instance in which this Shape is being
        placed. It is initially defaulted to None, and is initialized either upon the construction of
        the GameState instance that this Shape is added to or upon this Shape's construction if
        the Shape is being added to a previously existing GameState instance."""

        self.timer = timer
        """ Describes how much time is left to clear the shape. Default is None for
        game modes where no timer is required."""

        self.clear_method = clear_method
        """ A string that desribes how the given shape will be cleared, i.e. by tapping, swiping,
        or shaking. This leaves room for future gamemodes.
        You must check the clear_method of the shape. """

        if self.clear_method != 'tap':
            self.on_press = lambda : None

        self.health = 1
        """ health describes how many time a given shape has to be 'cleared' using its
        clear_method before it is actually removed from the board."""

    def on_press(self):
        """ This method will call decrement_health. In the case that the clear_method
        is not a tap, then on_press will be overridden in the constructor with an
        appropriate empty lambda function. The clear behavior will be implemented in
        the main game class and the update behavior will be implemented in the row class."""
        self.decrement_health()

    def decrement_health(self):
        """ This method will decrement the health."""
        self.health -= 1

# Evan's work goes below, Jason's Work goes above

class Row():
    """The Row class abstractly represents a row in the grid of
    the main Game. Each row contains a list of length row_length
    that is initially filled with "None" values but can be modified
    to contain Shape objects.

    Each row also stores an x and y offset that describes how much
    the entire row will be offset from the traditional square grid
    positions.

    PLEASE NOTE that all functionality in this class is abstract and
    NOT graphics related. Graphics are handled by the GameState class.
    """

    def __init__(self, row_length, x_offset, y_offset):
        """Initializes a Row object with a list of None that
        is of length row_length. Also stores x_offset and
        y_offset as instance variables named x_offset and
        y_offset"""
        pass

    def add_shape(self, shape, pos):
        """This method asserts that the given shape is indeed
        an instance of the Shape class and then adds the shape
        to this row's list of shapes at the specified position
        ONLY IF THAT POSITION IS CURRENTLY NONE."""
        pass

    def update(self):
        """This method iterates through the list of shapes and
        Nones contained by this Row. For each non-None Shape in
        the list, this method checks if that Shape has 0 health
        remaining. If so, it removes that shape from the board."""
        pass

    def remove_shape(self, index):
        """This method removes the shape at the given list index
        from this Row's list of shapes by setting the list value
        at that index to be None. it also uses the Shape's stored
        GameState to increase the score of that gameState by 10 points."""


class GameState():
    """This class contains all the data (in the form of Rows)
    that represents a ShapeSmasher Game in any mode. This class
    ALSO handles graphics updates to the game's screen, although
    even within this class methods are either abstract (solely
    devoted to manipulating data) or concrete (solely devoted to
    displaying data).

    A GameState contains a list of Row Objects (all of which must
    actually be Row Objects: no NoneTypes allowed). A GameState also
    stores a string describing which game mode is being played as well
    as a Widget of some sort in which the contents of this game will
    actually be displayed."""



    def __init__(self, game_mode, row_list, game_screen):
        """The constructor for a GameState requires both the type of
        Game being played, the list of rows that describes
        the current state of the Game, and the widget on which the game
        will be displayed. The constructor maeks sure these parameters
        are formatted correctly and stores them as instance attributes.

        This constructor calculates and sets an integer instance variable
        representing the number of empty spaces (spaces without a shape)
        in the game at its beginning, i.e. the total number of places in the
        grid. It also sets an instance variable score, which will start at 0.
        This constructor must also iterate through each shape in each Row
        (if there are any non-None Shapes to start with) to make sure those
        Shapes have a correctly initialized GameState attribute."""
        pass

    def draw(self):
        """This method is purely devoted to looking at the contents
        of this GameState's row_list and displaying that data on the
        game_screen. Each spot on the physical screen will be drawn
        using either a Shape's image representation or an empty shape
        representation (up to you, can just be nothing if you want)."""
        pass

    def update_event(self, event):
        """This is a general method used to update the game data when
        some event such as a swipe or shake is detected. This method
        will iterate through each row and each non-None Shape, updating
        the data (most likely health) of the shape if necessary based
        on the event. If the health of a shape reaches 0, that Shape
        is removed and the gameState's instance variable describing number
        of open spaces is decremented to reflect this.

        This method does not modify the game_screen until
        the last line, which will be a call to the draw() method."""
        pass

    def update(self):
        """This method is a general purpose update method for the gameState
        that is mean to be called on regular intervals of time. The
        method simply makes a call to the correct update method for this GameState's
        game mode as determined by the game_mode string (handled with a dispatch dictionary)."""
        pass

    def update_timed_mode(self):
        """This method is used specifically to update the game in timed mode.
        This method will be called once every second and will reduce each Shape's
        simple integer clock by 1. If any of these clocks goes to 0, this method
        stops the game by calling the game_over method. It also adds Shapes to the
        abstracted grid of Shapes.

        Here's the way adding Shapes will work:
        As you traverse the list of Rows which each contain lists of shapes, every
        empty space (i.e. every time a list has a None entry) will have a 0.15 chance
        to get a new Shape put in. However, a count of the number of shapes added will
        be updated as you traverse all the spots in the grid as well as a list of
        coordinate pairs missing shapes. If at any point during the traversal the
        number of shapes added exceeds 2/3 of the number of empty spaces remaining in
        the grid, no more shapes will be added. Conversely, if your program has added
        less than 5 new shapes after it has finished traversing, select random coordinate
        pairs from the temporary list you have been maintaining to put new Shapes into
        until 5 new Shapes have been placed or the board is full.

        This will ensure wild chaos and hilarity as differing numbers of shapes are
        added every second in random places."""
        pass

    def update_health_mode(self):
        """This method is used to update the game in health mode, a mode where shapes
        with variable health values are added quickly to the screen and the player loses
        if the entire grid fills up with shapes. (Alex pls finsh am tired no quiero trabajar)"""
        pass


    mode_dispatch = {'timed': (update_timed_mode,1) , 'health': (update_health_mode, 0.25)}
    #dispatch dictionary for different game modes and update times

    def game_over(self):
        """This method should be called when a condition is reached such that the game
        is over. this should stop the game's updating loop somehow and use the screen
        to exit and go to the leaderboard screen. The action of going to the leaderboard
        should also carry with it the score stored by this gameState so it can be placed
        onto the leaderboard."""
        pass
