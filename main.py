
from receipt import receipt
import json

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
        print(r, end="\t")
        for c in range(n_col):
            print(seating[r][c], end=" ")
        print(" ", end = "\t")
        if (r < 5):
            print("front", end = "\t")
            print("$80", end = "\n")
        elif (r < 11):
            print("middle", end = "\t")
            print("$50", end = "\n")
        else:
            print("back", end = "\t")
            print("$25", end = "\n")


def printMenu():
    printLines()
    print('Outdoor Park Concert App', end="\n")
    printLines()
    print('[b] buy')
    print('[v] view seating')
    print('[s] search for a customer by name and display the tickets purchased')
    print('[d] display all the purchases made and the total amount of income')
    print('[q] to quit')

def buyTickets():
    numberOfTickets = int(input("Number of seats to buy: "))
    startingSeat = input("Starting seat (ex. 3D): ")
    row = int(startingSeat[:-1])
    column = ord(startingSeat[len(startingSeat) - 1]) - 65
    
    #set price and seat price
    if (row < 5):
        price = 80
        seatType = "front"
    elif(row < 11):
        price = 50
        seatType = "middle"
    else:
        price = 25
        seatType = "back"
    
    #check if seats are available
    available = True
    for i in range(numberOfTickets):
        if (seating[row][column + i] != '.'):
            available = False
    if (available == False):
        print("The seats you chose are not available for purchase. Please try again.")
        return
    
    print(numberOfTickets, " seats starting at (", startingSeat, ") are available for purchase", end = "\n")
    name = input("Enter your name: ")
    email = input("Enter your email address: ")

    #reserves seats
    for i in range (numberOfTickets):
        seating[row][column + i] = "X"
    spaceLeft = 2
    spaceRight = 2
    for i in range (2, 0, -1):
        if (column < i):
            spaceLeft -= 1
    for i in range (24, 26):
        if (column + numberOfTickets > i):
            spaceRight -= 1

    for i in range (1, spaceLeft + 1):
        seating[row][column - i] = 'E'
    for i in range (0, spaceRight):
        seating[row][column + numberOfTickets + i] = 'E'

    if (row != 0):
        for i in range (numberOfTickets + spaceLeft + spaceRight):
            seating[row - 1][column - spaceLeft + i] = 'E'
    if (row != 19):
        for i in range (numberOfTickets + spaceLeft + spaceRight):
            seating[row + 1][column - spaceLeft + i] = 'E'

    purchases.append(receipt(name, email, numberOfTickets, seatType, startingSeat, price))
    printLines()
    print("Receipt")
    purchases[-1].printReceipt()

def searchCustomer():
    printLines()
    print("Search for Attendee")
    printLines()
    customer = input("Enter an attendee: ")
    for element in purchases:
        if (element.name == customer):
            element.printReceipt()
            return
    print("Attendee was not found")
    
def displayAll():
    printLines()
    print("Display All Purchases")
    printLines()
    for element in purchases:
        element.printReceipt()

def convertJson(): 
    for element in purchases:
        jsonData.append(json.dumps(element.__dict__))


createSeats()
purchases = []
jsonData = []
command = ""

while (command != 'q'):
    printMenu()
    command = input("Enter a command: ")
    match command:
        case 'b': 
            buyTickets()
        case 'v':   
            viewSeating()
        case 's':
            searchCustomer()
        case 'd':
            displayAll()
convertJson()
print(jsonData[0])
print(type(jsonData[0]))

