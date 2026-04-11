text = str(input()).split()
text = [str(word) for word in text]

punctuation = ".,!?:;-"
result = []

for word in text:
    clean_word = ""

    for char in word:
        if char not in punctuation:
            clean_word += char

    if clean_word not in result:
        result.append(clean_word)

print(result)