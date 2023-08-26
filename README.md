# Programming-in-Python-Coursera-
This Python script defines a 'Clothing' class along with its subclasses 'shirt' and 'pants'. The purpose of the script is to manage and track the stock of different types of clothing items based on their material.

Here's a breakdown of the script:

1. The 'Clothing' class is defined with a class variable 'stock' that stores the information about clothing items in the form of lists ('name', 'material', and 'amount'). The constructor '__init__' initializes an instance variable 'name'.
2. The 'add_item' method is used to add items to the stock. It appends the name, material, and amount of an item to the corresponding lists in the stock dictionary.
3. The 'Stock_by_Material' method is used to calculate and return the total stock amount for a given material. It iterates through the stock data and accumulates the total amount for the specified material.
4. Two subclasses, 'shirt' and 'pants', inherit from the 'Clothing' class. Each subclass specifies a default material.
5. Instances of 'shirt' and 'pants' are created with the names "Polo" and "Sweatpants," respectively. The 'add_item' method is called on these instances to add items to the stock.
6. The 'Stock_by_Material' method is called on the 'polo' instance to get the current stock amount of items with the material "Cotton."
7. The result is printed, showing the total stock amount for the material "Cotton."

Note: There's a small issue in the 'Clothing' class where the 'material' variable is defined in the constructor but is not used anywhere. To fix this, you should use the instance variable 'self.material' instead of the local variable 'material'...
