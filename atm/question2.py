

def NotesDespensed(onenote, twonote, fivenote, tennote, twentynote, fiftynote):
    one_1 = onenote//1
    two_2 = twonote//2
    five_5 = fivenote//5
    ten_10 = tennote//10
    twenty_20 = twentynote//20
    fifty_50 = fiftynote//50

    return one_1, two_2, five_5, ten_10, twenty_20, fifty_50

if __name__ == "__main__":
    
    onenote = int(input("Enter the amount you want in 1 cedi notes: "))  
    twonote = int(input("Enter the amount you want  in 2 cedis notes: "))  
    fivenote = int(input("Enter the amount you want in 5 cedis notes: ")) 
    tennote = int(input("Enter the amount you want in 10 cedis notes: "))  
    twentynote = int(input("Enter the amount you want in 20 cedis notes: ")) 
    fiftynote = int(input("Enter the amount you want in 50 cedis notes: "))  

    one_1, two_2, five_5, ten_10, twenty_20, fifty_50 = NotesDespensed(onenote,twonote,fiftynote,tennote, twentynote, fiftynote)

    print(f'{"Number of 1 cedis notes: "}{one_1}')
    print(f'{"Number of 2 cedis notes: "}{two_2}')
    print(f'{"Number of 5 cedis notes: "}{five_5}')
    print(f'{"Number of 10 cedis notes: "}{ten_10}')
    print(f'{"Number of 20 cedis notes: "}{twenty_20}')
    print(f'{"Number of 50 cedis notes: "}{fifty_50}')
