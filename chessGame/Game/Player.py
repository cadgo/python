class Player(object):
    """
        Player object to interact
    """
    def __init__(self, PlayerName, color='white'):
        self.PlayerName = PlayerName
        self.Color = 'color'
        
    @property    
    def PlayerWin(self, win='no'):
        self.PlayerWin = win
