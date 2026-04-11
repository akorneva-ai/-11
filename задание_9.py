list_word = []
punctuation = ".,!?:;-"

while True:
    line = input()

    if line == "":
        break

    for word in line.split():
        clean_word = ""

        for char in word:
            if char not in punctuation:
                clean_word += char

        clean_word = clean_word.lower()

        if clean_word != "":
            list_word.append(clean_word)

unique_words = []

for wrd in list_word:
    if wrd not in unique_words:
        unique_words.append(wrd)

for i in range(len(unique_words)):
    for j in range(i + 1, len(unique_words)):
        if list_word.count(unique_words[j]) > list_word.count(unique_words[i]):
            unique_words[i], unique_words[j] = unique_words[j], unique_words[i]

for wrd in unique_words:
    print(wrd)