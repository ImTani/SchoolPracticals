print("Bank Management")
print("1. Check Info")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

while True:
    a = int(input("Enter Your Choice : "))
    if a == 1:
        print("Info : none")
    elif a == 2:
        print("How much depposit?")
    elif a == 3:
        print("How much withdraw?")
    elif a == 4:
        print("OkBye")
        break
    else:
        print("Bro cant even read smh. Go ahead, try again.")
