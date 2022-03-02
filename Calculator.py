
from curses import window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window 
from kivy.lang.builder import Builder



Window.size= (350, 550)
Builder.load_file('./calculator.kv')

class CalculatorWidgate(Widget):
    pass

class CalculatorApp(App):
    def build(self):
        return CalculatorWidgate()

if __name__ == "__main__":
    CalculatorApp().run() 