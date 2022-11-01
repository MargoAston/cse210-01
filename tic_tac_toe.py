"""
Margo Aston
CSE210 | Programming with Classes
W01 Prove: Developer
"""
# The game board is a list of rows. Each row is a list of values.
game_board = []

def main():
    play_again = input("Do you want to play Tic-Tac_Toe? (y/n): ")
    while play_again == 'y':
        game_board = []
        board_size=int(input("\nWhat is your board size:"))
        create_game_board(board_size, game_board)
        print_game_board(board_size, game_board)
    
        marker = "X"
        location = int(input(f"X's turn to choose a square 1-{board_size**2}:"))
        update_game_board(marker, location, board_size, game_board)
        print_game_board(board_size, game_board)
        count = 1
        for index in range (0, (board_size**2)-1, 2):
            
            marker = "O"
            location = int(input(f"O's turn to choose a square 1-{board_size**2}:"))
            update_game_board(marker, location, board_size, game_board)
            print_game_board(board_size, game_board)
            count += 1
            print(count)
            if count == (board_size**2):
                print(count)
                break
            else:
                marker = "X"
                location = int(input(f"X's turn to choose a square 1-{board_size**2}:"))
                update_game_board(marker, location, board_size, game_board)
                print_game_board(board_size, game_board)
                count += 1

        play_again = input("Do you want to play again (y/n): ")



def create_game_board(size, game_board):
    counter = 1
    for index in range(0, size):
        # Create a list for each game row.
        row_index = "row_" + str(index)
        (row_index) = [] 

        for index in range(0, size):
            # Appends a value to the list for each square in the row.
            row_index.append(counter)
            counter += 1
        # Appends the list of values to the game board list.    
        game_board.append(row_index)
    print(game_board)

def update_game_board(marker, location, size, game_board):
    # Find the correct row.
    row_number = int((location / size) + .9)
    row_index = (row_number - 1)

    a_row = game_board[row_index]
    column_index = a_row.index(location)
    a_row[column_index] = marker
    game_board[row_index] = a_row


def print_game_board(size, game_board):
    
    for index in range(0, size):
        a_row = game_board[index]
        for index in range(0, size-1):
            print(f'   {a_row[index]}\t|', end="")
        print(f'   {a_row[index+1]}\n--------', end="")  
        for index in range(0, size-1) : 
            print(f'+-------', end="") 
        print()   
        
        
        
        




        
   



if __name__ == "__main__":
    main()