#Get user input on age and ticketPrice
age = int(input("Enter your age: "))
ticketPrice = float(input("Enter the price of the movie ticket: "))

# Invalid inputs 
if age < 0 or ticketPrice <= 0:
    print("Invalid input. Age cannot be negative and ticket price must be greater than 0.")
else:
    #Determine the category, discount percentage and discount price
    if age <= 12:
        category = "Children"
        discountPercentage = "50%"
        discountPrice = ticketPrice - (ticketPrice * 0.5)
    elif age <= 17:
        category = "Teenagers"
        discountPercentage = "25%"
        discountPrice = ticketPrice - (ticketPrice * 0.25)
    else:
        category = "Adults"
        discountPercentage = "0%"
        discountPrice = ticketPrice

    #Output
    print(f"Category:{category} ")
    print(f"Discount percentage:{discountPercentage}")
    print(f"Discounted ticket price:${discountPrice:.2f}")