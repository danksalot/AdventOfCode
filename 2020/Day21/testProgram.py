

with open('Input') as inFile:
	lines = inFile.read().splitlines()

allergenList = {}
safe_words = set()
for line in lines:
    words, allergens = line[:-1].split(" (contains ")
    words = words.split(" ")
    safe_words |= set(words)
    allergens = allergens.split(", ")
    for allergen in allergens:
        if allergen not in allergenList:
            allergenList[allergen] = set(words)
        else:
            allergenList[allergen] &= set(words)

# print('Safe:', safe_words)
# print('Risky', [x for v in allergenList.values() for x in v])
print(allergenList)
safe_words = safe_words - set(x for v in allergenList.values() for x in v)
print(len(safe_words))
out = 0
for line in lines:
    words, allergens = line[:-1].split(" (contains ")
    words = words.split(" ")
    allergens = allergens.split(", ")
    out += sum(word in safe_words for word in words)
print(out)


keys = sorted(allergenList.keys(), key=lambda x: len(allergenList[x]))
for key in keys:
    if len(allergenList[key]) == 1:
        allergen = next(iter(allergenList[key]))
        for key2 in keys:
            if key2 != key:
                allergenList[key2].discard(allergen)
print(",".join([next(iter(allergenList[x])) for x in sorted(allergenList.keys())]))