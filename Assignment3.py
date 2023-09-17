file_name = "input.txt"

search_words = ["Python", "C", "OOP", "Hello", "Java"]

word_count = {word: 0 for word in search_words}

with open(file_name, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1

for word, count in word_count.items():
    print(f"{word} -> {count}")
