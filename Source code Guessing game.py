import random
num_attempts=0
print("Hello Gamer! What is your name?")
name=input()
number=random.randint(1,20)

print('Well,'+name+',I am thinking of a number between 1 and 20.')
while num_attempts<6:
    diff=str(6-num_attempts)
    print('So try to guess that number, you have '+diff+' attempt(s) left to get it right')
    guess=input()
    guess=int(guess)
    num_attempts+=1
    if guess<number:
        print('your guess is low')
    if guess>number:
        print('your guess is too high')
    if guess==number:
        break
if guess==number:
    num_attempts=str(num_attempts)
    print('Good Job,'+name+'! You guessed my number in '+num_attempts+' Guesses !')
if guess !=number:
    number=str(number)
    print('Nope. The number I was thinking of was '+number)
