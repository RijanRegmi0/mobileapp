from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import os

class MeroShare(App):

    def build(self):
        self.root = BoxLayout(orientation='vertical')

        # Header
        header = BoxLayout(size_hint=(1, None), height=100)
        header.add_widget(Label(text='Share', font_size=24))

        # Main content area
        main_layout = BoxLayout(orientation='horizontal')

        # Left side
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

        left_layout.add_widget(Label(text='Date', font_size=16))
        self.date_input = TextInput(multiline=False, font_size=16)
        left_layout.add_widget(self.date_input)

        members = ['Hari Regmi', 'Rijan Regmi', 'Anita Regmi', 'Rishav Regmi']
        self.member_inputs = {}
        for member in members:
            left_layout.add_widget(Label(text=member, font_size=16))
            self.member_inputs[member] = TextInput(multiline=False, font_size=16)
            left_layout.add_widget(self.member_inputs[member])

        # Buttons
        button_layout = BoxLayout(size_hint=(1, None), height=50)
        add_button = Button(text='Add', font_size=16)
        add_button.bind(on_press=self.add_share)
        save_button = Button(text='Save', font_size=16)
        save_button.bind(on_press=self.save_share)
        clear_button = Button(text='Clear', font_size=16)
        clear_button.bind(on_press=self.clear_share)
        button_layout.add_widget(add_button)
        button_layout.add_widget(save_button)
        button_layout.add_widget(clear_button)

        left_layout.add_widget(button_layout)

        main_layout.add_widget(left_layout)

        # Right side (scrollable)
        right_layout = ScrollView()

        self.text_area = TextInput(readonly=True, font_size=16)
        right_layout.add_widget(self.text_area)

        main_layout.add_widget(right_layout)

        self.root.add_widget(header)
        self.root.add_widget(main_layout)

        return self.root

    def add_share(self, instance):
        date = self.date_input.text
        members_data = [(member, self.member_inputs[member].text) for member in self.member_inputs]
        total_value = sum(float(data[1]) for data in members_data)

        share_info = f'\n Date: {date}\n____________________________________\n'
        for member, value in members_data:
            share_info += f'\t{member}\t\t{value}\n'
        share_info += '____________________________________\n'
        share_info += f'\tTotal\t\t{"%.2f" % total_value}\n'
        share_info += '____________________________________\n'

        self.text_area.text += share_info

    def save_share(self, instance):
        date = self.date_input.text
        share_info = self.text_area.text

        filename = f'share/{date}.txt'
        with open(filename, 'w') as file:
            file.write(share_info)

    def clear_share(self, instance):
        self.date_input.text = ''
        for member_input in self.member_inputs.values():
            member_input.text = ''
        self.text_area.text = ''


if __name__ == "__main__":
    MeroShare().run()



