s = input("Enter a word : ")
s = s.lower()
checkCount = 0

ls = len(s)

for i in range(0, ls):
    if s[i] == s[ls - i - 1]:
        checkCount += 1

if checkCount > 0:
    print("Yes, the word is a palindrome.")
else:
    print("This word is not a palnidrome.")
