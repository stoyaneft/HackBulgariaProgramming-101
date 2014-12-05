from game import Game
from command_parser import CommandParser


class CLI:

    def __init__(self):
        self.game = Game()
        self.command_parser = CommandParser()
        self.init_command_parser()
        print('Welcome to the "Do you even math?" game!')

    def init_command_parser(self):
        self.command_parser.add_command('start', self.start)
        self.command_parser.add_command('highscores', self.print_highscores)
        self.command_parser.add_command('exit', self.exit)

    def start_menu(self):
        print('''
Here are your options:
- start
- highscores
- exit''')
        command = input('?> ')
        self.command_parser.execute(command)

    def start(self):
        username = input('Enter your playername>')
        print('Welcome {}! Let the game begin!'.format(username))
        self.game.register(username)
        while not self.game.is_over:
            self.game.generate_new_question()
            print('Question #{}:'.format(self.game.level))
            print(self.game.get_expression_string())
            try:
                answer = int(input('?> '))
            except ValueError:
                print('Answer must be an integer!')
            if self.game.give_answer(answer):
                print('Correct')
            else:
                print('''Incorrect! Answer was {}. Ending game. You score is: {}'''.format(
                    self.game.get_answer(), self.game.get_score()))
                self.game.restart()
                self.start_menu()

    def print_highscores(self):
        print(self.game.get_highscores_string())
        self.start_menu()

    def exit(self):
        import sys
        sys.exit()

if __name__ == '__main__':
    CLI().start_menu()
