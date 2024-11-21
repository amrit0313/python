import random

plays =True
def playGame():
    print("Let's play the game")
    decision = input("Type easy for 'Easy' and type hard for 'Hard': " )
    number = random.randint(1, 100)
    def compare(guess):
        if guess== number:
                print('Hey! you guessed it right')
                return 'correct'
        elif guess > number:
            print("Guess some lower ")
        elif guess < number:
            print("Guess some higher ") 

    def easy():
        n=10
        for _ in range(0,10):
            print(f'you have {n} attempts left')
            guess = int(input('Guess a number: '))
            result = compare(guess)
            if result == 'correct':
                return
            n-=1
            if n == 0:
                print(f"Hey! your attempts ended, correct answer was {number}")


    def hard():
        n=5
        for _ in range(0,5):
            print(f'you have {n} attempts left')
            guess = int(input('Guess a number'))
            result =compare(guess)
            if result == 'correct':
                return
            n-=1
            if n ==0:        
                print(f"Hey! your attempts ended, correct answer was {number}")



    if decision == 'easy':
        easy()
    elif decision == 'hard':
        hard()
while plays:
    playGame()
    play = input("Wanna play more?Type yes to continue, and no to exit: ")
    if play == 'yes':
        plays = True
    else:
        plays = False    