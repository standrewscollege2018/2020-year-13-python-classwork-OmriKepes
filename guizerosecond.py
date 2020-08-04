'''This funcaion runs a guizero program and forms an input box.'''
#important guizero addons
from guizero import App, Text, TextBox, PushButton
# print some text
def print_stuff():
    print(text_entry.vlaue)
    text.value = text_entry.value
#set the location
app = App(title="PushButton and textbox demo", bg=(50,50,50))
#create a text box called text_entry
text_entry = TextBox(app, width=20, height=2, multiline=True)
#create a button to print out what the user entered
print_button = PushButton(app, text="Push Me")
print_button.bg = (0,50,50)
print_button.text_color = "white"

app.display()