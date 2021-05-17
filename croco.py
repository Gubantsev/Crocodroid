from random import shuffle, choice

file = "desk_set.txt"
deck_name = """
Задание 0 уровня 0

Задание 1 уровня 0

Задание 2 уровня 0

Задание 3 уровня 0

Задание 4 уровня 0

Задание 5 уровня 0

Задание 6 уровня 0

Задание 7 уровня 0

Задание 8 уровня 0

Задание 9 уровня 0

next level

Задание 0 уровня 1

Задание 1 уровня 1

Задание 2 уровня 1

Задание 3 уровня 1

Задание 4 уровня 1

Задание 5 уровня 1

Задание 6 уровня 1

Задание 7 уровня 1

Задание 8 уровня 1

Задание 9 уровня 1

next level

Задание 0 уровня 2

Задание 1 уровня 2

Задание 2 уровня 2

Задание 3 уровня 2

Задание 4 уровня 2

Задание 5 уровня 2

Задание 6 уровня 2

Задание 7 уровня 2

Задание 8 уровня 2

Задание 9 уровня 2
    """

class Player:
    def __init__(self, name):
        self.player_id = 0
        self.sex = 0
        self.name = name


class Players:
    def __init__(self):
        self.players = []

    def new_player(self, name):
        self.players.append(Player(name))

    def get_rnd(self, player):
        p = self.players.copy()
        p.remove(self.players[player])
        pl = choice(p)
        return pl.name

    def create_players(self):
        print('\nКто будеть играть? (Пустое поле для завершения ввода)')
        while True:
            name = input('Введиете имя игрока: ')
            if name == '':
                print('В игре ' + str(len(self.players)) + ' игрока.\n')
                break
            self.players.append(Player(name))


class Deck:
    def __init__(self):
        self.cards = []
        self.max_level = 0
        self.build()

    def build(self):
        # f = open(file, 'r').read(-1)
        f = deck_name
        f_by_lvl = f.split('\n\nnext level\n\n')
        # print(len(f_by_lvl))
        self.max_level = len(f_by_lvl)
        for lvl in f_by_lvl:
            f_by_card = lvl.split('\n\n')
            for text in f_by_card:
                self.cards.append(Card(f_by_lvl.index(lvl), text))
            shuffle(self.cards)

    def count_cards_lvl(self, lvl):
        a = 0
        for card in self.cards:
            if card.level == lvl:
                a += 1
        return a

    def count_cards(self):
        a = len(self.cards)
        return a

    def get_card(self, lvl):
        curent_deck = [card for card in self.cards if card.level == lvl]
        card = curent_deck[-1]
        self.cards.remove(card)
        return card.text


class Card:
    def __init__(self, lvl, text):
        self.level = lvl
        self.text = text


def start():
    global level, turn, players
    turn = 1
    d = Deck()
    p = Players()
    print('Поиграем в Крокодил!!!\n')
    print('Задания загружены из файла: ' + file)
    print('\nДоступно уровней: ' + str(d.max_level))
    level = input('С какого уровня начнем? ')
    level = int(level) - 1
    p.create_players()
    game(d, p)


def get_card(d, p):
    global turn, level
    print('Ход №' + str(turn) + ', уровень: ' + str(level + 1))
    active_player = (turn % len(p.players))
    print('Игрок: ' + p.players[active_player].name)
    print('Угадывающий: ' + p.get_rnd(active_player) + '\n')
    print(d.get_card(level))
    turn += 1


def game(d, p):
    global level
    while True:
        if d.count_cards_lvl(level) == 0:
            if input('Все, карты этого уровня закончились, подять уровень? y/n ' + '\n') == 'n':
                print('Конец игры!')
                break
            level += 1
            if level >= d.max_level:
                print('Карт больше нет. Конец игры!')
                if input('Начнем с начала? y/n ') == 'y':
                    print('\n\n\n\n')
                    start()
                break
        get_card(d, p)
        choice = input('Вытягиваем следующий? y/n (up - поднять уровень) ')
        if choice == 'n':
            print('Конец игры!')
            break
        if choice == 'up':
            level += 1
            if level >= d.max_level:
                print('Успокойтесь, уровень уже максимальный!')
                level == d.max_level - 1
        print('\n')


if __name__ == '__main__':
    d = Deck()
    #print(d.get_card(1))
    start()
