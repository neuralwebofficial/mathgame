import random

global corrects
global wrongs
global attempted

corrects = 0
wrongs = 0
attempted = 0

print("Math game\n")

ops = ["+", "-", "/", "*"]

while True:
    digit1 = random.randint(0, 10)
    digit2 = random.randint(0, 10)
    operation = random.choice(ops)

    while digit2 == 0 and operation == "/":
        digit2 = random.randint(0, 10)

    answer = eval(f"{digit1} {operation} {digit2}")

    print(f"What is {digit1} {operation} {digit2} ?")

    user_answer = float(input("Enter the answer: "))

    if user_answer == answer:
        corrects += 1
        print("\nYour answer is correct\n")

    else:
        wrongs += 1
        print("\nYour answer is wrong")

    attempted += 1

    while attempted == 10:
        print(f"You got {corrects} correct and {wrongs} wrong out of {attempted}")
        quit()