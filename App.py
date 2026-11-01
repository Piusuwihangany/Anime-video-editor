
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class AnimeOfficialAI(App):

    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.12, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="[b]ANIME OFFICIAL AI[/b]",
            markup=True,
            font_size="28sp",
            size_hint_y=None,
            height=70
        )
        layout.add_widget(title)

        subtitle = Label(
            text="Your AI Photo & Video Editor",
            font_size="16sp",
            size_hint_y=None,
            height=40
        )
        layout.add_widget(subtitle)

        self.prompt = TextInput(
            hint_text="Andika icyo ushaka guhindura...",
            multiline=True,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.prompt)

        for name in [
            "Hindura Ifoto",
            "Hindura Video",
            "Kora Logo",
            "Koresha Ijwi"
        ]:
            btn = Button(
                text=name,
                font_size="18sp",
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=self.select_action)
            layout.add_widget(btn)

        self.status = Label(
            text="Murakaza neza kuri Anime Official AI",
            size_hint_y=None,
            height=60
        )
        layout.add_widget(self.status)

        return layout

    def select_action(self, instance):
        self.status.text = (
            instance.text + " - Turimo gutegura iki gikorwa."
        )

AnimeOfficialAI().run()
      
