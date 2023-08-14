# Programming-in-Python-Coursera-
Coding Exercises of the Course

This Python script represents a simple program for ordering items from a menu and calculating the bill. Here's a breakdown of the script's components:

1. Menu Dictionary (menu): This dictionary stores menu items as key-value pairs. Each key represents a menu item number, and the corresponding value is a dictionary containing the item's name and price.
2. Function 'calculate_subtotal(order):' This function takes a list of ordered items ('order') as input and calculates the subtotal by summing up the prices of all items in the order.
3. Function 'calculate_tax(subtotal):' This function calculates the tax from the subtotal. It multiplies the subtotal by 0.15 (15%) to calculate the tax amount and then rounds it to two decimal places.
4. Function 'summarize_order(order):' This function summarizes the order by calling the 'print_order' function, calculating the subtotal and tax, and then calculating the total by adding the subtotal and tax. It also creates a list of item names and returns both the item names and the rounded total.
5. Function 'print_order(order):' This function prints the number of items in the order and the names of the ordered items.
6. Function 'display_menu():' This function displays the menu items with their corresponding numbers, names, and prices.
7. Function 'take_order():' This function allows the user to select menu items by displaying the menu and prompting the user to input item numbers. It creates an 'order' list containing dictionaries of the selected items.
8. Function 'main():' This is the main function that orchestrates the entire process. It calls 'take_order' to create an order, then calls other functions to print the order details, calculate subtotal, tax, and total, and finally summarizes the order by printing the grand total.
9. 'if __name__ == "__main__":' This block ensures that the 'main()' function is executed only if the script is run directly, not if it's imported as a module.

Overall, this script simulates a simple order processing system for a menu, calculates the subtotal, tax, and total amount, and provides the user with a summary of their order.
