import urllib.request

def load_words(url):
	with urllib.request.urlopen(url) as wordfile:
		words = wordfile.read().decode('utf-8').upper().split()
	return words

def allsteps(word):
	result = []
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	for letter in alphabet:
		new_word = word + letter
		anagrams = [w for w in words if sorted(w) == sorted(new_word)]
		result.extend(anagrams)

	return sorted(list(set(result)))

def longest_ladder(words):
	max_ladder = []

	for word in words:
		ladder = [word]
		current_word = word

		while True:
			next_words = allsteps(current_word)
			if not next_words:
				break

			found = False
			for next_word in next_words:
				if next_word in words and next_word not in ladder:
					ladder.append(next_word)
					current_word = next_word
					found = True
					break

			if not found:
				break

		if len(ladder) > len(max_ladder):
			max_ladder = ladder

	return max_ladder

# Load the list of English words
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
words = load_words(url)

# Test the allsteps function
print(allsteps("APPLE"))  # Expected output: ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
print(allsteps("UC"))     # Expected output: ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']
print(allsteps("BEARCAT"))# Expected output: ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']

# Test the longest_ladder function
print(longest_ladder(words))
