from kivy.app import App 
from kivy.uix.label import Label

from kivy.core.window import Window

Window.size = (300, 100)
Window.clearcolor = (255/255, 186/255, 3/255, 1) 
Window.title = "Приложение"

class MyApp(App):

    def build(self):
        label = Label(text='Моя программа\nВсё работает!')

        return label

if __name__ == "__main__":
    MyApp().run()  