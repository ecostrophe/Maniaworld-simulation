import pygame
import random
from Mingo import Mingo
from Jingo import Jingo
from Dingo import Dingo

class Mania:
    def __init__(self,win,weather, num_mingo,num_jingo,num_dingo,length, width):
        self.length = length
        self.width = width
        self.weather = weather
        self.num_mingo = num_mingo
        self.num_jingo = num_jingo
        self.num_dingo = num_dingo
        self.animals = []  # List of animal objects in the environment
        self.plants = [] #List of plants in the environment
        self.count_species = [0,0,0]
        self.win = win

    def add_animal(self, animal):
        """Add an animal to the list of animals in the environment."""
        self.animals.append(animal)
        
    def add_plant(self, plant):
        """Add an plants to the list of animals in the environment."""
        self.plants.append(plant)

    def add_species(self):
        #add the animals to the manialand
        #add Mingos plants
        for i in range(self.num_mingo):
            Position= [random.randint(50,1050),random.randint(50,890)]
            mingo = Mingo(Position, self.win)
            self.add_plant(mingo)
        #add Jingos
        for i in range(self.num_jingo):
            energy = random.randint(20, 80)
            speed = random.randint(1, 5)
            power = random.randint(1, 5)
            health = random.randint(1, 5)
            position= [random.randint(150,800),random.randint(150,800)]
            resistance = random.randint(1, 5)
            jingo = Jingo(self.win, self.length, self.width, energy,speed,power,health,position,resistance)
            self.add_animal(jingo)
            #add Dingo
        for i in range(self.num_dingo):
            energy = random.randint(20, 80)
            speed = random.randint(1, 5)
            power = random.randint(1, 5)
            health = random.randint(1, 5)
            position= [random.randint(150,800),random.randint(150,800)]
            resistance = random.randint(1, 5)
            dingo = Dingo(energy,speed,power,health,resistance,position,self.win)
            self.add_animal(dingo)

    def count_animals(self):
        self.count_species =[0,0,0]
        for plant in self.plants:
            if isinstance(plant, Mingo):
                self.count_species[0] += 1

        for animal in self.animals:
            if isinstance(animal, Jingo):
                self.count_species[1] += 1
            elif isinstance(animal, Dingo):
                self.count_species[2] += 1
            else:
                pass

    def simulate_environment(self):
        """Simulate the environment by changing weather and animal properties."""
        self.weather.set_weather()
        
    def launch_species(self):
        for plant in self.plants:
            if plant.is_dead:
                self.plants.remove(plant)
            else:
                plant.draw()
                plant.update(self.weather.temperature,self.weather.humidity,self.weather.precipitation,self.plants)
            
        for animal in self.animals:
            animal.draw()
            pygame.display.update()
            if isinstance(animal, (Jingo,Dingo)):
                #follow test
                if isinstance(animal,Dingo):
                    prey=animal.detect_closest_animal(self.animals)
                    if prey is not None:
                        animal.attack(prey)
                        if prey.is_dead:
                            self.animals.remove(prey)
                elif isinstance(animal,Jingo):
                    prey=animal.detect_closest_animal(self.plants)
                    if prey is not None:
                        animal.attack(prey)
                        if prey.is_dead:
                            self.plants.remove(prey)
                animal.move()
                animal.draw()
        #pygame.display.update()
