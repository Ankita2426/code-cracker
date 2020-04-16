import random

#guess number
def get_guess():
    return list(input("please guess a number: "))

#generate computer code
def generate_code():
    digits = [str(num) for num in range(10)]

#shuffle the digits+
    random.shuffle(digits)

#then grab the first three
    return digits[:3]

#generate the clues
def generate_clues(code,user_guess):
    if user_guess == code:
        return "code is cracked"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return["nope"]
    else:
        return clues
#run game logic
print("welcome code breaker!")
print("code consist of total 3 numbers")
print("it will show *match* if number is allocated in correct position.")
print("it will show *close* if number is present but not in correct position.")
print("it will show *null* if guess is completely wrong")

#new comment is here
secret_code = generate_code()

clue_report = []

while clue_report != "code cracked":
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
