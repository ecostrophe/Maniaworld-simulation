import random
import pygame

class Disaster:
    def __init__(self, win):
        self.win = win
        self.type = random.choice(["hurricane", "earthquake", "wildfire"])
        self.is_active = False
        self.timer = 0
        self.color = (255, 0, 0)
        self.disaster_font = pygame.font.Font(None, 50)

    def activate(self):
        """Activate the disaster."""
        self.is_active = True
        self.timer = 100
        self.color = (255, 0, 0)
        if self.type == "hurricane":
            # Do something for hurricane
            pass
        elif self.type == "earthquake":
            # Do something for earthquake
            pass
        elif self.type == "wildfire":
            # Do something for wildfire
            pass

    def deactivate(self):
        """Deactivate the disaster."""
        self.is_active = False
        self.timer = 0
        self.color = (255, 255, 255)
        if self.type == "hurricane":
            # Do something for hurricane
            pass
        elif self.type == "earthquake":
            # Do something for earthquake
            pass
        elif self.type == "wildfire":
            # Do something for wildfire
            pass

    def update(self):
        """Update the state of the disaster."""
        if self.is_active:
            self.timer -= 1
            if self.timer <= 0:
                self.deactivate()

    def draw(self):
        """Draw the disaster on the screen."""
        if self.is_active:
            pygame.draw.circle(self.win, self.color, (600, 400), 20)
            disaster_text = self.disaster_font.render(self.type.capitalize(), True, self.color)
            self.win.blit(disaster_text, (550, 350))

