menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    
    print('Calculating bill subtotal...')
    subtotal = 0.0
    for item in order:
        subtotal += item['price']
    return subtotal

def calculate_tax(subtotal):
    
    print('Calculating tax from subtotal...')
    tax = subtotal * 0.15
    rounded_tax = round(tax, 2)
    return rounded_tax

def summarize_order(order):
    
    print_order(order)
    #calculate subtotal
    subtotal = calculate_subtotal(order)
    #calculate tax
    tax = calculate_tax(subtotal)
    #calculate total
    total = subtotal + tax
    rounded_total = round(total, 2)
    #create a list of items names
    names = [item['name'] for item in order]
    return names, rounded_total

#will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
'''
def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)
    print("The grand total is: " + str(subtotal))

if __name__ == "__main__":
    main()


