# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:12:44 2023

@author: Lobri
"""

nodes_checked = 0
moves = []

def alpha_beta(maximize, beta, alpha, board):
    global nodes_checked
    global moves
    
    print(alpha, ', ', beta, ', ', maximize)
    
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
    
    best = 0
    
    if maximize:
        best = -float('inf')
    else:
        best = float('inf')
    
    moves = board.get_moves()
    for move in moves:
        board.make_move(move, user)
        
        score = alpha_beta(not maximize, beta, alpha, board)
        
        if maximize:
            best = max(best, score)
            alpha = max(alpha, best)
        else:
            best = min(best, score)
            beta = min(best, beta)
            
        board.undo(move)
        if beta <= alpha:
            break
            
    
    return best