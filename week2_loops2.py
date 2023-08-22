import json

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

def main():
    # Convert the menu dictionary to JSON
    menu_json = json.dumps(menu, indent=4)  # Indent for pretty formatting

    # Print the JSON representation of the menu
    print(menu_json)

    # Rest of your main function...

if __name__ == "__main__":
    main()