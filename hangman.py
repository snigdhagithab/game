import random
from words import words
import string
import hangman_pic

def get_word(words):
	right_word = random.choice(words)
	return right_word.upper()

#the game

def game():
	#some variables to work with
	right_word = get_word(words)
	word_letters = set(right_word)#letters inthe word
	letters = set(string.ascii_uppercase)
	used_letter = set()
	lives = 7

	#getting input
	while len(word_letters) > 0 and lives > 0:
		#letter used:
		#''.joint(['a','s','df' --> 'a s df'])

		print(f"you have {lives} live.You have used letters:",''.join(used_letter))


		#what current word is 
		word_list =[letter if letter in used_letter else "-" for letter in right_word ]
		print("current word:",''.join(word_list))
		user_letter = input("what's your guessed letter:").capitalize()
		if user_letter in letters - used_letter:
			used_letter.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			else:
				lives = lives - 1
				print(hangman_pic.HANGMANPICS[(7-(lives+1))])
		elif user_letter in used_letter:
			print("the letter has already been printed.")
		else:
			print("Invalid input")
	
	if lives == 0:
		print(f"you died .The word was {right_word}")
	else:
		print(f"you guessed the word {right_word}")



game()