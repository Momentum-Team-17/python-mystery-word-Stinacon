
import random


def open_file(file):
    with open(file) as my_file:
        data = my_file.read()
        format_data = data.split()
        return format_data


def choose_random_word(list):
    word = random.choice(list)
    return word


def play_game():
    # good illustration of calling a function within a function
    word_to_guess = choose_random_word(open_file('words.txt'))
    word_length = len(word_to_guess)
    underscore = '_ ' * word_length
    underscore_as_list = list(underscore)

    # for me to know what the word is for now; will take out later
    print(word_to_guess)
    print(f'Your word has {word_length} letters.')
    print(underscore)

    user_guess = (input('Guess a letter! ')).lower()
    print(user_guess)
    if len(user_guess) > 1:
        user_guess = input("Your entry is invalid. Try again. ")
        print(user_guess)
    right_guesses = []
    wrong_guesses = []
    wrong_guess_count = len(wrong_guesses)
    # ? need to create empty lists (or something) to store user guesses, wrong
    # and right guesses - will need to store a count of one or both of those

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
