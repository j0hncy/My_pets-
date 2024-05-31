# My_pets-

# How To Run
1. Clone this repository or Download the 3 python codes to your local system
•	petsclass.py
•	SavepetShop.py
•	unit_test.py
2. Open the terminal in your local system where python is installed
3. Execute the python code SavepetShop.py and verify output is as below:
   
![image](https://github.com/j0hncy/My_pets-/blob/main/output.png)

4. Execute the unit test code unit_test.py and verify the output as below:
   
Ran 2 tests in 0.000s
OK

# Implementation
petsclass.py -> This file contains the cat dog and database class and its methods. The methods are used to give different properties to Cat, Dog and database class. Functionalities of Cat and Dog Class are
1.	configure an initial name. While calling an object of the class it assigns an initial name to your pet.
2.	Assigns an age to your pet between 5 and 10
3.	Your pet (Cat and Dog) can speak to you when calling the method speak()
If you call this method either with message or without message. If you pass a message, pet will echo that message, else it will reply with the default message.
4.	This class can store all the names you pet ever had
5.	You can list all the names your pet ever had by calling the method getNames()
6.	If your pet speak / reply to you more then 5 times, your pet’s age gets increased by 1.
7.	You can get the average length of the names given to your pet by calling the method getAverageNameLength() 
SavepetShop.py -> This file is used to give inputs to the Cat and Dog Class defined in petsclass.py and save the data to the database.
1.	Here, saveTest() method will do below jobs for you:
a.	Create a cat with a name and insert it into the database.
b.	Create a dog with a name and insert it into the database.
2.	And savePetShop() method will do below jobs for you:
a.	Create three nameless cats.
b.	Create three nameless dogs.
c.	Insert all six pets into the database
3.	And logStats() method will print the total number of cat and dog in the data base

Homework.sql -> This file contains SQL statements to create table(s) to store our pet data and sample insert statements.

Unit_test.py -> This python code will do the unit testing of the code we have developed.
1.	Assert that a cat’s initial age is a random number between 5 and 10.
2.	Assert the speak() method is properly functioning.









