import random

words = ["computer science", "hard disk", "usb", "iphone", "software"]
myword = 'a'
while len(myword) < 4:
	myword = random.choice(words)
myword = myword.lower()

def hangMan():
  guesses = 0
  word = random.choice(words)
  word_list = list(word)
  blanks = "_"*len(word)
  blanks_list = list(blanks)
  new_blanks_list = list(blanks)
  guess_list = []

  print("HANGMAN")
  print("" + ' '.join(blanks_list))
  print("Guess a letter.\n")

  while guesses < 6:

  		guess = str(raw_input("> "))
  		guess = guess.lower()

  		if guess in guess_list:
  				print("You have guessed that letter already.")
  		else:
  				guess_list.append(guess)
  				i = 0
  				while i < len(word):
  						if guess == word[i]:
  								new_blanks_list[i] = word_list[i]
  						i = i+1

  				if new_blanks_list == blanks_list:
  						print("Your letter isn't here.")
  						guesses = guesses + 1

  						if guesses < 6:
  								print("Guess again.")

  				elif word_list != blanks_list:

  						blanks_list = new_blanks_list[:]

  						if word_list == blanks_list:
  						  print("You win! Your letter was",word)
  						  print("Type y if you want to play again")
  						  again = str(input("> "))
  						  if again == "y":
  						    hangMan()
  						  quit()

  						else:
  								print("Good guess!")

hangMan()