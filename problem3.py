import random
word_list = ["orange", "banana","mango","apple"]
random_word = random.choice(word_list)
letters = list(random_word)
random.shuffle(letters)
scramble_word = ''.join(letters)

attempts = 5
print("Welcome to the Word Scramble Game!")
print("Try to guess the original word from the scrambled word: ", scramble_word)
print("pYou have 5 attempts.")

while attempts > 0:
    input_word = input("Enter your guess: ")
    if random_word == input_word:
        print("Congratulations! You guessed the correct word!")
        break 
    else:
        attempts-=1
        if attempts>0:
            print(f"Incorrect! Try again. You have{attempts} attempts left.")
        else:
            print("You’re out of attempts! The correct word was: ", random_word) 




