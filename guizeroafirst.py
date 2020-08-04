'''Demonstrates how guizero works.'''
#import the wedgets we need from quizero

from guizero import App, Text

#create the main window
App = App(layout="grid", title="Omris guizero window", bg=(200,200,200), width=(700))
#creating a text label
# the first paramiter is the location of the widget 
Header = Text(App, grid=[0,5], text="Sub g, heres my program!", font="calibri", size=40)
Header.text_color = (50,0,200)
#starts the program by displaying the module
App.display()
