import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file("kivy_calc.kv")
Window.size = (360, 640)

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        text = self.ids.calc_input.text

        if "Error!" in text:
            text = ""
        if text == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{text}{button}"
    
    def math_sign(self, sign):
        text = self.ids.calc_input.text
        self.ids.calc_input.text = f"{text}{sign}"

    def equals(self):
        text = self.ids.calc_input.text
        try:
            answer = eval(text)
            self.ids.calc_input.text = str(answer)
        
        except:
            self.ids.calc_input.text = "Error!"

    def dot(self):
        text = self.ids.calc_input.text
        num_list = text.split("+")
        if "+" in text and "." not in num_list[-1]:
            text = f"{text}."
            self.ids.calc_input.text = text
        elif "." in text:
            pass
        else: 
            text = f"{text}."
            self.ids.calc_input.text = text

    def remove(self):
        text = self.ids.calc_input.text
        if text=="0":
            pass
        else:
            text = text[:-1]
            self.ids.calc_input.text = text
            if len(text)==0:
                self.ids.calc_input.text = "0"

    def plusminus(self):
        text = self.ids.calc_input.text
        if "-" in text:
            self.ids.calc_input.text = f"{text.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{text}"


class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (3/255, 10/255, 26/255, 1)
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()