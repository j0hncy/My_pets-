from petsclass import Cat, Data, Dog

# Connect to the database 
data = Data("database")

def saveTest():
    # Create a Cat object with a name
    cat = Cat("Grafield")
#    cat.setName("Grafield")
    dog = Dog("Bruno")
#    dog.setName("Bruno")
   
    # Begin a transaction
    data.beginTran()
    
    # Insert the Cat object into the database
    data.insert("Cat", cat)
    data.insert("Dog", dog)
    
    # Commit the transaction
    data.commit()
    print("All pets added to Database successfully.")

def savePetShop():
    # Create an empty list to store the Cat objects
    cats = []
    # Iterate three times using a for loop
    for i in range(3):
    # Create a new Cat object and append it to the list
        cat = Cat()
        cats.append(cat)
#    print ("cats:", cats)

    dogs = []
    for i in range(3):
        dog = Dog()
        dogs.append(dog)
#    print ("dogs:", dogs)

    data.beginTran()

    for cat in cats:
        data.insert("Cat", cat)
        
        # Insert all Dog objects into the database
    for dog in dogs:
        data.insert("Dog", dog)
        
        # Commit the transaction if all insertions succeed
    data.commit()
    print("All pets added to Database successfully.")

def logStats():
    print("Logging script execution statistics:")
    # Count the number of pets in the database after saving
    count_cat = data.count("Cat")
    count_dog = data.count("Dog")
    
    print(f"Total number of cats in the database: {count_cat}")
    print(f"Total number of dogs in the database: {count_dog}")
        
saveTest()
print ("===================================")
savePetShop()
print ("===================================")
logStats()



