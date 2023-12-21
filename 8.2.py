def cashier():
    # Get the price of the item
    price = float(input("Enter the price of the item: "))
    # Get the amount of payment
    payment = float(input("Enter the payment: "))

    # List of banknotes
    banknotes = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]

    # Calculate the change
    change = payment - price

    # Create a dictionary to store the change
    change_dict = {note: 0 for note in banknotes}

    # Calculate the number of each banknote
    for note in banknotes:
        while change >= note:
            change -= note
            change_dict[note] += 1

    # Print the change
    print("Change: ", change_dict)

# Run the cashier function
cashier()






#heco con inteligencia artificial 