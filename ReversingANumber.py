n = input("Enter A Number : ")
numcount = 1
res = 0
res1 = ''
lst = []

try:
    for i in n:
        mult = 10 ** (numcount - 1)
        res = res + (int(i) * mult)
        numcount += 1

    print("Input is an integer.\n")
    print("The reverse of", n, "is", res)

except ValueError:
    print("Input is a string.\n")
    for i in n:
        lst.append(i)

    for i in range(len(lst) - 1, -1, -1):
        res1 = res1 + lst[i]

    print("The reverse of", n, "is", res1)
