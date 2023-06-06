import pygame
import random
import math
from Dingo import Dingo

class Jingo:
    def __init__(self, win,length,width, energy, speed, power, health, position, resistance):
        self.gender = random.choice(['male', 'female'])
        self.energy = energy
        self.speed = speed
        self.power = power
        self.health = health
        self.position = position
        self.resistance = resistance
        self.radius = 5
        self.length = length
        self.width = width
        self.win = win
        self.color = (255, 0, 0)
        self.energy = 100
        self.attack_power = 20
        self.is_attacking = False
        self.is_dead = False
        self.target = None
        self.infection_chance = 0.1  # Default infection chance
      
    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.position[0], self.position[1]), self.radius, 0)


    def move(self):
        x, y = self.position
        dx, dy = random.choice([[1, 0], [-1, 0], [0, 1], [0, -1]])
        if dx == 1:
            new_x = x + dx + self.speed 
        else:
            new_x = x - dx - self.speed
        if dy == 1:
            new_y = y + dy + self.speed
        else:
            new_y = y - dy - self.speed
        # Check if new position is inside the window
        if (self.radius <= new_x <= self.win.get_width() - self.radius) and \
                (self.radius <= new_y <= self.win.get_height() - self.radius):
            self.position = [new_x, new_y]
            self.energy -= 1  # Moving costs energy
        self.draw()
        
        
    def infect(self, duration):
        """Infect the animal."""
        self.infection_chance = 0.8  # Increase infection chance when infected
        # Other infection logic...


    def cure(self):
        """Cure the animal."""
        self.infection_chance = 0.1  # Reset infection chance after cure
        # Other cure logic..


    def detect_closest_animal(self, mania_animals):
        min_distance = float("inf")
        closest_animal = None
        for animal in mania_animals:
            if animal != self and self.get_distance(animal) <= self.radius + animal.radius and animal is not isinstance(animal,Jingo):
                distance = self.get_distance(animal)
                if distance < min_distance:
                    min_distance = distance
                    closest_animal = animal
                    self.target = closest_animal
        return closest_animal
    
    
    def get_distance(self, other_animal):
        dx = self.position[0] - other_animal.position[0]
        dy = self.position[1] - other_animal.position[1]
        return math.sqrt(dx ** 2 + dy ** 2)


    def attack(self, mania_animal,):
        if self.target is not None:
            pygame.draw.line(self.win,(255,0,0),self.position,mania_animal.position,4)
            pygame.draw.circle(self.win, (255,0,0), mania_animal.position, 100,2)
            pygame.display.update()
            if self.get_distance(self.target) <= self.radius + self.target.radius:
                self.target.health -= self.attack_power
                if self.target.health <= 0:
                    self.target.is_dead = True
                    if self.target.stage == 4:
                        self.energy += 50
                        self.health += 50
                        self.resistance += 100
                        self.speed += 2
                        self.radius += 2
                    else:
                        self.energy += 50
                    self.is_attacking = False
                    self.target = None
            else:
                self.move_towards_target()
        else:
            self.is_attacking = False


    def move_towards_target(self):
        dx = self.target.position[0] - self.position[0]
        dy = self.target.position[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx = dx / distance
            dy = dy / distance
            self.position[0] += dx * self.speed
            self.position[1] += dy * self.speed
        self.draw()
        

    def reproduce(self, other_bingo, mania):
        if self.gender != other_bingo.gender and self.energy > 50 and other_bingo.energy > 50:
            child_position = self.position  #Child has same position as parent
            child_energy = random.randint(20, 80)
            child_speed = random.randint(1, 5)
            child_power = random.randint(1, 5)
            child_health = random.randint(1, 5)
            child_resistance = random.randint(1, 5)
            child_jingo = Jingo(self.win, self.length,self.width, child_energy, child_speed, child_power, child_health, child_position, child_resistance)
            mania.add_animal(child_jingo)
            self.energy -= 20
            other_bingo.energy -= 20
