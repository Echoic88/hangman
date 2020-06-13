"""
Hangman game
"""


def main():
    """
    Hangman game
    """

    def input_word():
        word_input = input("Enter a word: ").lower()
        return word_input

    word = input_word()

    word_dashed = word.replace(word, "-"*len(word))
    tracker = list(word_dashed)
    plays = 5

    def guess_letter():
        guess = input("Guess a letter: ")
        return guess

    while plays > 0 and word != "".join(tracker):
        print("Guess the word")
        print("".join(tracker))
        print(f'You have {plays} chances left')
        guess = guess_letter()
        if guess in word:
            for index in range(len(word)):
                if word[index] == guess:
                    tracker[index] = guess
        else:
             plays -= 1

        if "".join(tracker) == word:
            print("You win \\(^o^)/")
            break

    else:
        print("You lose (;_;)")

main()
