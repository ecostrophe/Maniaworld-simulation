import pygame
import random
import math

class Mingo:
    def __init__(self, position, win):
        self.energy = 100
        self.power = 50
        self.health = 100
        self.position = position
        self.resistance = random.uniform(0.1, 1)
        self.stage = 1
        self.radius = 5
        self.win = win
        self.color = (0, 255, 0)
        self.is_dead = False
        self.target = None
        self.infection_chance = random.uniform(0.1, 1)  # Default infection chance

    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.position[0], self.position[1]), self.radius, 0)
        if self.stage == 2:
            pygame.draw.circle(self.win, self.color, (self.position[0], self.position[1]), self.radius+5, 2)
        elif self.stage == 3:
            pygame.draw.circle(self.win, (255,110,255), (self.position[0], self.position[1]), self.radius, 0)
        elif self.stage == 4:
            pygame.draw.circle(self.win, (0,255,188), (self.position[0], self.position[1]), self.radius+5, 2)

    def grow(self, temperature, humidity, precipitation):
        if self.infection_chance < 0.7:
            if self.stage == 1:
                if temperature > 12 and humidity > 85 and precipitation > 3:
                    self.stage += 1
                    self.energy += 50
                    self.power += 25
                    self.health += 50
                    self.infection_chance += 0.1
            elif self.stage == 2 and self.infection_chance <= 0.6:
                if temperature > 5 and humidity > 75 and precipitation > 7:
                    self.stage += 1
                    self.energy += 50
                    self.power += 25
                    self.health += 50
                    self.radius += 1
                    self.infection_chance += 0.1
            elif self.stage == 3:
                if temperature > 26 and humidity > 42 and precipitation > 2:
                    self.stage += 1
                    self.energy += 50
                    self.power += 25
                    self.health += 50
                    self.radius +=1
                    
            elif self.stage >= 4 and self.infection_chance <= 0.5:
                if self.health >= 0:
                    self.is_dead = True
                else:
                    self.energy -= 5
                    self.power -= 5
                    self.health -= 5
                    self.resistance = 0
                    self.radius = 5
        else:
            if self.health >= 0:
                self.is_dead = True
            else:
                self.energy -= 5
                self.power -= 5
                self.health -= 5
                self.resistance = 0
                self.radius = 5
         
    def infect(self, duration):
        """Infect the animal."""
        self.infection_chance = 0.8  # Increase infection chance when infected
        # Other infection logic...

    def cure(self):
        """Cure the animal."""
        self.infection_chance = 0.1  # Reset infection chance after cure
        # Other cure logic...
     
    def detect_closest_plant(self, mania_plants):
        min_distance = float("inf")
        closest_plant = None
        for plant in mania_plants:
            if plant != self and self.get_distance(plant) <= self.radius + plant.radius:
                distance = self.get_distance(plant)
                if distance < min_distance:
                    min_distance = distance
                    closest_plant = plant
                    if self.stage >= 2 and plant.stage >= 2:
                        self.target = closest_plant
        return closest_plant
    
    
    def get_distance(self, other_plant):
        dx = self.position[0] - other_plant.position[0]
        dy = self.position[1] - other_plant.position[1]
        return math.sqrt(dx ** 2 + dy ** 2)

    def reproduce(self, other_plant, mania):
        child_position = self.position  #Child has same position as parent
        child_mingo = Mingo(self.win, child_position)
        mania.append(child_mingo)

    def update(self, temperature, humidity, precipitation, mania_plants):
        self.grow(temperature, humidity, precipitation)
        self.detect_closest_plant(mania_plants)
        if self.target is not None:
            self.reproduce(self.target, mania_plants)
 
    def __str__(self):
        return f"Mingo: Stage {self.stage}, Energy {self.energy}, Power {self.power}, Health {self.health}, Position {self.position}, Resistance {self.resistance}"