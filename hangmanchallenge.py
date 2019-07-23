import random
potential_words = ["Summer", "Beach", "Juice", "Ice Cream"]
potential_word = random.choice(potential_words)
#potential_word = potential_word[0] + potential_word[(len(potential_word)-1): (len(potential_word))]
word = ["_ "]*len(potential_word)

guesses = [20]
maxfails = 7
fails = 0
print("Let's play Hangman!")
print("Begin")

while fails < maxfails:
	print(word)
	guess = input("Guess a letter:")
	if guess not in potential_word:
		print("Give it another shot. You got this!!")
		guess =+ 1
	elif guess in potential_word:
		print("You are correct!")
		if guess == guesses:
			guess += 1

print(potential_word)
print("You have" + str(maxfails - fails) + "tries left!")
print("Goodbye")
