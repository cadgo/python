import Player

class TypeOfGame():
    Type = ['Versus', '1v1', 'Cooperative']
    Winner = ['Player1', 'Player2','Computer']
class Game(TypeOfGame):
    def __init__(self):
        self.players = []
    
    def AddPlayer(self):
        self.players.append(Player("Player 1", "white"))
        self.players.append(Player("Player 2", "black"))
    
    def SetGameName(self, Name):
        self.GameName = Name
    
    def GameVersion(self, Version=".1"):
        self.GameVersion = Version
    
    def SetScreenSize(self, widht, height):
        self.widht = widht
        self.height = height
        
    def SetTypeOfGame(self, Type= '1v1'):
        if Type in self.Type:
            self.TypeOfGame = Type
        else:
            self.TypeOfGame = 'NewKindOfGame'
            
    def WhoWins(self, PlayerName):
        pass
            