
def NumOfNotes(total_amt):
    note_5,balance1 = divmod(total_amt,5)
    note_2,balance2 = divmod(balance1,2)
    note_1,balance3 = divmod(balance2,1)

    return note_5, note_2, note_1



if __name__ == "__main__":
    amount = int(input("Enter amount to redraw: "))
    
    note5, note2, note1 = NumOfNotes(total_amt=amount)

    print(f"Number of 5 cedis notes: {note5}" )
    print(f"Number of 2 cedis notes: {note2}" )
    print(f"Number of 1 cedis notes: {note1}" )