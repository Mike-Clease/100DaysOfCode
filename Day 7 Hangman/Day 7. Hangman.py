import random
from Hangman_Lives import stages, logo
from Hangman_Words import word_list
import os

clear = lambda: os.system('cls')

chosen_word = random.choice(word_list)

display = ['_'] * len(chosen_word)
lives = 6

clear()

print(logo, "\n\n\n")
print(f"The word is: {display}")
print(stages[lives])
print(f'psssst. The solution is: {chosen_word}')

while '_' in display and lives > 0:

    guess = input("Guess a letter: ").lower()
    clear()
    print(logo, "\n")
    
    if guess not in display:
        if guess not in chosen_word:
            lives -= 1
            print(f"Your guess ({guess}) is not in this word. You lose a life!")
        else:
            for i, letter in enumerate(chosen_word):
                if guess == letter:
                    display[i] = letter
    else:
        print(f"You've already tried {guess} before, guess again.")


    print(display)
    print(stages[lives])
        
if lives > 0:
    print(f"{chosen_word}! You win!")
else:
    print(f"Haha! You lose! The word was: {chosen_word}")