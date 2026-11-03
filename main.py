from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class AnimeOfficialApp(App):

    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.08, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="[b]ANIME OFFICIAL[/b]",
            markup=True,
            font_size=28,
            size_hint=(1, 0.2)
        )

        subtitle = Label(
            text="AI Photo & Video Editor",
            font_size=18,
            size_hint=(1, 0.1)
        )

        prompt = TextInput(
            hint_text="Andika icyo ushaka guhindura...",
            multiline=True,
            size_hint=(1, 0.3)
        )

        photo_button = Button(
            text="EDIT PHOTO",
            size_hint=(1, 0.15)
        )

        video_button = Button(
            text="EDIT VIDEO",
            size_hint=(1, 0.15)
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(prompt)
        layout.add_widget(photo_button)
        layout.add_widget(video_button)

        return layout


if __name__ == "__main__":
    AnimeOfficialApp().run()

        
