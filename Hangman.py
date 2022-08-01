from Words import words
import random
import string



def target_word(random_word):
    word = random.choice(random_word)
    while '-' in word or ' ' in word or len(word) != 5:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = target_word(words)
    valid_alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    word_letters = set(word)
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives and You have used these letter', ' '.join(guessed_letters))
        word_list = []
        for letter in word:
            if letter in guessed_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print('Current word', ' '.join(word_list))

        user_letter = input('Guess a letter ').upper()
        if user_letter in valid_alphabet:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1

        elif user_letter in guessed_letters:
            print('\n you have already guessed this letter')

        else:
            print(user_letter + ' - is not a valid letter')

    if lives == 0:
        print('Sorry You lost :( the correct word was ' + word)
    else:
        print('Yay You guessed the word ' + word)


def main():
    hangman()


if __name__ == "__main__":
    main()
