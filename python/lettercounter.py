def lettercounter(word):
	count = 0
	for letter in word:
		if letter == inputletter:
			count = count + 1
	print count

inputletter = raw_input('Choose the letter:\n')
inputfruit = raw_input('Choose the word or phrase:\n')

lettercounter(inputfruit)

