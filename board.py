import pygame 

from config import *


class TicTacToe:
    def __init__(self, window, *players):
        window.fill(BACKGROUND_COLOR)
        self.window = window 

        cell_position_list = [(row, col) for row in range(3) for col in range(3)]
        self.cell_list = [Cell(window, *cell_pos) for cell_pos in cell_position_list]
        self.grid = Grid(window, self.cell_list)

        self.current_player, self.waiting_player = players

        self._is_done = False

    @property
    def is_done(self):
        return self._is_done

    @is_done.setter
    def is_done(self, done):
        self._is_done = done


    def winner(self):
        for i in range(3):
            if all([cell.letter == self.current_player.letter for cell in filter(lambda cell: cell.position.x == i * CELL_SIZE, self.cell_list)]): 
                pygame.draw.line(self.window, RED, (CELL_SIZE * i +  CELL_SIZE/2, 0 + PADDING), (CELL_SIZE * i + CELL_SIZE/2, 600 - PADDING), width = LINE_WIDTH) 
                pygame.display.flip()
                print("returned ")
                return True

            elif all([cell.letter == self.current_player.letter for cell in filter(lambda cell: cell.position.y == i * CELL_SIZE, self.cell_list)]): 
                pygame.draw.line(self.window, RED, (0 + PADDING, CELL_SIZE * i + CELL_SIZE/2), (600 - PADDING, CELL_SIZE * i + CELL_SIZE/2), width = LINE_WIDTH) 
                pygame.display.flip()
                return True 
                
            elif all([cell.letter == self.current_player.letter for cell in filter(lambda cell: [cell.position.x//CELL_SIZE, cell.position.y//CELL_SIZE] in [[0,0], [1,1], [2,2]], self.cell_list)]): 
                pygame.draw.line(self.window, RED, (0 + PADDING, 0 + PADDING), (600 - PADDING, 600 - PADDING), width = LINE_WIDTH) 
                pygame.display.flip()
                return True
                
            elif all([cell.letter == self.current_player.letter for cell in filter(lambda cell: [cell.position.x//CELL_SIZE, cell.position.y//CELL_SIZE] in [[2,0], [1,1], [0,2]], self.cell_list)]): 
                pygame.draw.line(self.window, RED, (0 + PADDING, 600 - PADDING), (600 - PADDING, 0 + PADDING), width = LINE_WIDTH) 
                pygame.display.flip()
                return True
                
        return False

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_done = True
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                
                cell = self.grid.click(position)

                self.grid.select(cell, self.current_player)
                if self.winner():
                        self._is_done = True
                        print(self.current_player.letter)
                        print(len(list(filter(lambda cell: cell.is_available, self.cell_list))))
                        break
                else: 
                    if self.grid.is_switch:
                        temp = self.current_player
                        self.current_player, self.waiting_player = self.waiting_player, temp
                        del temp
                        
                        self.grid.is_switch = False
                    
                if self.grid.is_full():
                    self._is_done = True


class Grid:
    def __init__(self, window, cell_list):
        self.window = window
        self.cell_list = cell_list
        self._is_switch = False
        self._draw()

    @property 
    def is_switch(self):
        return self._is_switch

    @is_switch.setter
    def is_switch(self, val):
        self._is_switch = val

    def _draw(self):
        for i in range(4): 
            pygame.draw.line(self.window, LINE_COLOR, (CELL_SIZE * i, 0 + PADDING), (CELL_SIZE * i, 600 - PADDING), width = LINE_WIDTH) 
            pygame.draw.line(self.window, LINE_COLOR, (0 + PADDING, CELL_SIZE * i), (600 - PADDING, CELL_SIZE * i), width = LINE_WIDTH) 
            pygame.display.flip()

    def click(self, pos):
        px, py = pos
        if 0 <= px and px <= BOARD_SIZE and 0 <= py and BOARD_SIZE >= py:
            px = px // CELL_SIZE
            py = py // CELL_SIZE
            return Position(x=px * CELL_SIZE, y=py * CELL_SIZE)
        return None 

    def select(self, selected_cell, player):
        for cell in self.cell_list:
            if cell.position == selected_cell and cell.is_available:
                cell.select(player.letter)
                self._is_switch = True
        
    def is_full(self):
        return True if all([not cell.is_available for cell in self.cell_list]) else False


class Cell:
    def __init__(self, window, row, col):
        self.window = window
        self.position = Position(x = row * CELL_SIZE, y = col * CELL_SIZE)
        self._is_available = True
        self.letter = None

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, val):
        self._is_available = val
    

    def _draw(self):
        if self.letter == Letter.CIRCLE:
            pygame.draw.circle(self.window, CIRCLE_COLOR, center = (self.position.x + CELL_SIZE/2, self.position.y + CELL_SIZE/2), 
            radius = CELL_SIZE/2 - PADDING, width = LINE_WIDTH)

        elif self.letter == Letter.CROSS:
            pygame.draw.line(self.window, CROSS_COLOR, start_pos=(self.position.x + PADDING, self.position.y + PADDING), 
            end_pos = (self.position.x + CELL_SIZE - PADDING, self.position.y + CELL_SIZE - PADDING), width = LINE_WIDTH)
            
            pygame.draw.line(self.window, CROSS_COLOR, start_pos=(self.position.x + PADDING , self.position.y + CELL_SIZE - PADDING), 
            end_pos = (self.position.x + CELL_SIZE - PADDING, self.position.y + PADDING), width = LINE_WIDTH)
        pygame.display.flip()

    def select(self, letter):
        self.letter = letter
        self._draw()
        self._is_available = False