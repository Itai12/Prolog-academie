import pygame

from copy import deepcopy

from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.queen import Queen
from classes.rook import Rook

from GUI.board import Board
from GUI.game import Game

unit = 140

if __name__ == "__main__":

    pygame.init()

    board = Board(unit)
    board.display()
    game = Game(board)
    game.launchGame()
