import sys
import unittest
sys.path.append("..")

from game import Game
from game import GameStatus


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def testGameStartWithEmptyBoard(self):
        self.assertListEqual(self.game._board, [' '] * 9)

    def testCalculateIndex(self):
        self.assertEqual(Game.calculate_index((2, 1)), 7)

    def testValidMove(self):
        self.assertTrue(self.game.is_valid_move(5))

    def testInvalidMoveOutsideBoard(self):
        self.assertFalse(self.game.is_valid_move(9))

    def testInvalidMoveOnOccupiedCell(self):
        self.game.play_move(2)
        self.assertFalse(self.game.is_valid_move(2))

    def assertGameStatus(self, expected_status):
        self.assertEqual(
            self.game._status,
            expected_status)

    def testGameInProgress(self):
        self.game._board = [
            'X', 'O', ' ',
            'X', 'X', ' ',
            ' ', 'O', ' ',
        ]
        self.game._update_game_status()
        self.assertGameStatus(GameStatus.IN_PROGRESS)

    def testVerticalWin(self):
        self.game._board = [
            'O', ' ', ' ',
            'O', ' ', ' ',
            'O', ' ', ' ',
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        self.assertGameStatus(GameStatus.COMPUTER_WINS)

    def testHorizontalWin(self):
        self.game._board = [
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            'X', 'X', 'X',
        ]
        self._player = 'X'
        self.game._update_game_status()
        self.assertGameStatus(GameStatus.PLAYER_WINS)

    def testDiagonalWin(self):
        self.game._board = [
            'O', ' ', ' ',
            ' ', 'O', ' ',
            ' ', ' ', 'O',
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        self.assertGameStatus(GameStatus.COMPUTER_WINS)

    def testForTie(self):
        self.game._board = [
            'O', 'X', 'X',
            'X', 'O', 'O',
            'O', 'X', 'X',
        ]
        self._player = 'O'
        self.game._update_game_status()
        self.assertGameStatus(GameStatus.TIE)

    def testPlayAMove(self):
        self.game.play_move(5)
        expected_board = [
            ' ', ' ', ' ',
            ' ', ' ', 'X',
            ' ', ' ', ' '
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testAIWinsIfCan(self):
        self.game._board = [
            'X', ' ', 'X',
            ' ', 'O', 'O',
            ' ', ' ', 'X'
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        move_index = self.game.get_computer_move()
        self.game.play_move(move_index)
        expected_board = [
            'X', ' ', 'X',
            'O', 'O', 'O',
            ' ', ' ', 'X'
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testAIBlocksHumanWin(self):
        self.game._board = [
            'X', 'X', ' ',
            ' ', 'O', ' ',
            ' ', ' ', ' '
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        move_index = self.game.get_computer_move()
        self.game.play_move(move_index)
        expected_board = [
            'X', 'X', 'O',
            ' ', 'O', ' ',
            ' ', ' ', ' '
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testAIOccupiesCenterIfEmpty(self):
        self.game._board = [
            'X', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        move_index = self.game.get_computer_move()
        self.game.play_move(move_index)
        expected_board = [
            'X', ' ', ' ',
            ' ', 'O', ' ',
            ' ', ' ', ' '
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testAIOccupiesCornerIfEmpty(self):
        self.game._board = [
            'X', ' ', ' ',
            ' ', 'O', ' ',
            ' ', ' ', 'X'
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        move_index = self.game.get_computer_move()
        self.game.play_move(move_index)
        expected_board = [
            'X', ' ', 'O',
            ' ', 'O', ' ',
            ' ', ' ', 'X'
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testAIOccupiesSideIfNoneOfAbove(self):
        self.game._board = [
            'X', 'X', 'O',
            'O', 'O', ' ',
            'X', ' ', 'X'
        ]
        self.game._player = 'O'
        self.game._update_game_status()
        move_index = self.game.get_computer_move()
        self.game.play_move(move_index)
        expected_board = [
            'X', 'X', 'O',
            'O', 'O', 'O',
            'X', ' ', 'X'
        ]
        self.assertListEqual(self.game._board, expected_board)

    def testGetBoardString(self):
        self.game._board = [
            'X', 'O', ' ',
            ' ', 'X', ' ',
            ' ', ' ', ' '
        ]
        expected_board_string = 'X O  \n  X  \n     '
        self.assertEqual(self.game.get_board_string(), expected_board_string)

if __name__ == '__main__':
    unittest.main()
