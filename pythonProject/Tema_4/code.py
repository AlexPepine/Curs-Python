import random
words = ["caine", "pisica", "masina", "ceas", "minge", "telefon", "artist", "portofel", "calculator", "lampa", "incarcator"]
country = random.choice(words)
mistakes = 3
guesses = []
made = False

while not made:
    for text in country:
        if text.lower() in guesses:
            print(text, end=' ')
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Errors left {mistakes}, next guess > ")
    guesses.append(guess.lower())
    if guess.lower() not in country.lower():
        mistakes -= 1
        if mistakes == 0:
            break

    made = True
    for text in country:
        if text.lower() not in guesses:
            made = False

if made:
    print(f"You won! The word was  {country}!")

else:
    print(f"You lost! The word was{country}!")