import pygame

global_screen_width = 400
global_screen_heigth = 600
TetrisWidht = 8
TetrisHeight = 18

class TetrisGrid():

    def __init__(self, window, Matrix_Widht, Matrix_Height):
        self.win = window
        self.Matrix_Width = Matrix_Widht
        self.Matrix_Hiegth = Matrix_Height
        self.grid = [[0 for x in range(self.Matrix_Hiegth)] for y in range(self.Matrix_Hiegth)]
        self.CFigure = None

    def ResetGrid(self, fill):
        self.grid = [[fill for x in range(self.Matrix_Hiegth)] for y in range(self.Matrix_Hiegth)]

    def RequestFigure(self, xx, yy):
        """Pedir una figura de forma aleatoria"""
        self.CFigure = Square()
        x = xx
        y = yy-1
        for a in range(self.CFigure.FiGLength):
            for b in range(len(self.CFigure.MFigure[a])):
                print(self.CFigure.MFigure[a][b])
                if self.CFigure.MFigure[a][b] == 1:
                    self.grid[a+x][b+y] = 1


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

    def __init__(self):
        self.MFigure = [] #Una matriz bidemensional con la figura
        self.FiGLength = len(self.MFigure)

    def initalPosition(self, Matrix_Width, Matrix_Heigth):
        """Definimos la posicion incial"""

    def TurnLeft(self):
        """Turn Left"""

    def TurnUp(self):
        """Turn UP"""

class Square(Figure):
    FigureName = "square"

    def __init__(self):
        self.MFigure = [[1,1],
                        [1,1]]
        self.FiGLength = len(self.MFigure)

class ZBar(Figure):
    FigureName = "zbar"

    def __init__(self):
        self.MFigure = [[1,0],
                        [1,1],
                        [0,1]]
        self.FiGLength = len(self.MFigure)


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((global_screen_width, global_screen_heigth))
    Grid = TetrisGrid(win,TetrisWidht, TetrisHeight)
    GameRuning = True
    FigureFalling = False
    while(GameRuning):
        win.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameRuning = False
        if FigureFalling == False:
            Grid.RequestFigure(0,int(TetrisWidht/2))
            FigureFalling = True
        Grid.UpdateGrid(global_screen_width, global_screen_heigth)
        pygame.display.update()

    pygame.quit()
