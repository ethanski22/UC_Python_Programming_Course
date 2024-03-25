# allsteps function
def allsteps(word):
    # Create a dictionary to store words indexed by their sorted form
    word_dict = {}
    for w in words:
        sorted_w = ''.join(sorted(w))
        if sorted_w not in word_dict:
            word_dict[sorted_w] = []
        word_dict[sorted_w].append(w)

    # Generate one-step words
    one_step_words = []
    sorted_word = ''.join(sorted(word))
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_word = sorted_word + char
        if new_word in word_dict:
            one_step_words.extend(word_dict[new_word])

    # Remove duplicates and sort the list
    return sorted(list(set(one_step_words)))

# longest_ladder function
def longest_ladder(words):
    # Create a dictionary to store words indexed by their sorted form
    word_dict = {}
    for w in words:
        sorted_w = ''.join(sorted(w))
        if sorted_w not in word_dict:
            word_dict[sorted_w] = []
        word_dict[sorted_w].append(w)

    def dfs(word, visited):
        visited.add(word)
        max_ladder = [word]
        sorted_word = ''.join(sorted(word))
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_word = sorted_word + char
            if new_word in word_dict:
                for next_word in word_dict[new_word]:
                    if next_word not in visited:
                        ladder = dfs(next_word, visited)
                        if len(ladder) > len(max_ladder):
                            max_ladder = ladder
        visited.remove(word)
        return [word] + max_ladder

    # Find the longest k-ladder
    longest_ladder = []
    visited = set()
    for word in words:
        if word not in visited:
            ladder = dfs(word, visited)
            if len(ladder) > len(longest_ladder):
                longest_ladder = ladder

    return longest_ladder

# Starter code to load the list of English words
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

# Test cases for allsteps function
print(allsteps("APPLE"))    # ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']
print(allsteps("UC"))       # ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']
print(allsteps("BEARCAT"))  # ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']

# Test case for longest_ladder function
print(longest_ladder(words))
