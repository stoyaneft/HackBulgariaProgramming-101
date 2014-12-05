from player import Player
from random import shuffle, randint
from connections import *
from sqlalchemy import desc


class Game:

    OPERATIONS = ['x', '^', '+', '-', '//']

    def __init__(self):
        Base.metadata.create_all(engine)
        self.__session = Session()
        self.__level = 0
        self.__expression = None
        self.__is_over = False
        self.username = None

    def generate_new_question(self):
        shuffle(self.OPERATIONS)
        operation = self.OPERATIONS[0]
        if operation == '^':
            second_arg = randint(0, 15)
            self.__expression = {'first_arg': 2, 'operation': '^',
                                 'second_arg': second_arg,
                                 'answer': 2 ** second_arg}
            self.__level += 1
            return
        elif operation == 'x':
            upper_bound = 20
        else:
            upper_bound = 100
        first_arg = randint(1, upper_bound)
        second_arg = randint(1, upper_bound)
        if operation == '+':
            answer = first_arg + second_arg
        elif operation == '-':
            answer = first_arg - second_arg
        elif operation == '//':
            second_arg = randint(2, 10)
            answer = first_arg // second_arg
        elif operation == 'x':
            answer = first_arg * second_arg
        expression = {'first_arg': first_arg, 'second_arg': second_arg,
                      'operation': operation, 'answer': answer}
        self.__expression = expression
        self.__level += 1

    def get_answer(self):
        return self.__expression['answer']

    @property
    def level(self):
        return self.__level

    @property
    def is_over(self):
        return self.__is_over

    def get_expression_string(self):
        return 'What is the answer to {first_arg} {operation} {second_arg}?'.format(**self.__expression)

    def give_answer(self, answer):
        if self.is_correct(answer):
            return True
        else:
            self.__is_over = True
            self._save_highscore()
            return False

    def is_correct(self, answer):
        return self.__expression['answer'] == answer

    def register(self, username):
        if not self.__session.query(Player).filter(
                Player.name == username).all():
            self.__session.add(Player(name=username))
            self.__session.commit()
        self.username = username

    def get_highscores_string(self):
        players = self.__session.query(
            Player).order_by(desc(Player.highscore)).limit(10).all()
        highscores_str = '\n'.join(
            '{}. {} with {} points'.format(
                i + 1, player.name, player.highscore)
            for i, player in enumerate(players))
        return highscores_str

    def get_score(self):
        return (self.__level - 1) ** 2

    def _save_highscore(self):
        current_highscore = self.__session.query(
            Player.highscore).filter(Player.name == self.username).one()[0]
        if current_highscore < self.get_score():
            self.__session.query(Player).filter(
                Player.name == self.username).update(
                {'highscore': self.get_score()})
            self.__session.commit()

    def restart(self):
        self.__is_over = False
        self.__level = 0
