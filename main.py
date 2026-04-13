from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import requests

class ChatApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Область сообщений
        self.scroll = ScrollView()
        self.chat_history = Label(text="Добро пожаловать в Zenith!\n", size_hint_y=None, halign='left', valign='top')
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        self.root.add_widget(self.scroll)

        # Поле ввода
        self.input_box = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.message_input = TextInput(hint_text="Введите сообщение...", multiline=False)
        self.send_btn = Button(text=">>", size_hint_x=None, width=70)
        self.send_btn.bind(on_release=self.send_message)
        
        self.input_box.add_widget(self.message_input)
        self.input_box.add_widget(self.send_btn)
        self.root.add_widget(self.input_box)

        # Обновляем чат каждые 3 секунды
        Clock.schedule_interval(self.get_messages, 3)
        return self.root

    def send_message(self, instance):
        msg = self.message_input.text
        if msg:
            try:
                # Отправляем на твой сервер Render
                requests.post("https://tegegrom-server.onrender.com/send", json={"text": msg})
                self.message_input.text = ""
            except:
                self.chat_history.text += "[Ошибка отправки]\n"

    def get_messages(self, dt):
        try:
            # Получаем сообщения с сервера
            r = requests.get("https://tegegrom-server.onrender.com/messages")
            if r.status_code == 200:
                data = r.json()
                # Просто выводим последние сообщения
                self.chat_history.text = "\n".join([f"Кто-то: {m['text']}" for m in data[-15:]])
        except:
            pass

if __name__ == '__main__':
    ChatApp().run()