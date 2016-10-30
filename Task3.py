import random

WORDS = ("python", "warships", "Katerina", "Misha")
word = random.choice(WORDS)
correct = word
i = 0

jumble = ""
while word != "":
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print "Hello"
print("The jumble is:", jumble)

guess = raw_input("\nYour guess: ")
while guess != correct and guess != "" and i != len(correct):
    print("Sorry, that's not it.")
    response = ""
    while response not in ("y", "n") and guess != correct and i != len(correct):
        response = raw_input("Do you want a hint?\t")
        if response == "y" and guess != correct:
            print i+1, '-st letter is:', correct[i]
            response = ""
            i += 1
            print correct[:i]
            guess = raw_input("\nYour guess: ")
        elif response == "n":
            guess = raw_input("\nYour guess: ")


print "Thanks for playing. Jumble is", correct

raw_input("\n\nPress the enter key to exit.")