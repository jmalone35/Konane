import math
from konane import *;

class MinimaxPlayer(Konane, Player): 
    
    def __init__(self, size, depthLimit):         
        Konane.__init__(self, size)         
        self.limit = depthLimit 
 
    def initialize(self, side):         
        self.side = side
        if side == "B":
            self.name = "KingOfGames1"
        else:
            self.name = "KingOfGames2"

    def eval(self, board):
        n = len(board)
        if n == 0:
            return (0)
        else:
            return (self.countSymbol(board, 'B'))

    def MiniMax(self, board, depth, maximizingPlayer):
        #return best move
        
        if (depth == 0 or self.generateMoves(board, self.side) == []):
            return (self.eval (board), [])
        
        if (maximizingPlayer):
            value = float('-inf')
            miniMaxBoard = board
            #Get all possible moves
            #Call max on each one with decramented depth        
            moves = self.generateMoves(board, self.side)
            if len(moves) == 0:
                return (-float('inf'), [])
            for move in moves:
                miniMaxMove = self.MiniMax(self.nextBoard(board, self.side, move), (depth - 1), False)
                if(value <= miniMaxMove[0]):
                    value = miniMaxMove[0]
                    miniMaxBoard = move 

            return (value, miniMaxBoard)
        else:
            otherSide = ''
            if(self.side == 'B'):
                otherSide = 'W'
            else:
                otherSide = 'B'
            value = float('inf')
            miniMaxBoard = board
            moves = self.generateMoves(board, otherSide)
            if len(moves) == 0:
                return (float('inf'), [])        
            for move in moves:
                miniMaxMove = self.MiniMax(self.nextBoard(board, otherSide, move), (depth - 1), True)
                if(value >= miniMaxMove[0]):
                    value = miniMaxMove[0]
                    miniMaxBoard  = move
            
            return (value, miniMaxBoard)      
    def getMove(self, board):
        return self.MiniMax(board, self.limit, True)[1]
        #complete this

   
        #complete this – thi
        # 
        # 
game = Konane(8)
game.playNGames(2, MinimaxPlayer(8,2), MinimaxPlayer(8,1), 0)  