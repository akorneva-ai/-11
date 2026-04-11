lst = input().lower().split()

letters = ["a", "b", "d", "e", "g", "o", "p", "q"]
result = []

count_all = 0

for word in lst:
    if word != " ":
        count_all += 1

    for letter in word:
        count_all += 1

def count_holes(words):
    """
     Count the total number of letters with holes in all words

    :param words: list of words
    :return: number of letters with holes
    """
    count_holes = 0
    for word in words:
        for letter in words:
            if letter in letters:
                count_holes += 1

    return count_holes


def holes_in_word(word):
    """
    ount the number of letters with holes in a single word

    :param word: input word
    :return: number of letters with holes in the word
    """
    c_holes = 0
    for letter in word:
        if letter in letters:
            c_holes += 1

    return c_holes

count_with_holes = count_holes(lst)
count_without_holes = count_all - count_with_holes


for word in lst:
    if holes_in_word(word) >= 2:
        result.append(word)

print("Количество букв без дырок: ", count_without_holes, "Количество букв с дырками: ", count_all - count_holes(), result)
