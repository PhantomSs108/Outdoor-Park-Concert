
class receipt:

    def __init__(self, name, email, numberOfTickets, seatType, startingSeat, price):
        self.name = name
        self.email = email
        self.numberOfTickets = numberOfTickets
        self.seatType = seatType
        self.startingSeat = startingSeat
        self.price = price

    def printLines(self):
        for i in range(80):
            print('-', end ='')
        print()

    def printReceipt(self):
        self.printLines()
        print("Name:", "\t", "\t", end = "\t")
        print(self.name)
        print("Email:", "\t", "\t", end = "\t")
        print(self.email)
        print("Number of Tickets:", end = "\t")
        print(self.numberOfTickets)
        print("Seat Type:", "\t", end = "\t")
        print(self.seatType)
        print("Seats: ", "\t", end = "\t")
        for i in range (self.numberOfTickets):
            print(self.startingSeat[:-1], chr(ord(self.startingSeat[len(self.startingSeat) - 1]) + i), sep = '', end = " ")
        print()
        print("Ticket Cost:", "\t", end = "\t")
        ticketCosts = self.price * self.numberOfTickets
        print(f"${ticketCosts:.2f}")
        print("Mask Fee: ", "\t", end = "\t")
        maskFee = self.numberOfTickets * 5
        print(f"${maskFee:.2f}")
        print("Sub-total: ", "\t", end = "\t")
        subtotal = self.price * self.numberOfTickets + self.numberOfTickets * 5
        print(f"${subtotal:.2f}")
        tax = subtotal * 0.0725
        total = subtotal + tax
        print("Tax:", "\t", "\t", end = "\t")
        print(f"${tax:.2f}")
        self.printLines()
        print("Total:", "\t", "\t", end = "\t")
        print(total)
        self.printLines()