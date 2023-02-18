
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
    underscore = '_' * word_length
    # underscore_as_list = list(underscore)

    # for me to know what the word is for now; will take out later
    print(word_to_guess)
    print(f'Your word has {word_length} letters.')
    print(underscore)
    # add spaces to this print statement

    user_guess = input('Guess a letter!\n').lower()
    if len(user_guess) > 1:
        user_guess = input("Your entry is invalid. Try again. ")
        # print(user_guess)

    wrong_guess_letters = []
    wrong_guess_count = 0
    underscore_list = list(underscore)
    # The below loop tests one guess against the word; prints updated gameboard if guess is correct.
    for index in range(len(word_to_guess)):
        if word_to_guess[index] == user_guess:
            underscore_list[index] = user_guess
            print("You guessed right!")
            print(' '.join(underscore_list))
            # m in dream is not printing correctly

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
