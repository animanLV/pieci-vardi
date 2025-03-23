from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WordApp(App):
    def build(self):
        self.words = self.load_words()
        self.index = 0
        self.layout = BoxLayout(orientation='vertical')
        self.word_label = Label(text=self.format_word(self.words[self.index]), font_size=32)
        self.next_btn = Button(text="Далее", size_hint=(1, 0.2))
        self.next_btn.bind(on_press=self.next_word)
        self.layout.add_widget(self.word_label)
        self.layout.add_widget(self.next_btn)
        return self.layout

    def load_words(self):
        with open("words.txt", encoding="utf-8") as f:
            return [line.strip().split(" - ") for line in f if " - " in line]

    def format_word(self, pair):
        return f"{pair[0]} - {pair[1]}"

    def next_word(self, instance):
        self.index = (self.index + 1) % len(self.words)
        self.word_label.text = self.format_word(self.words[self.index])

if __name__ == "__main__":
    WordApp().run()