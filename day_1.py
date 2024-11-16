#Merge Strings Alternately

word1 = "abc"
word2 = "pqrs"

word1_len = len(word1)
word2_len = len(word2)

print("word1len",word1_len)
print("word2len",word2_len)

if word1_len > word2_len:
    largest_word = word1
    smallest_word = word2
elif word2_len >word1_len:
    largest_word = word2
    smallest_word = word1
else:
    largest_word = word1
    smallest_word = word2
print(smallest_word,largest_word)
letters = ''
for index,letter in enumerate(largest_word):
    print(index)
    if index <= len(smallest_word)-1:
        letters += f"{letter}{smallest_word[index]}"
    else:
        letters += f"{letter}"
    print(letters)

print(letters)