# Programming-in-Python-Coursera-
This Python script defines a simple example of abstract base classes and inheritance using two classes: 'Bank' and 'Swiss'.

1. 'Bank' Class:
   - This class is defined as an abstract base class (ABC) by inheriting from the 'ABC' class from the 'abc' module.
   - It includes a non-abstract method 'basicinfo()' that prints "This is a generic bank" and returns the string "Generic Bank: 0".
   - It also includes an abstract method 'withdraw()', marked with the '@abstractmethod' decorator, which is meant to be overridden by derived classes.

2. 'Swiss' Class:
   - This class inherits from the 'Bank' class.
   - It has a constructor '__init__()' that initializes the class variable bal to 1000.
   - It overrides the 'basicinfo()' method to print "This is the Swiss Bank" and return a string with "Swiss Bank: {self.bal}".
   - It implements the 'withdraw(amount)' method, which deducts the specified amount from the 'bal' balance. If the withdrawal amount is greater than the 
     balance, it prints "Insufficient funds" and does not deduct any money.

3. 'main()' Function:
   - This function is the entry point of the script.
   - It checks if 'Bank' is a subclass of 'ABC'.
   - It creates an instance of the 'Swiss' class.
   - It calls the 'basicinfo()' method of the 'Swiss' instance and prints the returned value.
   - It calls the 'withdraw()' method twice with different withdrawal amounts.

The script demonstrates the concept of abstract classes and method overloading in Python, using the 'ABC' module. The 'Bank' class defines the structure and interface, while the 'Swiss' class provides specific implementation details for a Swiss bank.
