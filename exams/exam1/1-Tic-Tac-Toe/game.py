from enum import Enum


class InvalidMoveError(Exception):
    pass


class Cell:
    X = 'X'
    O = 'O'
    EMPTY = " "


class GameStatus(Enum):
    PLAYER_WINS = 1
    COMPUTER_WINS = 2
    TIE = 3
    IN_PROGRESS = 4


class Game:
    ROWS_COUNT = 3
    COLS_COUNT = 3
    BOARD_CELLS_COUNT = ROWS_COUNT * COLS_COUNT
    WINNING_LINES = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self, board=None):
        self._board = board or [Cell.EMPTY] * self.BOARD_CELLS_COUNT
        self._player = Cell.X
        self._status = GameStatus.IN_PROGRESS

    @staticmethod
    def calculate_index(position):
        index = position[0] * Game.ROWS_COUNT + position[1]
        return index

    def is_valid_move(self, index):
        return index in range(9) and \
            self._board[index] == Cell.EMPTY and \
            self._status == GameStatus.IN_PROGRESS

    def _play_human_move(self, position):
        index = self.calculate_index(position)
        if not self.is_valid_move(index):
            raise InvalidMoveError("Invalid move!")
        self._board[index] = self._player

    def _change_player(self):
        if self._player == Cell.X:
            self._player = Cell.O
        else:
            self._player = Cell.X

    def _play_computer_move(self):
        if self._status == GameStatus.IN_PROGRESS:
            move_index = self._get_computer_move()
            self._board[move_index] = self._player

    def play_move(self, position=None):
        if self._player == Cell.X:
            self._play_human_move(position)
        else:
            self._play_computer_move()
        self._update_game_status()
        self._change_player()

    def _get_winner(self):
        for line in self.WINNING_LINES:
            line_cells = [self._board[i] for i in line]
            if all([cell == self._player for cell in line_cells]):
                return self._player

    def _update_game_status(self):
        winner = self._get_winner()
        if winner == Cell.X:
            self._status = GameStatus.PLAYER_WINS
        elif winner == Cell.O:
            self._status = GameStatus.COMPUTER_WINS
        elif all([cell != Cell.EMPTY for cell in self._board]):
            self._status = GameStatus.TIE
        else:
            self._status = GameStatus.IN_PROGRESS

    def get_board_string(self):
        rows = [' '.join(self._board[i: i + 3]) for i in (0, 3, 6)]
        return '\n'.join(rows)

    '''Medium-powered AI'''

    def _get_computer_move(self):
    # First, check if we can win in the next move
        for i in range(0, 9):
            board_copy = self._board[:]
            virtual_game = Game(board_copy)
            virtual_game._player = 'O'
            if virtual_game._board[i] == Cell.EMPTY:
                virtual_game._board[i] = Cell.O
                winner = virtual_game._get_winner()
                if winner == Cell.O:
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(0, 9):
            board_copy = self._board[:]
            virtual_game = Game(board_copy)
            virtual_game._player = 'X'
            if virtual_game._board[i] == Cell.EMPTY:
                virtual_game._board[i] = Cell.X
                winner = virtual_game._get_winner()
                if winner == Cell.X:
                    return i

        # Try to take the center, if it is free.
        if self._board[4] == Cell.EMPTY:
            return 4

        # Try to take one of the corners, if they are free.
        corners = [0, 2, 6, 8]
        for i in corners:
            if self._board[i] == Cell.EMPTY:
                return i

        sides = [1, 3, 5, 7]
        for i in sides:
            if self._board[i] == Cell.EMPTY:
                return i
