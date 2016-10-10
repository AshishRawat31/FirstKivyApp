import kivy
kivy.require('1.9.1')	#My version of Kivy

from kivy.app import App
from kivy.uix.label import Label

#add these two lines to slove OpeGL 1.1 error
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class MyApp(App):
    
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    MyApp().run()
