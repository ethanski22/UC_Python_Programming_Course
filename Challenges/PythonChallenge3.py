def allsteps(word):
	"""
	Returns a list of all unique, valid step words appearing in a list of English words.
	
	Args:
	- word (str): The input word for which one-step words are to be found.
	
	Returns:
	- list: A list of all one-step words.
	
	Examples:
	>>> allsteps("APPLE")
	['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
	
	>>> allsteps("UC")
	['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']
	
	>>> allsteps("BEARCAT")
	['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']
	"""
	
	# Load the list of English words
	url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
	from urllib.request import urlopen
	wordfile = urlopen(url)
	words = wordfile.read().decode('utf-8').upper().split()
	
	# Convert the input word to uppercase
	word = word.upper()
	
	# Initialize a set to store unique one-step words
	onestep_words = set()
	
	# Generate one-step words
	for i in range(len(word) + 1):
			for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
					new_word = word[:i] + char + word[i+1:]
					if new_word != word and new_word in words:
							onestep_words.add(new_word)
	
	return sorted(list(onestep_words))

# Run the doctests
if __name__ == "__main__":
	import doctest
	doctest.testmod()
