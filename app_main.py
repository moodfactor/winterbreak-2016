from kivy.app import App
from kivy.lang import Builder
#from kivy.uix.widget import Widget
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.uix.checkbox import CheckBox

from screens import *

Builder.load_file("ShapeSmasher.kv")

import random

class ShapeSmasherApp(App):
    """The physical App that the user will actually run and interact with.
    Apps generaly start with a titlescreen, and this app should be 
    renamed once a name is settled upon."""
    def build(self):
        """The build method of this App tells the App what to create when 
        it is run. As of now, when the App is run it displays whatever 
        is in Title Screen. In the future, the TitleScreen will contain 
        a BoxLayout containing several buttons which give the user 
        the option of checking out which game they want to play, going
        to a settings page, and seeng all time leaderboard results."""
        return LeaderboardScreen()
    def switchToGameScreen(self):
        """When completed, this method will return a BoxLayout that will 
        contain two items in a vertical layout: a BoxLayout and a
        GameWidget, a custom widget which deals with playing the actual
        game. The upper BoxLayout will contain small Labels corresponding 
        the player's current level and score and a button that takes the
        user to an options page."""
        pass

class DemoScreen(FloatLayout):
    """The TitleScreen is the first screen seen by the user upon entering
    the game; it will eventually contain buttons that will send the user 
    to either the main game, how-to-play, settings, or leaderboard screens.
    The TitleScreen's physical components are described in the ShapeSmasher.kv
    file."""

    # property describing the background color
    bg_color = ListProperty([0.8,1,0.7,0.9]) 
    
    def better(self, btn):
        """Simple method that demonstrates linking the components in the kv file
        to this python file. This method prints text to the console based on which
        button is pressed, and additionally changes the text on the buttons. Each 
        button thinks it is better than the other! This method also changes the 
        background to a random color using a ListProperty."""

        self.bg_color = [random.random() for i in range(3)]+[1]
        if(btn == self.ids.but_1):
            print('Button 1 is better!')
            self.ids.but_1.text = 'me!'
            self.ids.but_2.text = ''
        elif(btn == self.ids.but_2):
            print('Button 2 gets buckets, fam!')
            self.ids.but_2.text = 'me!'
            self.ids.but_1.text = ''
        else:
            print('Widget not recognized as button 1 or button 2')

if __name__ == '__main__':
    ShapeSmasherApp().run()
