
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