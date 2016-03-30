import string
import random
import subprocess

word_list = subprocess.check_output(
    "cat /usr/share/dict/words | grep -v \"'s\"",
    shell=True, 
    universal_newlines=True
).split('\n')

# word_list = ['munchkin', 'cat', 'vex', 'dog', 'doom', 'aardvark', 'recursion', 'dyslexia']

word = random.choice(word_list).upper()
blanks = ["_"] * len(word)
available_guesses = 10
num_bad_guess = 0
player_guesses = []
winner = False


def get_input():
    invalid = True
    while invalid:
        print("You have guessed: {}".format(', '.join(sorted(player_guesses)) if player_guesses else ''))
        guess = input("Guess letter: ").upper()
        if len(guess) > 1:
            print("Only guess one letter, dummy.")
        elif guess in player_guesses:
            print("You've already guessed that letter, dummy.")
        elif guess not in string.ascii_letters:
            print("Enter only letters, dummy.")
        else:
            invalid = False
    return guess


while num_bad_guess < available_guesses and not winner:

    print('\n({} letters)\t{}'.format(len(word), ''.join(blanks)))
   
    guess = get_input()
    player_guesses.append(guess)

    if guess in word.upper(): 
        print("You guessed right")
        indecies = [pos for pos, char in enumerate(word) if char == guess]
        for index in indecies:
            blanks[index] = guess
    else:
        print("You guessed wrong")
        num_bad_guess += 1
        print("You've made {}/{} wrong guesses".format(num_bad_guess, available_guesses))

    if ''.join(blanks).upper() == word.upper():
        winner = True

if winner:        
    print("You have guessed the word!  {}".format(word))
else:
    print("You lose! The word was {}".format(word))


