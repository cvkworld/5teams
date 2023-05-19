import random

class Hunter:
    def __init__(self, bullet_count, hunger_level, kilometers_traveled, position):
        self.bullet_count = bullet_count
        self.hunger_level = hunger_level
        self.kilometers_traveled = kilometers_traveled
        self.position = position
    
    def hunt(self, forest):
        self.bullet_count -= 1
        self.kilometers_traveled += random.randint(1, 3)
        self.hunger_level += random.randint(1, 2)
        
        for rabbit in forest.rabbits:
            if rabbit.position == self.position:
                self.hunger_level -= 5
                forest.rabbits.remove(rabbit)
        
        for burrow in forest.burrows:
            if burrow.position == self.position and not burrow.occupied:
                burrow.occupied = True
                self.hunger_level -= 2
                break

class Rabbit:
    def __init__(self, speed, color, kilometers_traveled, position):
        self.speed = speed
        self.color = color
        self.kilometers_traveled = kilometers_traveled
        self.position = position
    
    def flee(self):
        self.kilometers_traveled += random.randint(1, 3)

class Burrow:
    def __init__(self, position):
        self.position = position
        self.occupied = False

class Forest:
    def __init__(self, burrows, rabbits, total_square_kilometers, trees_hiding_rabbit):
        self.burrows = burrows
        self.rabbits = rabbits
        self.total_square_kilometers = total_square_kilometers
        self.trees_hiding_rabbit = trees_hiding_rabbit

# Create a hunter
hunter = Hunter(bullet_count=3, hunger_level=7, kilometers_traveled=0, position=(0, 0))

# Create a forest with rabbits and burrows
burrows = [Burrow(position=(0, 1)), Burrow(position=(2, 2)), Burrow(position=(3, 3))]
rabbits = [Rabbit(speed=8, color='white', kilometers_traveled=0, position=(1, 1)),
           Rabbit(speed=5, color='brown', kilometers_traveled=0, position=(4, 4)),
           Rabbit(speed=9, color='brown', kilometers_traveled=0, position=(2, 3))]
forest = Forest(burrows=burrows, rabbits=rabbits, total_square_kilometers=5, trees_hiding_rabbit=30)

# Automatic routine for interaction
hunter.hunt(forest)
print("Hunter bullet count:", hunter.bullet_count)
print("Hunter hunger level:", hunter.hunger_level)
print("Hunter kilometers traveled:", hunter.kilometers_traveled)
print()

for rabbit in forest.rabbits:
    rabbit.flee()
    print("Rabbit kilometers traveled:", rabbit.kilometers_traveled)
print()

for burrow in forest.burrows:
    print("Burrow position:", burrow.position)
    print("Burrow occupied:", burrow.occupied)
