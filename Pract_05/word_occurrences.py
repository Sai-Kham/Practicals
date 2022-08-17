word_frequency = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
    words = list(word_frequency.keys())
    words.sort()
for word in words:
    print("{} : {}".format(word, word_frequency[word]))
