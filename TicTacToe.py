#%%
#Step 1: Function to display the board

from IPython.display import clear_output
clear_board = '\n*100'
clear_board
    
    # '\n*100' clears board. In jupyter notebook,
    #the method clear_board() does the same

def display_board(board):
    
    print(board[7]+' |',board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' |',board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' |',board[2]+' | '+board[3])

# test if board displaying works

test_board = ['#','1','2','3','4','5','6','7','8','9']

display_board(test_board)

#%%
# Step 2: Function to ask players for marker (X or O)

def player_input():
    '''
    OUTPUT = {'Player 1': Player 1 marker, 'Player 2': Player 2 marker}
    '''
    print('Hello, this is Tic Tac Toe.')
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
     
    if marker == 'X':
        return markers = {'Player 1': 'X','Player 2': 'O'}
    
    else:
        return markers = {'Player 1': 'O', 'Player 2': 'X'}
        
    
#%%  
#test
player_input()
return tuple(markers.values())

#%%
# Step 3: Function to position marker on board

def place_marker(board, marker, position):
    int(input(print(f'{choose_first()} begins! Press the corresponding number on your num pad to set your marker on the Tic Tac Toe Board:')))
    board[position] = marker

#%%
#test
place_marker(test_board, 'T', 4)
display_board(test_board)

#%%
# Step 4: Function to take in marker input and test if a player has won
def win_check(board,marker):
    
    if ((board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker) or
    (board[1] == marker and board[5] == marker and board[9] == marker) or
    (board[7] == marker and board[5] == marker and board[3] == marker)):
        
        #alternative:
        #str = ''
        #str.join(board[4,5,6]) == marker*3
        #str.join(board[7,8,9]) == marker*3
        
        print(f'Congratulations! {markers.key('marker')} wins!')
        break

#%%
#test
win_check(test_board,'T')

#%%
# Step 5: Function to pick player that starts

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#%%
# Step 6: Check if there is an open space on the board

def space_check(board, position):
    
    return board[position] == ' '

#%%
# Step 7: Check if board is full

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
        
#%%
# Step 8: Ask for position input and check if position is free

def player_choice(board):
    
    position = 0
    
    while position not in list(range(1,10)) or not space_check(board, position):
        position = int(input('Choose your next position (1-9): ')) 
        
    return position

#%%    
#test
player_choice(test_board)

#%%
# Step 9: Ask for replay

def replay():
    
    return input('Do you want to play again? [yes/no]').lower().startswith('y')

#%%
# Step 10: Put functions together to run the game 

def play_TicTacToe()
    
    empty_board = ['#','','','','','','','','','']
    # Step 7
    while game_ongoing == True:
         # Step1   
         display_board(empty_board)
         # Step 2
         player_input()
         # Step 5
         print(f'{choose_first()} begins! Choose your position: ')
         # Step 3   
         place_marker(empty_board, marker, position)
         # Steps 8 and 6
         player_choice(empty_board)         
         # Step 4
         if win_check(empty_board,marker):

    else:
        # Step 7
        if full_board_check(board):
             print("It's a tie!") 

    # Step 9
    if replay() == 'y':
        clear_board
        









         








#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%
board = ['#',''*9]

while board[position] == ' ' #len(test_board) < 11:
    
    player1_input = int(input('Press the corresponding number on your num pad to set your marker on the Tic Tac Toe Board (see board image below):'))
    player2_input = int(input('Press the corresponding number on your num pad to set your marker on the Tic Tac Toe Board (see board image below):'))        
    display_board(test_board)
    
    
    if board[player1_input] != ''
        
        board[player1_input] = player1_marker
        '\n*100'
        display_board(board)
        continue
     
    if board[player2_input] != ''
    
        board[player2_input] = player2_marker
        '\n*100'
        display_board(board)
        continue
    
    # check if a player has won
    
    if board[1] = board[2] == board[3] == marker or 
    board[4] = board[5] == board[6] == marker or
    board[7] = board[8] == board[9] == marker or
    board[1] = board[4] == board[7] == marker or
    board[2] = board[5] == board[8] == marker or
    board[3] = board[6] == board[9] == marker or
    board[1] = board[5] == board[9] == marker or
    board[7] = board[5] == board[3] == marker:
        
        #alternative:
        #str = ''
        #str.join(board[4,5,6]) == player1_marker*3
        #str.join(board[7,8,9]) == player1_marker*3
        
        print(f'Congratulations! {}Player1 wins!')
        break
        
    if board[1] = board[2] == board[3] == player2_marker or 
    board[4] = board[5] == board[6] == player2_marker or
    board[7] = board[8] == board[9] == player2_marker or
    board[1] = board[4] == board[7] == player2_marker or
    board[2] = board[5] == board[8] == player2_marker or
    board[3] = board[6] == board[9] == player2_marker or
    board[1] = board[5] == board[9] == player2_marker or
    board[7] = board[5] == board[3] == player2_marker:
        
        print('Congratulations! Player2 wins!')
        break
        
        
        rerun = ''
        
        while rerun != 'yes' and rerun != 'no':
            input('Do you want to play again? [yes/no]')
            
            if rerun = 'yes':
                continue
            if rerun = 'no':
                clear_output
                break
            
            
            
        
        
        


