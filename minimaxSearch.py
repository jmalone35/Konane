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
    def MiniMax(self, board, depth, maximizingPlayer):
        #return best move
        if (depth == 0 or self.generateMoves(board, self.side) == []):
            return self.eval (board)
        
        if (maximizingPlayer):
            value = float('-inf')
            miniMaxBoard = board
            #Get all possible moves
            #Call max on each one with decramented depth
            moves = self.generateMoves(board, self.side)
            for move in moves:
                miniMaxMove = self.MiniMax(move, (depth - 1), False)
                if(value < miniMaxMove[0]):
                    value = miniMaxMove[0]
                    MiniMaxBoard = miniMaxMove[1] 

            return (value, MiniMaxBoard)
        else:
            value = float('inf')
            miniMaxBoard = board
            moves = self.generateMoves(board, self.side)
            for move in moves:
                miniMaxMove = self.MiniMax(move, (depth - 1), True)
                if(value > miniMaxMove[0]):
                    value = miniMaxMove[0]
                    miniMaxBoard  = miniMaxMove[1] 
            
            return (value, MiniMaxBoard)      
    def getMove(self, board):
        return self.MiniMax(board, self.limit, True)[1]
        #complete this

    def eval(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        if n == 0:
            return (0, [])
        else:
            return (1, moves[0])
        #complete this – thi  