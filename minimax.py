# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:33:05 2023

@author: Lobri
"""

class node:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data

nodes_checked = 0
states = []

def minimax(maximize, board):    
    global nodes_checked
    global moves
    
    nodes_checked += 1
    
    if board.is_draw():
        return 0
    elif board.is_over()[0]:
        ret = 1 if board.get_winner() == 1 else -1
        return ret
    
    user = 0
    if maximize:
        user = 1
    else:
        user = 2
    
    scores = []
    
    moves = board.get_moves()
    for move in moves:
        board.make_move(move, user)
        
        score = minimax(not maximize, board)
        
        scores.append(score)
        board.undo(move)

    rtn = max(scores) if maximize else min(scores)
    
    return rtn