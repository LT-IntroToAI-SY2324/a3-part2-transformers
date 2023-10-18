import random

fortnite_locations = ["Tilted Towers", 
                      "Pleasant Park", 
                      "Salty Springs", 
                      "Retail Row", 
                      "Lazy Lake", 
                      "Holly Hedges", 
                      "Sweaty Sands", 
                      "Craggy Cliffs", 
                      "Steamy Stacks", 
                      "Misty Meadows", 
                      "The Authority", 
                      "Weeping Woods", 
                      "Slurpy Swamp", 
                      "Frenzy Farm", 
                      "Dirty Docks", 
                      "Catty Corner", 
                      "Grappler Grotto", 
                      "Risky Reels"]
random_location = random.choice(fortnite_locations)
print("Randomly chose Fortnite location: " + random_location)