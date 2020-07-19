import random 
import os



# algorithm simply makes a random choice from three different columns and concatenates them. 


# print generated insult for the 'user' 
def random_insult():
	pref = 'Thou'

	raw_column1 = open('insults.txt')
	raw_column2 = open('insults2.txt')
	raw_column3 = open('insults3.txt')

	column1 = raw_column1.readlines()
	column2 = raw_column2.readlines()
	column3 = raw_column3.readlines()

	word1 = random.choice(column1)[:-1]
	word2 = random.choice(column2)[:-1]
	word3 = random.choice(column3)[:-1]

	return(word1 + ' ' + word2 + ' ' + word3 + '.' )
