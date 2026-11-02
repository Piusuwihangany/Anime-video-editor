
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 15
    spacing: 12

    Label:
        text: "[b]ANIME OFFICIAL AI[/b]"
        markup: True
        font_size: "26sp"
        size_hint_y: None
        height: "65dp"

    Label:
        text: "Your AI Photo and Video Editor"
        font_size: "16sp"
        size_hint_y: None
        height: "40dp"

    TextInput:
        id: prompt
        hint_text: "Andika icyo ushaka gukora..."
        multiline: True

    Button:
        text: "GENERATE"
        size_hint_y: None
        height: "55dp"
        on_release: app.generate()

    Button:
        text: "PHOTO EDITOR"
        size_hint_y: None
        height: "50dp"
        on_release: app.message("Photo editor izongerwamo.")

    Button:
        text: "VIDEO EDITOR"
        size_hint_y: None
        height: "50dp"
        on_release: app.message("Video editor izongerwamo.")

    Label:
        id: result
        text: "Welcome to Anime Official AI"
"""

class AnimeOfficial(App):
    def build(self):
        return Builder.load_string(KV)

    def generate(self):
        prompt = self.root.ids.prompt.text.strip()
        if not prompt:
            self.message("Banza wandike icyo ushaka.")
        else:
            self.root.ids.result.text = (
                "Prompt yawe yakiriwe. AI generation "
                "ntirahuza na server."
            )

    def message(self, text):
        Popup(
            title="Anime Official",
            content=Label(text=text),
            size_hint=(0.85, 0.35)
        ).open()

AnimeOfficial().run()
