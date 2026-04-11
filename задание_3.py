text = str(input()).split()
text = [str(word) for word in text]

punctuation = ".,!?:;-"
result = []

for word in text:
    clean_word = ""

    for char in word:
        if char not in punctuation:
            clean_word += char

    result.append(clean_word)

print(result)