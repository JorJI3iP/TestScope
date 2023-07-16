from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen


class Root(MDScreen):
    pass


class SquareIconButton(MDRaisedButton):
    right_icon = StringProperty('')
    left_icon = StringProperty('')
    label_text = StringProperty('')

class Test(MDApp):
    def build(self):
        # Создаём экземпляр корневого класса
        root = Root()
        self.theme_cls.theme_style = "Dark"  # "Light" Тёмная или Светлая тема
        self.theme_cls.primary_palette = 'LightGreen'  # Цвет темы
        self.theme_cls.primary_hue = '500'  # Сочность цвета темы
        return root


Test().run()  # Запуск приложения