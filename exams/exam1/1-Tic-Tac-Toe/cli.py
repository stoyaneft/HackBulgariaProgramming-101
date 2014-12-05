import os
import time

from game import Game, GameStatus, InvalidMoveError, Cell


class CLI:

    def __init__(self):
        self.game = Game()

    def play(self):
        while self.game._status == GameStatus.IN_PROGRESS:
            self._clear()
            self.draw_board()
            move_index = None
            while move_index is None:
                if self.game._player == Cell.X:
                    move_coords = self._get_move()
                    move_index = Game.calculate_index(move_coords)
                else:
                    move_index = self.game.get_computer_move()
                try:
                    self.game.play_move(move_index)
                except InvalidMoveError:
                    print('Invalid move!')
            if self.game._player == Cell.X:
                print('Computer played at {} {}'.format(
                    *Game.calculate_coords(move_index)))
            time.sleep(1)

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
