TotalCoffee = 3.50 * 2
TotalMuffin = 2.10 * 3
TotalWater = 1.05 * 4
Subtotal = TotalCoffee + TotalMuffin + TotalWater
Tax = Subtotal * 0.06
Total =  Subtotal + Tax
Receipt = f"========== RECEIPT ==========\nItem\t\tPrice\tQty\tTotal\nCoffee\t\t$3.50\t2\t${TotalCoffee}\nMuffin\t\t$2.10\t3\t${TotalMuffin}\nWater\t\t$1.05\t4\t${TotalWater}\n------------------------------\nSubtotal\t\t\t${Subtotal}\nTax (6%)\t\t\t${Tax}\nTotal\t\t\t${Total}\n=============================="
print(Receipt)