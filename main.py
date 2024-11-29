# OBJECT ORIENTED PROGRAMMING - PYTHON, ABSTRACTION
# CREATING CLASSES IN PYTHON, UNDERLYING CONCEPTS AND IDEAS

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

# Creating the instances for the class -> Instantiation
civic = Car("Honda", "Civic", "2018") # -> Object for the Class CAR
civic.start_engine()     # output -> the car of this make - Engine has started...
civic.display_car_info() # output -> info attached to the car

sample_list:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def capitalize(lst:list):
    return (word.upper() for word in lst)

capitalized_words:list = capitalize(sample_list)

for word in capitalized_words:
    print(word)