# FUNCTION FOR OPENING FILE AND READING IT
# defining the function w/o arguments because it's localized
import random


def open_file(file):
    # opening the file in read mode and will auto close it too
    with open(file) as my_file:
        # reading the file on the right then in data it makes it readable for humans
        data = my_file.read()
        format_data = data.split()
        return format_data

# def choose_random_word() --> choice() from a random module? or from my .txt file


# print(open_file('words.txt'))

# WILL NEED TO CALL FILE FUNCTION
# open_file('words.txt')


def play_game():
    word_list = open_file('words.txt')
    word_to_guess = random.choice(word_list)
    print(word_to_guess)
    # word = 'apple'
    user_guess = input('Guess a lowercase letter! ')
    # ? need to create empty lists (or something) to store user guesses, wrong
    # and right guesses - will need to store a count of one or both of those

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
