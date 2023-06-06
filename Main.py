import pygame
from Mania import Mania
from Journey import Journey
from Weather import Weather
from Disaster import Disaster
from Pandemic import Pandemic

pygame.init()
window = pygame.display.set_mode((800, 800),pygame.RESIZABLE)

#Varible
run = True
clock=pygame.time.Clock()

#Meteo
temperature = 40
humidity = 80
precipitation = 30
wind_speed = 18
atmospheric_pressure= 1015
weather_today = Weather(temperature,humidity,precipitation,wind_speed,atmospheric_pressure)

#create the manialand
manialand = Mania(window,weather_today,100,30,10,1060,900)
manialand.add_species()
journey = Journey(window,manialand,weather_today,30,24)

#Start the simulations
while run:
    journey.run()
    corona = Pandemic(window,2,journey)
    corona.update(manialand.animals)
    #pygame.display.update()
    clock.tick(60)
	#The differents events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


