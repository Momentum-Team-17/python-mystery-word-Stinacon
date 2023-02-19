
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
    word_to_guess = choose_random_word(open_file('test-word.txt'))
    word_length = len(word_to_guess)
    underscore = '_' * word_length

    # for me to know what the word is for now; will take out later
    print(word_to_guess)
    print(f'Your word has {word_length} letters.')
    print(underscore)
    # add spaces to this print statement

    # print(user_guess)

    wrong_guess_letters = []
    wrong_guess_count = 0
    underscore_list = list(underscore)

    while wrong_guess_count < 8:
        user_guess = input('Guess a letter!\n').lower()
        if user_guess in word_to_guess:
            for index in range(len(word_to_guess)):
                if word_to_guess[index] == user_guess:
                    underscore_list[index] = user_guess
                    print("You guessed right!")
                    print(' '.join(underscore_list))
                    user_guess = input("Guess another letter.\n")
        elif len(user_guess) > 1:
            user_guess = input("Your entry is invalid. Try again. ")
            print(wrong_guess_count)
        elif user_guess not in word_to_guess and user_guess not in wrong_guess_letters:
            wrong_guess_count += 1
            wrong_guess_letters.append(user_guess)
            print(wrong_guess_count)
            user_guess = input("Nope! Guess another letter.\n")
        else:
            user_guess = input(
                "You have already guessed that letter. Try again.")

        # should i use if in instead of a loop below?
        # The below loop tests one guess against the word; prints updated gameboard if guess is correct.

        # an if or elif inside while loop that "breaks" when all letters have been guessed correctly
    else:
        print("You have used all 8 guesses. You have been eliminated.")
        user_guess
    play_again = input("Do you want to play again Y/N?\n")
    if play_again == 'Y':
        play_game()
# while loop: while wrong_guess_count < 8...
# break: when wrong_guess_count = 8


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
