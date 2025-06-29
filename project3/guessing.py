import random

easy_word = ["india", "pakistan", "japan", "kohli", "rohit", "iran", "thai" ,"tiger"]
medium_word = ["big boy", "roundup", "undertaker", "roman rance", "eliphant", "starboy"]
hard_word = ["this is godguy","out of ten" ,"increament salery", "t20 world cup","Noboduy argument me", "i am the best"]

print("welcome the passoword guessing game with hints")
print ("choose a difficulty level : easy , medium or hard")

level = input("Enter difficulty level : ").lower()

if level == "easy" :
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)   
elif level == "hard" :
    secret = random.choice(hard_word)
else :
    print ("Enter the valid choice : defaulting chosing easy level")
    secret = random.choice(easy_word)

attempts = 0
print ("\n guess the secrate password !")

while True:
    guess = input("Enter the guessing keyword :").lower()
    attempts += 1
    if guess == secret:
        print (f"congratulations! you guessed it in {attempts} attempts. ")
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else :
            hint += "_"
    print ("Hint : ", hint)
print("Game over")