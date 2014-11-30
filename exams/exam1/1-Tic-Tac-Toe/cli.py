import os
import time

from game import Game, GameStatus, InvalidMoveError


class CLI:

    def __init__(self):
        self.game = Game()

    def play(self):
        while self.game._status == GameStatus.IN_PROGRESS:
            self._clear()
            self.draw_board()
            if self.game._player == 'X':
                move = None
                while move is None:
                    move = self._get_move()
                try:
                    self.game.play_move(move)
                except InvalidMoveError:
                    print('Invalid move!')
                    time.sleep(1)
            else:
                move = self.game._get_computer_move()
                self.game.play_move()
                print('Computer played at {} {}'.format(move // 3, move % 3))
                time.sleep(1.5)

        self._clear()
        self.draw_board()
        status = self.game._status
        if status == GameStatus.PLAYER_WINS:
            print('Congratulations! You win!')
        elif status == GameStatus.COMPUTER_WINS:
            print('Computer wins!')
        else:
            print("It's a tie!")

    def draw_board(self):
        print(self.game.get_board_string())

    def _get_move(self):
        move = input("It's your turn. Play your move: <row col>")
        try:
            position = tuple(map(int, move.split(' ')))
            return position
        except ValueError:
            print("Enter move in the right format")
            return None

    def _clear(self):
        os.system('clear')

if __name__ == '__main__':
    CLI().play()
