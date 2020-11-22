import random
words = ["magic", "fog", "join", "amusement", "school", "blade"]
TheWord = random.choice(words)
print(TheWord)

current = "_" * len(TheWord)
ShowedList = list(current)
needToGuess = list(TheWord)
print (*ShowedList)

print("Welkome to HANGMAN")
print("Type 'QQ' to quit")
Input = input("Guess the word >>> ")

guessedList = []

fails = 0

while(Input != "QQ"):
	print()
	if (fails >= 5):
		print("You lost!")
		print("The word was ", TheWord)
		break
	else:
		if (Input.isalpha()):
			if Input in guessedList:
				print("Already Guessed.")
				Input = input("Guess the word >>> ")
			else:
				guessedList.append(Input)
				if Input in TheWord:
					print("You guessed it.")
					for i in range(len(Input)): 
						for y, x in enumerate(TheWord):
							if(x == Input[i]):
								if(ShowedList[y] == "_"):
									ShowedList[y] = Input[i]
									
				else:
					print("Not the right word...")
					fails = fails + 1
				print(*ShowedList)
				if (ShowedList == needToGuess):
					print("You Win!")
					break
				else:
					Input = input("Guess the word >>> ")
		else:
			print("Not a letter, please try again")
			Input = input("Guess the word >>> ")
