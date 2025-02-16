import random
from wordlist import words


#dictionay of key:()
hangman_art = {
    0: (
        "   _______  ",
        "  |/      |  ",
        "  |          ",
        "  |          ",
        "  |          ",
        "  |          ",
        " _|_         "
    ),
    1: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |          ",
        "  |          ",
        "  |          ",
        " _|_         "
    ),
    2: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |       |  ",
        "  |          ",
        "  |          ",
        " _|_         "
    ),
    3: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |      /|  ",
        "  |          ",
        "  |          ",
        " _|_         "
    ),
    4: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |      /|\\",
        "  |          ",
        "  |          ",
        " _|_         "
    ),
    5: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |      /|\\ ",
        "  |      /   ",
        "  |          ",
        " _|_         "
    ),
    6: (
        "   _______  ",
        "  |/      |  ",
        "  |       o  ",
        "  |      /|\\ ",
        "  |      / \\ ",
        "  |          ",
        " _|_         "
    )
}


def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
            
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You won!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("you lose!")
            is_running = False

if __name__ == "__main__":
    main()