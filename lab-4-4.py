weight = float(input())
ticketPrice = float(input())
if weight <= 15:
    finalPrice = ticketPrice - 10
else:
    finalPrice = weight - 15 * 4
print(finalPrice)
