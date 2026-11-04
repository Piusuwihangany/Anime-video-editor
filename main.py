
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class AnimeOfficialAI(App):

    def build(self):
        Window.clearcolor = get_color_from_hex("#101522")

        root = BoxLayout(
            orientation="vertical",
            padding=18,
            spacing=14
        )

        title = Label(
            text="[b]ANIME OFFICIAL AI[/b]",
            markup=True,
            font_size="25sp",
            color=get_color_from_hex("#FFFFFF"),
            size_hint_y=None,
            height=65
        )
        root.add_widget(title)

        subtitle = Label(
            text="AI Photo • Video • Logo Editor",
            font_size="15sp",
            color=get_color_from_hex("#B9C5D8"),
            size_hint_y=None,
            height=35
        )
        root.add_widget(subtitle)

        self.prompt = TextInput(
            hint_text="Andika icyo ushaka ko AI igukorera...",
            multiline=True,
            size_hint_y=None,
            height=120,
            background_color=get_color_from_hex("#202B3D"),
            foreground_color=get_color_from_hex("#FFFFFF"),
            hint_text_color=get_color_from_hex("#AAB5C5"),
            padding=12
        )
        root.add_widget(self.prompt)

        self.result = Label(
            text="Murakaza neza muri Anime Official AI!",
            color=get_color_from_hex("#FFFFFF"),
            halign="left",
            valign="top",
            size_hint_y=None
        )
        self.result.bind(
            width=lambda instance, width:
            setattr(instance, "text_size", (width, None))
        )
        self.result.bind(
            texture_size=lambda instance, size:
            setattr(instance, "height", size[1] + 20)
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)
        root.add_widget(scroll)

        actions = [
            ("EDIT PHOTO", self.photo_action),
            ("EDIT VIDEO", self.video_action),
            ("CREATE LOGO", self.logo_action),
            ("SEND PROMPT", self.send_prompt)
        ]

        for caption, action in actions:
            button = Button(
                text=caption,
                size_hint_y=None,
                height=52,
                background_normal="",
                background_color=get_color_from_hex("#1769AA"),
                color=get_color_from_hex("#FFFFFF)
            )
            button.bind(on_release=action)
            root.add_widget(button)

        return root

    def photo_action(self, instance):
        self.show_message("Photo editing izashyirwamo.")

    def video_action(self, instance):
        self.show_message("Video editing izashyirwamo.")

    def logo_action(self, instance):
        self.show_message("Logo creation izashyirwamo.")

    def send_prompt(self, instance):
        prompt = self.prompt.text.strip()

        if not prompt:
            self.show_message("Banza wandike icyo ushaka.")
            return

        self.show_message(
            "Icyifuzo cyawe:\n" + prompt +
            "\n\nAI service ntirahuza na porogaramu."
        )

    def show_message(self, message):
        self.result.text = message


if __name__ == "__main__":
    AnimeOfficialAI().run()
  
