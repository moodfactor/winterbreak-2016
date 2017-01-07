"""File containing the Shape and Row abstractions that will be 
displayed in the main game screen."""


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
        at that index to be None."""



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
        are formatted correctly and stores them as instance attributes."""
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
        on the event. This method does not modify the game_screen until
        the last line, which will be a call to the draw() method."""
        pass
     
