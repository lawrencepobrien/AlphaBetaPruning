# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:34:50 2023

@author: Lobri
"""

import sys
import tictactoe
import minimax
import alphabeta

def print_board(algo, board):
    if algo == 'a':
        score = minimax.minimax(True, board)
        
        if score == 1:
            print("Winner: Player 1")
        elif score == -1:
            print("Winner: Player 2")
        elif score == 0:
            print("Winner: Draw")
            
        print("Number of game tree nodes:", minimax.nodes_checked)
        
    elif algo == 'b':
        score = alphabeta.alpha_beta(True, float('inf'), -float('inf'), board)
        
        if score == 1:
            print("Winner: Player 1")
        elif score == -1:
            print("Winner: Player 2")
        elif score == 0:
            print("Winner: Draw")
            
        print("Number of game tree nodes:", alphabeta.nodes_checked)
        

if __name__ == "__main__":
    algo = sys.argv[1]
    board_state = sys.argv[2]
    
    state = []
    rows = board_state.split(',')
    
    for row in rows:
        true_row = row.strip()
        arr = true_row.split(' ')
        
        r = []
        for num in arr:
            r.append(int(num))
            
        state.append(r)
    
    board = tictactoe.board(state)
    
    print_board(algo, board)