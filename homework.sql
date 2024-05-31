-- Create table for dogs
CREATE TABLE Dogs (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    FavoriteFood VARCHAR(100),
    SpeakCounter INT,
    CONSTRAINT CHK_Age CHECK (Age >= 0),  -- Ensure age is non-negative
    CONSTRAINT CHK_SpeakCounter CHECK (SpeakCounter >= 0)  -- Ensure speak counter is non-negative
);

-- Create table for cats
CREATE TABLE Cats (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    FavoriteFood VARCHAR(100),
    SpeakCounter INT,
    CONSTRAINT CHK_Age CHECK (Age >= 0),  -- Ensure age is non-negative
    CONSTRAINT CHK_SpeakCounter CHECK (SpeakCounter >= 0)  -- Ensure speak counter is non-negative
);

-- Sample insert statements for dogs
INSERT INTO Dogs (ID, Name, Age, FavoriteFood, SpeakCounter)
VALUES (1, 'Buddy', 7, 'Bones', 10),
       (2, 'Max', 5, 'Chicken', 7),
       (3, 'Bailey', 6, 'Beef', 12);

-- Sample insert statements for cats
INSERT INTO Cats (ID, Name, Age, FavoriteFood, SpeakCounter)
VALUES (1, 'Whiskers', 6, 'Fish', 8),
       (2, 'Mittens', 8, 'Tuna', 5),
       (3, 'Felix', 7, 'Salmon', 10);
