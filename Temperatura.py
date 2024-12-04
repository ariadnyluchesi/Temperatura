from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ConverterApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation="vertical")
        
        self.input_celsius = TextInput(hint_text="Celsius", input_filter='float')
        self.main_layout.add_widget(self.input_celsius)
        
        self.to_fahrenheit_button = Button(text="Converter para Fahrenheit", on_press=self.convert_to_fahrenheit)
        self.main_layout.add_widget(self.to_fahrenheit_button)
        
        self.input_fahrenheit = TextInput(hint_text="Fahrenheit", input_filter='float')
        self.main_layout.add_widget(self.input_fahrenheit)
        
        self.to_celsius_button = Button(text="Converter para Celsius", on_press=self.convert_to_celsius)
        self.main_layout.add_widget(self.to_celsius_button)
        
        self.result_label = Label(text="")
        self.main_layout.add_widget(self.result_label)
        
        return self.main_layout

    def convert_to_fahrenheit(self, instance):
        try:
            celsius = float(self.input_celsius.text)
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.text = f"{celsius}°C = {fahrenheit}°F"
        except ValueError:
            self.result_label.text = "Por favor, insira um número válido!"

    def convert_to_celsius(self, instance):
        try:
            fahrenheit = float(self.input_fahrenheit.text)
            celsius = (fahrenheit - 32) * 5/9
            self.result_label.text = f"{fahrenheit}°F = {celsius}°C"
        except ValueError:
            self.result_label.text = "Por favor, insira um número válido!"

if __name__ == "__main__":
    ConverterApp().run()