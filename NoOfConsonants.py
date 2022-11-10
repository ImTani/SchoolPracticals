w = input("Enter a word : ")
vowelCount = 0
consonantCount = 0
upperCount = 0
lowerCount = 0
vowels = ('a', 'e', 'i', 'o', 'u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

for letter in w:
    if letter.isupper():
        upperCount += 1
    if letter.islower():
        lowerCount += 1

w = w.lower()

for letter in w:
    if letter in vowels:
        vowelCount += 1
    if letter in consonants:
        consonantCount += 1

print("The number of vowels is :", vowelCount)
print("The number of consonants is :", consonantCount)
print("The number of uppercase letters is :", upperCount)
print("The number of lowercase letters is :", lowerCount)
