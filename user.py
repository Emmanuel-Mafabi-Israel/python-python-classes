class User:
    # class attributes - global to the class
    ROLES:list = ["admin", "local"]

    all_users:dict = {}
    user_count:int = 0

    def __init__(self, user_name:str, user_role:str):
        # Instance Suite, Scope - Unshared among instances...
        self.user_name = user_name
        self.user_role = user_role

    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Invalid credentials given... ref: user!")
        else:
            # successful validation...
            self._user_name = value
            User.increase_user_count() # auto increment whenever a new user is created...
            User.store_user(self.user_name) # store the created user after instantiation...

    @property
    def user_role(self):
        return self._user_role
    
    @user_role.setter
    def user_role(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Invalid credentials given... ref: role!")
        else:
            # successful validation...
            self._user_role = value

    @classmethod
    def print_instances(cls)->str:
        return f"User - instances created: {cls.user_count}"
    
    @classmethod
    def increase_user_count(cls, increment:int = 1)->None:
        cls.user_count += increment

    @classmethod
    def store_user(cls, user:str)->None:
        cls.all_users.append(user)

    @classmethod
    def retrieve_stored_users(cls)->list:
        return [user for user in cls.all_users]

user_0 = User("Emmanuel") # first instance
user_1 = User("Wendy")    # second instance
print(User.print_instances())
print(User.retrieve_stored_users())