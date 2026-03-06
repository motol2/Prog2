
with open("erben.txt", "r") as file:
    text = file.read()


words = text.split(" ")
word_count = len(words)

letter_count = {}

for char in text:
    if char != " ":  
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

most_common = max(letter_count.values())

print("Počet slov:", word_count)
print("Počet výskytů nejčastějšího písmena:", most_common)