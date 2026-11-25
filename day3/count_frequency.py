from collections import defaultdict

sentence = input("Enter a sentence: ")
dictionary :dict[str, int] = defaultdict(int)

for word in sentence.split():
    dictionary[word] += 1

for word, count in dictionary.items():
    print(f"{word}: {count}")