word_stats = {}
special_characters = [",", ";", ".", "!", ":", "-", " "]

with open("C://Users//Kostas//PycharmProjects//learningBasics310//exercises//poem.txt", "r") as f:
    for line in f:
        if line == '\n' or line == '':
            continue  # if this line is just a line break or completely empty, continue to next iteration of for

        words = line.split(" ")
        for word in words:

            if word[-1] == "\n":  # if last char is a line break, remove it
                word = word[0:-1]

            if word[-1] in special_characters:  # if last char is in special chars list, remove it.
                word = word[0:-1]

            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1

# print(word_stats)

word_occurrences = list(word_stats.values())
max_count = max(word_occurrences)
print(f"The maximum number of times a word appears in the poem is: {max_count}")

print("Words with maximum occurrence:")
for word, count in word_stats.items():  # word, count = key, value
    if count == max_count:
        print(word)

