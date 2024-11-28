# Car Class in Python - Object Oriented Programming, By Israel Mafabi Emmanuel

Welcome to this beginner's guide to Object Oriented Programming (OOP) using Python. This README covers the basics of creating classes, defining methods, and using instance variables.

## Overview

In this example, we define a `Car` class that captures the essential details and behavior of a car. We will cover the following concepts:

- Class Definition
- Constructors
- Instance Variables
- Methods
- Instantiation



## Car Class

We define a `Car` class with the following structure:

```python
class Car:
    # Class suite
    # Class constructor -> __init__(self, ...)
    # sound:str = ""
    def __init__(self, make:str, model:str, year:str):
        # instance variables -> attributes, member variables
        self.make  = make
        self.model = model
        self.year  = year

    # class methods, member functions
    def start_engine(self):
        print(f"{self.make} - Engine has started...")

    def display_car_info(self):
        print(f"Car make: {self.make}, Car Model: {self.model}, Assembly Year: {self.year}")
```



## Instantiation

We create an instance of the `Car` Class and call its methods:

```python
civic = Car("Honda", "Civic", "2018") # -> Object for the Class CAR
civic.start_engine()     # output -> the car of this make - Engine has started...
civic.display_car_info() # output -> info attached to the car

```



## Additional Methods

To make the `Car`  class more interactive, we can add additional methods:

```python
def stop_engine(self):
    print(f"{self.make} - Engine has stopped...")

def honk_horn(self):
    print(f"{self.make} {self.model} - Honk! Honk!")

```



## New Usage

Here is how you can use the additional methods in  `Car` class:

```python
civic.stop_engine() # output -> the car of this make - Engine has stopped...
civic.honk_horn()   # output -> the car of this make and model - Honk! Honk!
```



## Acknowledgements

At Large and Most Importantly We give Glory to God!!!:

also A thank you 🤭😉 to Group One Members. 



## Conclusion

This example provides a foundational understanding of classes, instance variables, and methods in Python. By extending the `Car` class with more methods, we can see how OOP principles make code modular and reusable ~ so so easy!!! 😉🤭:

God Bless!!!

