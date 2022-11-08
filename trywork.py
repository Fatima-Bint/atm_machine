if notes[3] == amount // 20 and notes[2] = amount MOD 20 / 10:
    print("and")

    elif (notes[3] == amount / 20 and notes[2] == amount % 20/ 10):
    print("Collect your money: ")
    print("    >> £20 Banknotes: " + notes[3])
    print("    >> £10 Banknotes: " + notes[2])
    print("Thank you for using this Python Bank ATM.")
    print("Good Bye.")
else:
    print("okay")

if ((amount % 10) != 0):
    print("You can only withdraw a multiple of ten!")

elif ((amount < 10) or (amount > 1000)):
    print("You can only withdraw between £10 and GHc 1000")