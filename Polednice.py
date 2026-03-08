from collections import Counter

with open("polednice.txt", "r", encoding="utf-8") as f:
    text = f.read()

# počet slov
words = text.split()
pocet_slov = len(words)

# počet vět (oddělené prázdným řádkem)
vety = [v for v in text.split("\n\n") if v.strip() != ""]
pocet_vet = len(vety)

# počet písmen
letters = [c for c in text if c.isalpha()]
pocet_pismen = len(letters)

print("Počet slov:", pocet_slov)
print("Počet vět:", pocet_vet)
print("Počet písmen:", pocet_pismen)

# 3 nejčastější slova
word_counts = Counter(words)
print("3 nejčastější slova:", word_counts.most_common(3))

# nejčastější písmeno
letter_counts = Counter(letters)
nej_pismeno = letter_counts.most_common(1)[0][0]

print("Nejčastější písmeno:", nej_pismeno)