from kivy.app import App
class ShapeSmasherApp(App):
    """The physical App that the user will actually run and interact with.
    Apps generaly start with a titlescreen, and this app should be 
    renamed once a name is settled upon."""
    def build(self):
        """The build method of this App tells the App what to create when 
        it is run. As of now, when the App is run it displays whatever 
        is in Title Screen. In the future, the TitleScreen will be made 
        up of a BoxLayout containing several buttons which give the user 
        the option of checking out which game they want to play, going
        to a settings page, and seeng all time leaderboard results."""
        return TitleScreen()
    def switchToGameScreen(self):
        """When completed, this method will return a BoxLayout that will 
        contain two items in a vertical layout: a BoxLayout and a
        GameWidget, a custom widget which deals with playing the actual
        game. The upper BoxLayout will contain small Labels corresponding 
        the player's current level and score and a button that takes the
        user to an options page."""
        pass
