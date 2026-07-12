print("=" * 40)
print("      Welcome to Quiz Game")
print("=" * 40)

score = 0

print("\nQuestion 1:")
answer = input("What is the capital of Pakistan? ")

if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuestion 2:")
answer = input("How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuestion 3:")
answer = input("What is 5 + 3? ")

if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Final Score is:", score, "/3")
