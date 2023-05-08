
n_row = 20
n_col = 26
seating = []

def createSeats():
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append('.')
        seating.append(row)

def printLines():
    for i in range(80):
        print('-', end ='')
    print()

def viewSeating():
    printLines()
    print("Seating")
    printLines()

    print(" ", end = "\t")
    for i in range(n_col):
        print(chr(i+65), end = " ")
    print(" ", end = "\t")
    print("type", end = "\t")
    print("price", end = "\n")

    print(" ", end = "\t")
    for i in range (n_col * 2):
        print("-", end = "")
    print(" ", end = "\t")
    print("-----", end = "\t")
    print("-----", end = "\n")

    for r in range(n_row):
        print(r+1, end="\t")
        for c in range(n_col):
            print(seating[r][c], end=" ")
        print(" ", end = "\t")
        if (r < 5):
            print("front", end = "\t")
            print("$80", end = "\n")
        elif (r < 11):
            print("middle", end = "\t")
            print("$50", end = "\n")

        elif(r < 21):
            print("back", end = "\t")
            print("$80", end = "\n")


def printMenu():
    printLines()
    print('Outdoor Park Concert App', end="\n")
    printLines()
    print('[b] buy')
    print('[v] view seating')
    print('[s] search for a customer by name and display the tickets purchased')
    print('[d] display all the purchases made and the total amount of income')
    print('[q] to quit')

createSeats()
printMenu()
command = input("Enter a command: ")
match command:
    case 'v':   
        viewSeating()

