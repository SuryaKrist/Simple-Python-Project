secret_numbers = 9
guess = int(input("guess the number between 1 and 10 :"))

if guess == secret_numbers:
    print("Your guess is correct!")
elif guess <= secret_numbers:
    print("Your guess is too small")
else:
    print("Your guess is too big")
    

