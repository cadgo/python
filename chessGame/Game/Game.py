import Player

class TypeOfGame():
    Type = ['Versus', '1v1', 'Cooperative']
    Winner = ['Player1', 'Player2','Computer']
class Game(TypeOfGame):
    def __init__(self, GameName):
        self.NameOfTheGame = GameName
        self.players = []
        self.GameVersion()
    
    def AddPlayer(self, PlayerName, Color):
        self.players.append(Player(PlayerName, Color))
        #self.players.append(Player("Player 1", "white"))
        #self.players.append(Player("Player 2", "black"))
    
    def GameVersion(self, Version=".1"):
        self.GameVersion = Version
    
    def SetScreenSize(self, widht = 0, height = 0):
        self.widht = widht
        self.height = height
        
    def SetTypeOfGame(self, Type= '1v1'):
        if Type in self.Type:
            self.TypeOfGame = Type
        else:
            self.TypeOfGame = 'NewKindOfGame'
            
    def WhoWins(self, PlayerName):
        return self.players[PlayerName].PlayerName
    
    def GameStart(self):
        assert self.widht and self.height != 0, "Please Define the ScreenSize"
        assert self.TypeOfGame != None, "Please define the Type of Games"
        


if __name__ == "__main__":
    print('Hola')
    iGame = Game('Chess')
    
    
            