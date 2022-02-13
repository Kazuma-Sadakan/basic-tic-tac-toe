import pygame 
from player import Human, Random
from config import *
from board import TicTacToe

def main():
    pygame.init()
    window = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
    pygame.display.set_caption("Tic Tac Toe")

    game = TicTacToe(window, Human(Letter.CIRCLE), Human(Letter.CROSS))

    while not game.is_done:
        game.run()

    pygame.quit()
    
if __name__ == "__main__":
    main()