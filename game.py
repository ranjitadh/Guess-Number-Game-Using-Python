
#NUMBER GUESSING GAME

from random import randint

def game():
    num = randint(1, 100)
    guess = int(input("Guess the number between 1 and 100 : "))
      
    while num!= guess:
        print("You loose")
        if num>guess:
            print(f"The number is greather than {guess}")
        else:
            print(f"The number is less  than {guess}")
        guess = int(input("Guess the number between 1 and 100 : "))

    print("You win")
   

game()
