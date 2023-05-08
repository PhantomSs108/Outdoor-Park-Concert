
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
    row = int(startingSeat[0])
    column = ord(startingSeat[1]) - 65
    
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
    
    try:
        for i in range (numberOfTickets + 4):
            seating[row - 1][column - 2 + i] = "E"
    except IndexError:
        pass

    try:
        for i in range (numberOfTickets + 4):
            seating[row + 1][column - 2 + i] = "E"
    except IndexError:
        pass

    try:
        seating[row][column + numberOfTickets] = "E"
    except IndexError:
        pass
    
    try:
        seating[row][column + numberOfTickets + 1] = "E"
    except IndexError:
        pass

    try:
        seating[row][column - 1] = "E"
    except IndexError:
        pass

    try:
        seating[row][column - 2] = "E"
    except IndexError:
        pass

    #calculate costs and print receipt
    printLines()
    print("Receipt")
    printLines()
    print("Name:", "\t", "\t", end = "\t")
    print(name)
    print("Email:", "\t", "\t", end = "\t")
    print(email)
    print("Number of Tickets:", end = "\t")
    print(numberOfTickets)
    print("Seat Type:", "\t", end = "\t")
    print(seatType)
    print("Seats: ", "\t", end = "\t")
    for i in range (numberOfTickets):
        print(startingSeat[0], chr(ord(startingSeat[1]) + i), sep = '', end = " ")
    print()
    print("Ticket Cost:", "\t", end = "\t")
    ticketCosts = price * numberOfTickets
    print(f"${ticketCosts:.2f}")
    print("Mask Fee: ", "\t", end = "\t")
    maskFee = numberOfTickets * 5
    print(f"${maskFee:.2f}")
    print("Sub-total: ", "\t", end = "\t")
    subtotal = price * numberOfTickets + numberOfTickets * 5
    print(f"${subtotal:.2f}")
    tax = subtotal * 0.0725
    total = subtotal + tax
    print("Tax:", "\t", "\t", end = "\t")
    print(f"${tax:.2f}")
    printLines()
    print("Total:", "\t", "\t", end = "\t")
    print(total)
    printLines()



createSeats()
command = ""

while (command != 'q'):
    printMenu()
    command = input("Enter a command: ")
    match command:
        case 'b': 
            buyTickets()
        case 'v':   
            viewSeating()

