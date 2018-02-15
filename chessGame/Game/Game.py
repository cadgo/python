from Player import GamePlayer
from enum import IntEnum

class TypeOfGame(IntEnum):
    VERSUS=1
    ONEVONE = 2
    COOP =3
    COMPVS = 4

class Game(object):
    def __init__(self, GameName):
        self.NameOfTheGame = GameName
        self.players = []
        self.GameVersion()
    
    def AddPlayer(self, PlayerName, Color):
        self.players.append(GamePlayer(PlayerName, Color))
    
    def GameVersion(self, Version=".1"):
        self.GameVersion = Version
    
    def SetScreenSize(self, widht = 0, height = 0):
        self.widht = widht
        self.height = height
        
    def SetTypeOfGame(self, Type= TypeOfGame.COMPVS):
        self.GameType = Type
                   
    def WhoWins(self, PlayerName):
        return self.players[PlayerName].PlayerName
    
    def GameStart(self):
        print(len(self.players))
        assert self.widht and self.height != 0, "Please Define the ScreenSize"
        assert self.GameType != None, "Please define the Type of Games"
        assert len(self.players) != 0, "At least one player needs to be playing"
        


if __name__ == "__main__":
    print('Hola')
    iGame = Game('Chess')
    iGame.SetScreenSize(100, 100)
    iGame.SetTypeOfGame(TypeOfGame.COMPVS)
    #iGame.AddPlayer("carlos", 'white')
    iGame.GameStart()
    
    
            