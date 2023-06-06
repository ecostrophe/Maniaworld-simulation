import random
import pygame
from Mingo import Mingo
from Dingo import Dingo
from Jingo import Jingo
from Journey import Journey

class Pandemic:
    def __init__(self, screen, probability, journey:Journey):
        self.probability = probability  # Probability of getting infected (0-1)
        self.journey = journey  # Journey object for duration
        self.infected = []  # List of infected animals
        self.screen = screen  # Pygame screen object
    
    def infect_animals(self, animals):
        """Infect animals in the environment with a certain probability."""
        for animal in animals:
            if isinstance(animal, (Mingo, Dingo, Jingo)):
                if random.random() <= self.probability and animal not in self.infected:
                    animal.infect(self.journey.get_duration())
                    self.infected.append(animal)
                    pygame.draw.circle(self.screen, (255, 0, 0), (animal.position[0], animal.position[1]), 50, 2)
                    # Draw red circle around infected animal
    
    def spread_infection(self, animals):
        """Spread the infection to other animals in the environment."""
        newly_infected = []
        for infected_animal in self.infected:
            for animal in animals:
                if animal != infected_animal and random.random() <= infected_animal.infection_chance and animal not in self.infected:
                    animal.infect(self.journey.get_duration())
                    newly_infected.append(animal)
                    pygame.draw.circle(self.screen, (255, 0, 0), (animal.position[0], animal.position[1]), 10, 2)
                    # Draw red circle around newly infected animal
        self.infected.extend(newly_infected)
    
    def clear_infection(self):
        """Clear the list of infected animals."""
        for animal in self.infected:
            animal.cure()
        self.infected = []
    
    def update(self, animals):
        """Update the pandemic for the next simulation step."""
        self.spread_infection(animals)
        self.clear_infection()
        self.infect_animals(animals)
