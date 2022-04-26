import random
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

live = 6

chosen_word = word_list[random.randint(0,2)]
display = ["_" for i in range(len(chosen_word))]
print(f'Pssst, the solution is {chosen_word}')
flag = True

while flag : 
    guess = input("guess a letter : ")
    if guess in display :
        print("A letter already guessed")
    index = 0
    for word in chosen_word :
        if word == guess.lower() :
            display[index] = guess.lower()
        index += 1
    print(f"{' '.join(display)}")
    clear()

    if guess.lower() not in chosen_word :
        live -= 1
        print(f"you guessed {guess}, that's not in the word. you lose a life. YOU HAVE {live} life")
        print(stages[live])
        
        if live == 0 :
            flag = False
            print('You loose')
    
    if "_" not in display :
        print("You win")

