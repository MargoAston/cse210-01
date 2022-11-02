"""
Margo Aston
CSE210 | Programming with Classes
W01 Prove: Developer
"""
# The game board is a list of rows. Each row is a list of values.

game_board = []


def main():
    winner = False
    play_again = input("\nDo you want to play Tic-Tac_Toe? (y/n): ")
    while play_again == 'y':
        # Create a game board.
        game_board = []
        board_size=int(input("\nWhat is your board size (must be an integer larger than 1):"))
        while board_size == 1 or board_size < 1:
            board_size = int(input("Please enter a number greater than 1:"))
        create_game_board(board_size, game_board)

        # Print the game board.
        print_game_board(board_size, game_board)
    
        try:
            # Update the game board.
            count = 0
            counter = 0
            player_1 = "X"
            player_2 = "O"
            while count < (board_size**2):
                # Player 1's turn.
                location = int(input(f"X's turn to choose a square 1-{board_size**2}:"))
                counter = update_game_board(player_1, location, board_size, game_board)
                print_game_board(board_size, game_board)
                winner = check_for_win(board_size, player_1, game_board)
                if winner == True:
                    break
                count += counter
            
                # Checking for end of game.
                if count == (board_size**2):
                    break

                else:
                    # Player 2's turn.
                    location = int(input(f"O's turn to choose a square 1-{board_size**2}:"))
                    counter = update_game_board(player_2, location, board_size, game_board)
                    print_game_board(board_size, game_board)
                    winner = check_for_win(board_size, player_2, game_board)
                    if winner == True:
                        break
                    count += counter
  


        except IndexError as index_err:
            # This code will be executed if the user enters a valid integer for the square number, but the integer is greater than the number of squares in the game.
            print()
            print(type(index_err).__name__, index_err, sep=": ")
            length = len(game_board)
            if location < 0:
                print(f"{location} is a negative integer.")
            else:
                print(f"{location} is greater than the number of squares in the game.")
                print(f"There are only {length**2} squares in game.")
            print(f"Start a new game and enter a square number between 1 and {length**2}.")

        # Checking for start of new game.
        play_again = input("Do you want to play again (y/n): ")  
        while play_again != 'y':
            if play_again == 'n':
                print("Thank you for playing, see you next time.")
                break
            play_again=input('invalid entry. Please enter (y/n)')

    print("Thank you for visiting Tic-Tac_Toe\n")
    

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
       


def update_game_board(player, location, size, game_board):
    try:
        # Find the correct row.
        row_number = int((location / size) + .9)
        row_index = (row_number - 1) 
        a_row = game_board[row_index]

        # Find the correct column.
        column_index = a_row.index(location)

        a_row[column_index] = player
        game_board[row_index] = a_row
  
        return 1
    except ValueError as val_err:
        # This code will be executed if the user enters an integer that is not on the game board.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("That square is not available. Better luck next time.\n")
        return 0

def check_for_win(size, player, game_board):
    win = False
    # Create winning sequence.
    winning_sequence = []
    for index in range(0, size):
        winning_sequence.append(player)

    # Compare winning sequence to each game board row.
    for index in range(0, size):
        if game_board[index] == winning_sequence:
            print(f"{player} wins!")
            win = True
            return win

    # Create game board column.  
    for index in range(0, size):
        column = []
        column_index = index
        for index in range (0, size):
            row = game_board[index]
            column.append(row[column_index])    
        # Compare winning sequence to game board column.
        if column == winning_sequence:
            print(f"{player} wins!")
            win = True
            return win  

    # Create game board diagonal.
    diagonal = []
    for index in range (0, size):
        row = game_board[index]
        diagonal.append(row[index])
    # Compare winning sequence to game board diagonal.    
    if diagonal == winning_sequence:
        print(f"{player} wins!")
        win = True
        return win  
            
    # Create game board diagonal2.
    diagonal2 = []
    column = size-1
    for index in range (0, size):
        row = game_board[index]
        diagonal2.append(row[column])
        column -= 1
    # Compare winning sequence to game board diagonal2.    
    if diagonal2 == winning_sequence:
        print(f"{player} wins!")
        win = True
        return win 



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