from konane import *;

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit

    def initialize(self, side):
        Konane.initialize(self, side)
        if (side == "B"):
            self.name = "John"
        else:
            self.name = "Luke"
        
        #complete this
        
    def getMove(self, board):
        print("")
        #complete this

    def eval(self, board):
        print("")
        #complete this – this