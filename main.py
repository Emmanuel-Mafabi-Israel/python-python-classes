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

    # Getter and Setter functions, for value check and assignations
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        # length check
        if len(make) > 0 and len(make) <= 20:
            self._make = make
        else:
            # error out
            raise ValueError(f"error: [car make] length should be between 0 - 20 chars long...")
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        # length check
        if len(model) > 0 and len(model) <= 20:
            self._model = model
        else:
            # error out
            raise ValueError(f"error: [car model] length should be between 0 - 20 chars long...")
        
    



# Creating the instances for the class -> Instantiation
civic = Car("Honda", "Civic", "2018") # -> Object for the Class CAR
civic.start_engine()     # output -> the car of this make - Engine has started...
civic.display_car_info() # output -> info attached to the car

# Inheritance
class SUV(Car):
    def __init__(self, make, model, year, gears:int):
        super().__init__(make, model, year)
        self.gears = gears

    def display_gears(self):
        print(f"{self.make} - {self.model} has {self.gears} gears...")

    @property
    def gears(self):
        return self._gears

    # --- an equivalent syntax ---
    #   def gears(self):
    #       return self._gears
    #   
    #   gears = property(gears)
    
    @gears.setter
    def gears(self, gears):
        if gears > 0:
            self._gears = gears
        else:
            raise ValueError("Number of gears should be greater than 0...")
        
_civic_ = SUV("Honda", "Civic", "2018", 4)
_civic_.display_gears()