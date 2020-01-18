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

    def UpdateFigure(self, movement = 'Down', newmatrix=None):
        global FigureFalling
        newposition = []
        #print('movement ', movement)
        cc=None
        #print(self.CFigure.CurrPosition)
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
                FigureFalling = False
        if movement == 'left':
            print("movemos a la izq")
            #print("Current figure ", self.CFigure.CurrPosition)
            s = min(self.CFigure.CurrPosition)
            print("@@@SSSSS@@@ ", s)
            if s[1] > 0:
                for ex in range(len(self.CFigure.CurrPosition)):
                    # print("ex", ex, "figure", self.CFigure.CurrPosition)
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                    # Una vez que se borra la figura anterior se usa current position mas 1 para actualizar la figura
                for ex in range(len(self.CFigure.CurrPosition)):
                    if self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]-1] != 1:
                        newposition.append([self.CFigure.CurrPosition[ex][0], self.CFigure.CurrPosition[ex][1]-1])
                    else:
                        newposition = self.CFigure.CurrPosition
                        break
                print("newposition ", newposition)
                self.CFigure.CurrPosition = newposition
                for ex in range(len(self.CFigure.CurrPosition)):
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 1
        if movement == 'right':
            s = max(self.CFigure.CurrPosition)
            if s[1] < TetrisWidht-1:
                for ex in range(len(self.CFigure.CurrPosition)):
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                for ex in range(len(self.CFigure.CurrPosition)):
                    if self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]+1] != 1:
                        newposition.append([self.CFigure.CurrPosition[ex][0], self.CFigure.CurrPosition[ex][1]+1])
                    else:
                        newposition = self.CFigure.CurrPosition
                        break
                print("newposition ", newposition)
                self.CFigure.CurrPosition = newposition
                for ex in range(len(self.CFigure.CurrPosition)):
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 1
        if movement == 'rleft' and nm != None:
            s0=min(nm)
            s1=max(nm)
            print("rotamos a la izq")
            n= None
            if s1[1] < TetrisWidht or s0[1] > 0:
                for ex in range(len(self.CFigure.CurrPosition)):
                    self.grid[self.CFigure.CurrPosition[ex][0]][self.CFigure.CurrPosition[ex][1]] = 0
                for ex in range(len(nm)):
                    if self.grid[nm[ex][0]][nm[ex][1]] == 1:
                        n = 1
                if n != 1:
                    self.CFigure.CurrPosition=nm

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
    pivot = None

    def __init__(self):
        self.MFigure = [] #Una matriz bidemensional con la figura
        self.FiGLength = len(self.MFigure)

    def initalPosition(self, Matrix_Width, Matrix_Heigth):
        """Definimos la posicion incial"""

    def TurnLeft(self):
        """Turn Left"""
        print("Current position ", self.CurrPosition)
        p = self.CurrPosition[self.pivot]
        print("Obtenemos pivote y[{}] x[{}]".format(p[0], p[1]))
        rm = []
        for f in range(len(self.CurrPosition)):
            if f != self.pivot:
                x2 = self.CurrPosition[f][0] + p[1] - p[0]
                y2 = p[1] + p[0] - self.CurrPosition[f][1]
                rm.append([y2,x2])
            else:
                rm.append(self.CurrPosition[f])
        print("RM", rm)
        return rm


    def TurnRigth(self):
        """Turn UP"""
        piece_copy = deepcopy(self.CurrPosition)
        reverse_piece = piece_copy[::-1]
        print(reverse_piece)
        self.CurrPosition = reverse_piece


class Square(Figure):
    FigureName = "square"
    pivot = 0

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
    pivot = 1

    def __init__(self):
        self.MFigure = [[1,0],
                        [1,1],
                        [0,1]]
        self.FiGLength = len(self.MFigure)

class Bar(Figure):
    FigureName = "bar"
    pivot = 1

    def __init__(self):
        self.MFigure = [[1],
                        [1],
                        [1],
                        [1]]
        self.FiGLength = len(self.MFigure)

class LBar(Figure):
    FigureName = "Lbar"
    pivot = 1

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
                    nm = Grid.CFigure.TurnLeft()
                    move = 'rleft'
        if FigureFalling == False:
            Grid.StartFigure()
            FigureFalling = True
        elif FigureFalling == True:
            #La figura cae hay que moverla a abajo
            pygame.time.delay(600)
            if move == 'left':
                Grid.UpdateFigure(move)
                move = "down"
            elif move == 'right':
                Grid.UpdateFigure(move)
                move = "down"
            elif move == 'down':
                Grid.UpdateFigure()
                move='down'
            elif move == 'rleft':
                Grid.UpdateFigure(move,nm)
                move='down'
        Grid.UpdateGrid(global_screen_width, global_screen_heigth)
        pygame.display.update()

    pygame.quit()
