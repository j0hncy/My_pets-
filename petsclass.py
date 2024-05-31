import random

class Cat:
    def __init__(self, initial_name="kitty"):
        self.name = initial_name
        self.name_history = [initial_name]  # Initialize name history with initial name
        self.age = random.randint(5,10) # assigning random int between 5 and 10
        self.favoriteFood = None
        self.speak_counter = 0  # Counter to track the number of times the speak method is called
        self.new_age = self.age # Initializing new_age with default age

    def getName(self):
        return self.name
    
    def getNames(self):
        return self.name_history

    def getAge(self):
        return self.age

    def getFavoriteFood(self):
        return self.favoriteFood
    
    def speak(self, message=None):
        # speak method to see the response from the pet based on the input
        if message:
            reply = f"{self.name} says: {message}"
        else:
            reply = f"{self.name} says: meow"

        self.speak_counter += 1  # Increment the speak counter
        return reply
    
    def newAge(self):
        # check how many times the age should incremeneted
        quotient = self.speak_counter // 5
        self.new_age = self.age + quotient  # Incremenet age
        return self.new_age
    
    def getAverageNameLength(self):
        # function to get the average length of the all names given to pet
        total_length = 0
        for name in self.name_history:
            total_length += len(name)
        return total_length / len(self.name_history)

    def setName(self, newName):
        self.name = newName
        self.name_history.append(newName)  # Add the new name to the name history

    def setAge(self, newAge):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood
    
class Dog:
    # defining a Dog class doing same operation as Cat class
    def __init__(self, initial_name="Shadow"):
        self.name = initial_name
        self.name_history = [initial_name]
        self.age = random.randint(5,10)
        self.favoriteFood = None
        self.speak_counter = 0  
        self.new_age = self.age 

    def getName(self):
        return self.name
    
    def getNames(self):
        return self.name_history

    def getAge(self):
        return self.age

    def getFavoriteFood(self):
        return self.favoriteFood
    
    def speak(self, message=None):
        if message:
            reply = f"{self.name} says: {message}"
        else:
            reply = f"{self.name} says: Bow"

        self.speak_counter += 1
        return reply
    
    def newAge(self):
        quotient = self.speak_counter // 5
        self.new_age = self.age + quotient 
        return self.new_age
    
    def getAverageNameLength(self):
        total_length = 0
        for name in self.name_history:
            total_length += len(name)
        return total_length / len(self.name_history)

    def setName(self, newName):
        self.name = newName
        self.name_history.append(newName)

    def setAge(self, newAge):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood

class Data:
    def __init__(self, database):
        print("Connecting to database")
        self.cat_count = 0
        self.dog_count = 0

    def beginTran(self):
        print("Beginning a transaction")

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def insert(self, table, object):
        print(f"Inserting {object.getName()} into table {table}")
        if table == "Cat":
            self.cat_count += 1
        elif table == "Dog":
            self.dog_count += 1

    def count(self, table):
        if table == "Cat":
            return self.cat_count
        elif table == "Dog":
            return self.cat_count
        else:
            return 0
