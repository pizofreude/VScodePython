
from itertools import count
import random
import time

# Initial Steps to invite in the game:
print("\nHello and Welcome to the Hangman Game!\n")
name = input("Please enter your name: ")
print("\n   Hiya " + name + "! Best of Luck!")
time.sleep(1)
print("\n   The game is loading...!\n")
time.sleep(1)
print("\n   Auf der Spitze, fertig, los!\n")
time.sleep(1)

# Main content in the game:
def main():
    global count
    global display
    global word 
    global already_guessed
    global length
    global play_game
    words_to_guessed = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guessed)
    length = len(word)
    count = 0
    display = "_ " * length
    already_guessed = []
    play_game = ""


# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes or n = no \n")
    while play_game not in ["y","n","Y","N","yes","Yes","YES","no","No","NO"]:
        return play_game
    if play_game in ["y","Y","yes","Yes","YES"]:
        main()
    elif play_game in ["n","N","no","No","NO"]:
        print("Thanks for playing Hangman game with us! \n")
        time.sleep(2)
        print("Fancy to seeing you next time around! \n")
        exit()


# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word 
    global already_guessed
    global length
    global play_game
    limit = 5
    guess = input("This is the Hangman word: " + display + ". Hint: There are " + str(length) + " letters. \n")
    time.sleep(1)
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, Try again with a letter at a time! \n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()





