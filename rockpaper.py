import random
choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    user = input("rock/paper/scissors/q: ").lower()
    if user == "q":
        break
    if user not in choices:
        continue
    comp = random.choice(choices)
    print(f"You: {user} | Computer: {comp}")
    if user == comp:
        print("Tie!")
    elif beats[user] == comp:
        # user's choice beats computer's choice
        print("You win!")
    elif beats[comp] == user:
        # computer's choice beats user's choice
        print("You lose!")
    else:
        # fallback for any unexpected case
        print("Result unclear")