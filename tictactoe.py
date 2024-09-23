# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:46:18 2023

@author: Lobri
"""

class board:
    
    def __init__(self, board_state):
        self.state = board_state
    
    def get_winner(self):
        if self.is_over()[0]:
            return self.is_over()[1]
    
    def is_over(self):
        
        for i in range(len(self.state)):
            row = self.state[i]
            place_state = row[0]
            if place_state != 0:
                if row[1] == place_state and row[2] == place_state:
                    return True, place_state
                
            col = []
            for j in range(len(self.state[i])):
                col.append(self.state[j][i])
            
            place_state = col[0]
            if place_state != 0:
                if col[1] == place_state and col[2] == place_state:
                    return True, place_state
                
        place_state = self.state[0][0]
        if place_state != 0:
            if self.state[1][1] == place_state and self.state[2][2] == place_state:
                return True, place_state
            
        place_state = self.state[0][2]
        if place_state != 0:
            if self.state[1][1] == place_state and self.state[2][0] == place_state:
                return True, place_state
            
        return False, None
    
    def is_draw(self): 
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    return False
                
        return True
                        
        
    def get_moves(self):
        
        moves = []
        
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    moves.append([i, j])
                    
        return moves
    
    def get_state(self):
        return self.state
    
    def make_move(self, move, user):
        self.state[move[0]][move[1]] = user
        
    def undo(self, move):
        self.state[move[0]][move[1]] = 0