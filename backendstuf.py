import math

standard_Dict = {HP: 100, Stam: 50, Endurance: 20, Atk: 90}

if HP in standard_Dict:
    print("You have full health!")
    query = str(input("What is thine orders? /n"))
    for a in standard_Dict:
        print("There are", standard_Dict[:-5], "values in your character.")
