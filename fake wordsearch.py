import random

import re
 
def welcome_player():

    global name

    name = input("What is your name: ")

    print(f"Hello {name}! Welcome to Word Searc\n Find all the hidden words in the grid")

    return name

def read_words(filename):

    try:

        with open(filename, "r") as f:

            words = [line.strip().upper() for line in f if line.strip() != ""]

        return words

    except FileNotFoundError:

        print("File not found. Please check the filename and try again.")

        return []
 
 
def create_grid(size):

    return [[' ' for _ in range(size)] for _ in range(size)]
 
def place_words_in_grid(grid, words):

    size = len(grid)
 
    for word in words:

        placed = False
 
        while not placed:

            rows = random.randint(0, size -1)

            col = random.randint(0,size- len(word))
 
            space_free = True

            for i in range(len(word)):

                if grid[rows][col + i] != ' ':

                    space_free = False

                    break

            if space_free:

                for i in range(len(word)):

                    grid[rows][col + i] = word[i]

                placed = True

    for r in range(size):

        for c in range(size):

            if grid[r][c] == " ":

                grid[r][c] = chr(random.randint(65, 90))
 
def display_grid(grid):

    for i in grid:

        print(" ".join(i))
 
def get_coordinates():

    start = input('Enter start coordinate (e.g., A0): ').upper()

    end = input('Enter end coordinate (e.g., A5): ').upper()
 
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
 
    row_start = int(start[1:])

    row_end = int(end[1:])

    col_start = letters.index(start[0])

    col_end = letters.index(end[0])

    return (row_start, col_start), (row_end, col_end)
 
def check_word(grid, start, end, words, found_words):

    (row_start, col_start) = start

    (row_end, col_end) = end
 
    if row_start == row_end:

        if col_start < col_end:

            letters = grid[row_start][col_start:col_end+1]

        else:

            letters = grid[row_start][col_end:col_start+1]
 
    else:

        print('NO! Only Horizontal')

        return

    guess = ''.join(letters)
 
    if guess in words:

        print(f'Correct! You found {guess}!')

        found_words.append(guess)

        words.remove(guess)

    else:

        print('Not a word, try again')
 
def write_results(output_file, player_name, found_words, remaining_words, attempts):

    file = open(output_file, 'w')
 
    file.write(f'Player: {player_name}\n')

    file.write(f'Attempts: {attempts}\n')

    file.write(f'Found words: {found_words}\n')

    file.write(f'Words remaining: {remaining_words}\n')
 
    print(f'Results saved to "{output_file}".')
 
    file.close()
 
def game_loop(grid, words):

    found_words = []

    remaining_words = words.copy()

    attempts = 0
 
    display_grid(grid)
 
    while remaining_words:

        start, end = get_coordinates()

        check_word(grid, start, end, remaining_words, found_words)

        attempts += 1
 
    print(f"\nCongratulations, {name}! You found all words in {attempts} attempts.")

    write_results("results.txt", name, found_words, remaining_words, attempts)
 
def main():

    player_name = welcome_player()    

    input_file = input("Enter the name of your input file: ").strip()
 
    try:

        words = read_words(input_file)

    except FileNotFoundError:

        print(f" File '{input_file}' not found! Please make sure it’s in the same folder as this script.")

        return
 
    if not words:

        print("No words found in the file. Please check your input file and try again.")

        return

    grid_size = 10  # Adjustable difficulty

    grid = create_grid(grid_size)

    place_words_in_grid(grid, words)

    game_loop(grid, words)

    replay = input("Would you like to play again? (Y/N): ").strip().upper()

    if replay == "Y":

        main()

    else:

        print(f"Thanks for playing, {player_name}! Goodbye.")

# ------------------------------

# Run program

# ------------------------------

if __name__ == "__main__":

   main()

 