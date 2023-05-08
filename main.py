
n_row = 20
n_col = 26
seating = []

def createSeats():
    for r in range(n_row):
        row = []
        for c in range(n_col):
            row.append('.')
        seating.append(row)

def printSeats():
    for r in range(n_row):
        print(r+1, end="\t")
        for c in range(n_col):
            print(seating[r][c], end=" ")
        print()

def printLines():
    for i in range(80):
        print('-', end ='')
    print()

def printMenu():
    printLines()
    print('Outdoor Park Concert App', end="\n")
    printLines()
    print('[b] buy')
    print('[v] view seating')
    print('[s] search for a customer by name and display the tickets purchased')
    print('[d] display all the purchases made and the total amount of income')
    print('[q] to quit')

printMenu()
