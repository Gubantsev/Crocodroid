from kivy.uix.screenmanager import Screen
from kivy.config import ConfigParser
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import IRightBodyTouch
import croco


# class NewPlayer(MDBoxLayout):
#     def grabText(self, inst):
#         pass
#         # name = self.ids.new_name.text
#         # print(name)
#         # self.dialog.dismiss()


class PlayersScreen(Screen):
    def add_player(self):
        name = self.ids.new_name
        GameScreen.p.new_player(name.text)
        print("1")
        self.ids.container.clear_widgets()
        for n in GameScreen.p.players:
            self.ids.container.add_widget(player_widget(text=n.name))
        self.ids.new_name.text = ""

    def dell_player(self):
        print("self.ids.container")

    # dialog = None

    # def closeDialog(self):
    #     self.dialog.dismiss()
    #
        # self.dialog.dismiss()
    #
    # def show_dialog(self):
    #     if not self.dialog:
    #         self.dialog = MDDialog(
    #             title="Create player",
    #             type='custom',
    #             content_cls=NewPlayer(),
    #             buttons=[MDFlatButton(text="CANCEL"),
    #                      MDFlatButton(text="ACCEPT",
    #                                   on_press=self.grabText())])
    #     self.dialog.open()

    def on_enter(self):
        self.ids.container.clear_widgets()
        for n in GameScreen.p.players:
            self.ids.container.add_widget(player_widget(text=n.name))
        # self.ids.container.add_widget(MDTextField(text="Имя нового игрока"))


class player_widget(OneLineListItem):
    pass
    # , on_release=print("Click!")

class SettingsScreen(Screen):
    pass


class GameScreen(Screen):

    turn_number = 0
    #names = ['Рената', 'Стас', 'Алена', 'Дима']
    p = croco.Players()
    #for n in names:
    #    p.new_player(n)
    d = croco.Deck()

    def on_enter(self):
        self.fant_text.text = 'New card'
        self.info_text.text = ""
        self.turn_number = 0

    def info_update(self):
        new_info_text = ('Turn №' + str(self.turn_number) +
                         '     Player: ' +
                         self.p.players[self.turn_number % len(self.p.players)].name)
        self.info_text.text = new_info_text

    def new_fant(self):
        self.turn_number += 1
        self.fant_text.text = self.d.get_card(1)
        self.info_update()


class MenuScreen(Screen):
    pass


class CrocodileApp(MDApp):
    def __init__(self, **kwargs):
        self.title = 'Crocodile'
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = 'Light'
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file('Crocodile.kv')


if __name__ == '__main__':
    CrocodileApp().run()
