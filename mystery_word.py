
import random


def open_file(file):
    with open(file) as my_file:
        data = my_file.read()
        format_data = data.split()
        return format_data


def choose_random_word(list):
    word = random.choice(list)
    return word


# def check_one_guess(word):
#     for char in word:


def play_game():
    # good illustration of calling a function within a function
    word_to_guess = choose_random_word(open_file('test-word.txt'))
    word_length = len(word_to_guess)
    underscore = '_ ' * word_length
    # underscore_as_list = list(underscore)

    # for me to know what the word is for now; will take out later
    print(word_to_guess)
    print(f'Your word has {word_length} letters.')
    print(underscore)

    user_guess = (input('Guess a letter! ')).lower()
    print(user_guess)
    if len(user_guess) > 1:
        user_guess = input("Your entry is invalid. Try again. ")
        print(user_guess)

    right_guess_count = 0
    wrong_guess_count = 0

    i = 0
    for char in word_to_guess:
        current_index = word_to_guess[i]
        i += 1
        if current_index == user_guess:
            updated_game_board = underscore[:i] + \
                user_guess + underscore[i+1:]
            print(updated_game_board)

# while loop: while wrong_guess_count < 8...
# break: when wrong_guess_count = 8

# trying to write code for process of just one guess:
# for char in s:
# print(char)


# CLASS EXAMPLE
# word = 'apple'
# wrong_guesses = ['b', 'd']
# right_guesses = ['a', 'p']
# game_board = ''
# for letter in word:
#     if letter in right_guesses:
#         game_board += letter + ' '
#     else:
#         game_board += '_ '
# print(game_board)
if __name__ == "__main__":
    play_game()
