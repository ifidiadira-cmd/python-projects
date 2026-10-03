# Student Name: Adira Ifidi 

import random

def welcome_player():
    global name
    name = input("What is your name: ")
    print(f"Hello {name}! Welcome to Battleship")
    print("Try to sink all 3 ships hidden in the 5x5 grid")

def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for i in range(size):
            row.append('O')
        board.append(row)
    return board

def print_board(board):
    for i in board:
        print(" ".join(i))

def place_ships(board, count):
    size = len(board)
    ships = {}
    while len(ships) < count:
        rows = random.randint(0, size -1)
        col = random.randint(0,size-1)
        if (rows, col) not in ships:
            ships[(rows, col)] = False
    return ships

def get_guess(size):
        guess_row = int(input('Guess Row (0-4): '))
        guess_col = int(input('Guess Column (0-4): '))
        return (guess_row, guess_col)

def process_guess(board, ships, guess_row, guess_col):
    if not (0 <= guess_row <len(board) and 0 <= guess_col < len(board)):
        print('Not in grid, try again')
        return
    
    if board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == '-':
        print('You already tried that spot!')
        return
    
    if(guess_row, guess_col) in ships:
        print("Hit!")
        board[guess_row][guess_col] = 'X'
        ships.update({(guess_row, guess_col): True})

    else:
        print('Miss!')
        board[guess_row][guess_col] = '-'

def all_sunk(ships):
    if all(value == True for value in ships.values()):
        print('Congratulations! You sank all the ships')
        return True

def game_loop(board, ships):
    turns = 10
    size = len(board)

    for turn in range(turns):
        print(f'Turn {turn +1} of {turns}')
        print_board(board)

        guess_row, guess_col = get_guess(size)
        process_guess(board, ships, guess_row, guess_col)

        if all_sunk(ships):
            print(f'Attempts: {turn + 1}')
            print('You win!')
            print_board(board)
            return
        
    print(f'Attempts: {turns}')
    print('Game Over! Womp Womp. Thanks for playing Battleship')

    for (rows, column), hit in ships.items():
        if not hit and board[rows][column] == 'O':
            board[rows][column] = 'S'
    print('Ships revealed: ')
    print_board(board)

def play_again():
    while True:
        answer = input('Play again? (Y/N): ').upper()
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            print('Enter a valid input(Y/N)')

def main():
    welcome_player()
    size = 5
    board = create_board(size)
    ships = place_ships(board, 3)
    game_loop(board, ships)

    if play_again():
        main()
    else:
        print(f'Thanks for playing BattleShip {name}! and Goodbye!')

if __name__ == "__main__":
    main()