#%%
#Step 1: Function to display the board

#from IPython.display import clear_output
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

#%%
# Step 2: Function to ask players for marker (X or O)

def player_input():
    '''
    OUTPUT = (player1_marker, player2_marker)
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()
     
    if marker == 'X':
        return ('X','O')
    
    else:
        return ('O','X')
        
    
#%% test

#(player1_marker, player2_marker) = player_input()
#player1_marker
#player2_marker
# for dict instead of tuple return: return tuple(player_input().values())

#%%
# Step 3: Function to position marker on board

def place_marker(board, marker, position):
    board[position] = marker

#%%
# Step 4: Function to take in marker input and test if a player has won
def win_check(board,marker):
    
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[7] == marker and board[8] == marker and board[9] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker) or
    (board[1] == marker and board[5] == marker and board[9] == marker) or
    (board[7] == marker and board[5] == marker and board[3] == marker))
        
        #alternative:
        #str = ''
        #str.join(board[4,5,6]) == marker*3
        #str.join(board[7,8,9]) == marker*3

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
# Step 9: Ask for replay

def replay():
    
    choice = input('Do you want to play again? [yes/no]').lower().startswith('y')

    return choice == 'y'

#%%
# Step 10: Put functions together to run the game 

def play_TicTacToe():
    
    print('Hello, this is Tic Tac Toe.')
    
    while True:

        # SET UP GAME
        empty_board = ['']*10
        
        (player1_marker, player2_marker) = player_input()

        turn = choose_first()
        print(f'{turn} begins! ')

        play_game = input('Ready to play? [y/n] ')

        if play_game == 'y':
            game_on = True
        else:
            game_on = False
         
         ## GAME PLAY
        while game_on == True:
            ### PLAYER 1 TURN
            if turn == 'Player 1':
                display_board(empty_board)
                
                position = player_choice(empty_board)

                place_marker(empty_board, player1_marker, position)

                if win_check(empty_board,player1_marker):
                    display_board(empty_board)
                    print(f'Congratulations! Player 1 wins!')
                    game_on == False #same as break

                else:
                    if full_board_check(empty_board):
                        display_board(empty_board)
                        print("It's a tie!") 
                        game_on == False #same as break

                    else:
                        turn = 'Player 2'

            ### PLAYER 2 TURN
            else:
                display_board(empty_board)
                
                position = player_choice(empty_board)

                place_marker(empty_board, player2_marker, position)

                if win_check(empty_board,player2_marker):
                    display_board(empty_board)
                    print(f'Congratulations! Player 2 wins!')
                    game_on == False #same as break

                else:
                    if full_board_check(empty_board):
                        display_board(empty_board)
                        print("It's a tie!") 
                        game_on == False #same as break

                    else:
                        turn = 'Player 1'

        if replay():
            clear_board = '\n*100'
            clear_board
            game_on = True
        else:            
            break