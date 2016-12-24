from kivy.app import App
class WB2016App(App):
    """The physical App that the user will actually run and interact with.
    Apps generaly start with a titlescreen, and this app should be 
    renamed once a name is settled upon.""".
    def build(self):
        """The build method of this App tells the App what to create when 
        it is run. As of now, when the App is run it displays whatever 
        is in Title Screen"""
        return TitleScreen()
