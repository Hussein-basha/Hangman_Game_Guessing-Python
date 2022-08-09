import random

from hangman_guessing import guess_list
guessing_word = random.choice(guess_list).lower()
word_letters = len(guessing_word)
game_over = False
tries = 6

from hangman_life import game_name
print(game_name)

print(f'The Word You Guessed Is : {guessing_word}')


result = []
for _ in range(word_letters):
    result += '_'

while not game_over:
    user_guessing = input('Guess A Letter : ')

    if user_guessing in result:
        print(f'The Letter You Have Guessed Is {user_guessing}')

    for position in range(word_letters):
        letter = guessing_word[position]
        if letter == user_guessing:
            result[position] = letter

    if user_guessing not in guessing_word:
        print(f'You Guessed {user_guessing} , This Letter Is Not In The Word , You Lose A Try.')
        tries -= 1
        if tries == 0:
            game_over = True
            print('Game Over , You Lose The Game , Try A Game Later')

    print(f"{' '.join(result)}")
    if '_' not in result:
        game_over = True
        print('You Are A Winner  , Congratulation')

    from hangman_life import lives
    print(lives[tries])


