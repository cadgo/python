import pygame
from random import randint
from copy import deepcopy

global_screen_width = 400
global_screen_heigth = 600
TetrisWidht = 8
TetrisHeight = 18
FigureFalling = False

class TetrisGrid():

    def __init__(self, window, Matrix_Widht, Matrix_Height):
        self.win = window
        self.Matrix_Width = Matrix_Widht
        self.Matrix_Hiegth = Matrix_Height
        self.grid = [[0 for x in range(self.Matrix_Hiegth)] for y in range(self.Matrix_Hiegth)]
        self.CFigure = None

    def ResetGrid(self, fill):
        self.grid = [[fill for x in range(self.Matrix_Hiegth)] for y in range(self.Matrix_Hiegth)]

    def UpdateFigure(self, movement = 'Down'):
        global FigureFalling
        newposition = []
        print('movement ', movement)
        cc=None
        #value = self.CFigure.CurrPosition[self.C   Figure.FiGLength-1][0])
        if movement == 'Down':
            value = self.CFigure.CurrPosition[-1][0]
            if value < self.Matrix_Hiegth-1:
                for ex in range(len(self.CFigure.CurrPosition)):
                    #print("ex", ex, "figure", self.CFigure.CurrPosition)
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                    #Una vez que se borra la figura anterior se usa current position mas 1 para actualizar la figura
                for ex in range(len(self.CFigure.CurrPosition)):
                    if self.grid[self.CFigure.CurrPosition[ex][0]+1][self.CFigure.CurrPosition[ex][1]] != 1:
                        newposition.append([self.CFigure.CurrPosition[ex][0]+1,self.CFigure.CurrPosition[ex][1]])
                    else:   cc = 1
                if cc != 1:
                    self.CFigure.CurrPosition = newposition
                else:
                    FigureFalling = False
                for ex in range(len(self.CFigure.CurrPosition)):
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 1
                #print("New Position", newposition)
            else:
                print("Deja de Caer")
                FigureFalling = False
        if movement == 'left':
            print("movemos a la izq")
            print("Current figure ", self.CFigure.CurrPosition)
            for ex in range(len(self.CFigure.CurrPosition)):
                # print("ex", ex, "figure", self.CFigure.CurrPosition)
                self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                # Una vez que se borra la figura anterior se usa current position mas 1 para actualizar la figura
            for ex in range(len(self.CFigure.CurrPosition)):
                if self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]-1] != 1:
                    newposition.append([self.CFigure.CurrPosition[ex][0], self.CFigure.CurrPosition[ex][1]-1])
            print("newposition ", newposition)
            self.CFigure.CurrPosition = newposition
            for ex in range(len(self.CFigure.CurrPosition)):
                self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 1
        if movement == 'right':
            print("Movemos a la derecha")
            print("Current figure ", self.CFigure.CurrPosition)
            for ex in range(len(self.CFigure.CurrPosition)):
                # print("ex", ex, "figure", self.CFigure.CurrPosition)
                self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                # Una vez que se borra la figura anterior se usa current position mas 1 para actualizar la figura
            for ex in range(len(self.CFigure.CurrPosition)):
                if self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]+1] != 1:
                    newposition.append([self.CFigure.CurrPosition[ex][0], self.CFigure.CurrPosition[ex][1]+1])
            print("newposition ", newposition)
            self.CFigure.CurrPosition = newposition
            for ex in range(len(self.CFigure.CurrPosition)):
                self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 1

    def __FigChooser(self):
        cf = {0: Square(), 1: ZBar(), 2: Bar(), 3: LBar()}
        return cf[randint(0,len(cf)-1)]


    def StartFigure(self):
        """Pedir una figura de forma aleatoria"""
        self.CFigure = self.__FigChooser()
        x = 0
        y = int(TetrisWidht/2)-1
        self.CFigure.CurrPosition = []
        for a in range(self.CFigure.FiGLength):
            for b in range(len(self.CFigure.MFigure[a])):
                if self.CFigure.MFigure[a][b] == 1:
                    if self.grid[a+x][b+y] != 1:
                        self.grid[a+x][b+y] = 1
                        self.CFigure.CurrPosition.append([a+x, b+y])
                    else:
                        print("Game Over")
                        pygame.time.delay(3000)
                        pygame.quit()
                    #print(self.CFigure.CurrPosition)

    def UpdateFigureGrid(self, update_matrix):
        for ex in range(len(update_matrix)):
            if self.grid[update_matrix[ex][0]][update_matrix[ex][1]] == 0:
                self.grid[update_matrix[ex][0]][update_matrix[ex][1]] = 1

    def UpdateGrid(self, screen_widht, screen_heigth):
        x = y = 0
        paddingwith = screen_widht / self.Matrix_Width
        paddingheight = screen_heigth / self.Matrix_Hiegth
        for b in range(self.Matrix_Width):
            for a in range(self.Matrix_Hiegth):
                if self.grid[a][b] == 0:
                    pygame.draw.rect(self.win, (255, 255, 255), (x, y, paddingwith, paddingheight), 3)
                else:
                    pygame.draw.rect(self.win, (255, 255, 0), (x, y, paddingwith, paddingheight))
                y = y + paddingheight
            x = x + paddingwith
            y = 0


    def GetTetrisWidth(self):
        return self.Matrix_Width

    def GetTetrisHeight(self):
        return self.Matrix_Hiegth

class Figure():
    FigureName = None
    CurrPosition = []
    def __init__(self):
        self.MFigure = [] #Una matriz bidemensional con la figura
        self.FiGLength = len(self.MFigure)

    def initalPosition(self, Matrix_Width, Matrix_Heigth):
        """Definimos la posicion incial"""

    def TurnLeft(self):
        """Turn Left"""


    def TurnRigth(self):
        """Turn UP"""
        piece_copy = deepcopy(self.CurrPosition)
        reverse_piece = piece_copy[::-1]
        print(reverse_piece)
        self.CurrPosition = reverse_piece


class Square(Figure):
    FigureName = "square"

    def __init__(self):
        self.MFigure = [[1,1],
                        [1,1]]
        self.FiGLength = len(self.MFigure)

    def TurnLeft(self):
        return

    def TurnRigth(self):
        return

class ZBar(Figure):
    FigureName = "zbar"

    def __init__(self):
        self.MFigure = [[1,0],
                        [1,1],
                        [0,1]]
        self.FiGLength = len(self.MFigure)

class Bar(Figure):
    FigureName = "bar"

    def __init__(self):
        self.MFigure = [[1],
                        [1],
                        [1],
                        [1]]
        self.FiGLength = len(self.MFigure)

class LBar(Figure):
    FigureName = "Lbar"

    def __init__(self):
        self.MFigure = [[1],
                        [1],
                        [1],
                        [1,1]]
        self.FiGLength = len(self.MFigure)

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((global_screen_width, global_screen_heigth))
    Grid = TetrisGrid(win,TetrisWidht, TetrisHeight)
    GameRuning = True
    move = "down"

    while(GameRuning):
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameRuning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("presionamos a")
                    move = 'left'
                if event.key == pygame.K_d:
                    move = 'right'
                    print("presionamos d")
                if event.key == pygame.K_w:
                    print('rotate')
                    print(Grid.CFigure.CurrPosition)
                    print(Grid.CFigure.TurnRigth())
        if FigureFalling == False:
            Grid.StartFigure()
            FigureFalling = True
        elif FigureFalling == True:
            #La figura cae hay que moverla a abajo
            pygame.time.delay(1000)
            if move == 'left':
                Grid.UpdateFigure(move)
                move = "down"
            elif move == 'right':
                Grid.UpdateFigure(move)
                move = "down"
            elif move == 'down':
                Grid.UpdateFigure()
                move='down'
        Grid.UpdateGrid(global_screen_width, global_screen_heigth)
        pygame.display.update()

    pygame.quit()
