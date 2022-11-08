print("Welcome to the ATM Bank")
amount = int(input("Enter amount to redraw: "))

note5 = amount // 5
amount = amount - (note5 * 5)
note2 = amount // 2 
amount = amount - (note2 * 2)
note1 = amount // 1

# note_5,balance1 = divmod(amount,5)

# note_2,balance2 = divmod(balance1,2)

# note_1,balance3 = divmod(balance2,1)


# print(f"GHc 5 = {note_5}")
# print(f"GHc 2 = {note_2}")
# print(f"GHc 1 = {note_1}")

def NumOfNotes():
    print(f'{"Number of 5 cedis notes: "}{note5}')
    print(f'{"Number of 2 cedis notes: "}{note2}')
    print(f'{"Number of 1 cedi notes: "}{note1}')

NumOfNotes()

onenote = int(input("Enter the amount you want in 1 cedi notes: "))  
twonote = int(input("Enter the amount you want  in 2 cedis notes: "))  
fivenote = int(input("Enter the amount you want in 5 cedis notes: ")) 
tennote = int(input("Enter the amount you want in 10 cedis notes: "))  
twentynote = int(input("Enter the amount you want in 20 cedis notes: ")) 
fiftynote = int(input("Enter the amount you want in 50 cedis notes: "))  


def NotesDespensed():
     print(f'{"Number of 1 cedis notes: "}{onenote//1}')
     print(f'{"Number of 2 cedis notes: "}{twonote//2}')
     print(f'{"Number of 5 cedis notes: "}{fivenote//5}')
     print(f'{"Number of 10 cedis notes: "}{tennote//10}')
     print(f'{"Number of 20 cedis notes: "}{twentynote//20}')
     print(f'{"Number of 50 cedis notes: "}{fiftynote//50}')

NotesDespensed()

def total():
    total = (onenote * 1) + (twonote * 2) + (fivenote * 5) + (tennote * 10) + (twentynote * 20) + (fiftynote * 50)
    print(f'{"Total amount to redraw is: "}{total}')