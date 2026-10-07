import random

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)

print("\nChoose a difficulty level:")
print("1. Easy   - 10 attempts")
print("2. Medium - 7 attempts")
print("3. Hard   - 5 attempts")

choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    attempts = 10
elif choice == "2":
    attempts = 7
elif choice == "3":
    attempts = 5
else:
    print("Invalid choice. Medium difficulty selected.")
    attempts = 7

secret_number = random.randint(1, 100)
score = 100

print("\nI have selected a number between 1 and 100.")
print("You have", attempts, "attempts to guess it.")

for attempt in range(1, attempts + 1):

    guess = int(input("\nAttempt " + str(attempt) + ": Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("\n🎉 CONGRATULATIONS! 🎉")
        print("You guessed the correct number!")
        print("Attempts used:", attempt)

        score = score - ((attempt - 1) * 10)

        if score < 0:
            score = 0

        print("Your score:", score)
        break

else:
    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Better luck next time!")

print("\nThank you for playing!")