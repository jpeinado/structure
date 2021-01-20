# Imports library external for class graphics in win32
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
# Deveplopment of class graphics loginScreen with Kivy framework
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.submit = Button(text="Submit",font_size=40)
        self.add_widget(self.submit)

class simplekivy(App):
    def build(self):
        #lbl = Label(text="Hello world")
        #btn = Button(text="Push Me", size_hint=(.2,.2),pos=(300,250))
        #return Label(text="hello world")
        return LoginScreen()

if __name__ == "__main__":
    simplekivy().run()