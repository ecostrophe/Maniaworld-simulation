import pygame
import random
from Mania import Mania
from Weather import Weather
from StockData import StockData

class Journey:
    def __init__(self, win, mania: Mania, weather: Weather, num_days: int, num_heurs_per_day: int):
        self.weather = weather
        self.mania = mania
        self.num_days = num_days
        self.num_heurs_per_day = num_heurs_per_day
        self.morning = False  # Set morning to False by default
        self.night = True  # Set night to True by default
        self.win = win
        self.part_day = ""
        self.heur = 0
        self.num_day = 0
        self.t_sunset = 5
        self.t_sunrise = 17
        self.day_color = (100,100,100)
        self.stock = StockData()
        self.data = self.set_data()
        self.morning_duration = self.t_sunrise - self.t_sunset
        self.night_duration = self.num_heurs_per_day - self.morning_duration


    def get_duration(self):
        """Get the duration of the journey based on the current time of day."""
        if self.morning:
            return self.morning_duration
        elif self.night:
            return self.night_duration

    def switch_time_of_day(self):
        """Switch between morning and night."""
        if self.morning:
            self.morning = False
            self.night = True
            self.part_day= "Night"
            self.day_color = (100,100,100)
        else:
            self.morning = True
            self.night = False
            self.part_day=  "Morning"
            self.day_color = (255,255,255)

    def Sunrising(self):
        """Change weather properties when the sun is rising."""
        self.weather.temperature += random.uniform(0, 2)
        self.weather.humidity -= random.uniform(0, 5)

    def Sunset(self):
        """Change weather properties when the sun is setting."""
        self.weather.temperature -= random.uniform(0, 2)

    def set_data(self):
        data = [0,self.num_day, self.heur, self.part_day, self.weather.weather_now, self.weather.temperature, self.weather.humidity, self.weather.precipitation, self.weather.wind_speed, self.weather.atmospheric_pressure]
        return data


    def write_stats(self):
        # Fonts
        font = pygame.font.Font('freesansbold.ttf',20)
        day_info = font.render("•-> Day info:",True,(255,0,0))
        day_num = font.render("Day num:"+str(self.num_day),True,(0,0,0))
        heur_num = font.render("Heur:"+str(self.heur),True,(0,0,0))
        per_day = font.render("Part of day:"+self.part_day,True,(0,0,0))
        sunrise = font.render("Sunrise:"+str(self.t_sunrise),True,(0,0,0))
        sunset = font.render("Sunset:"+str(self.t_sunset),True,(0,0,0))
        
        weather_info = font.render("•-> Weather info:",True,(255,0,0))
        tem_info = font.render("Temperature:"+str(int(self.weather.temperature)),True,(0,0,0))
        hum_info = font.render("Humidity:"+str(int(self.weather.humidity)),True,(0,0,0))
        pre_info = font.render("Precipitation:"+str(int(self.weather.precipitation)),True,(0,0,0))
        win_info = font.render("Wind speed:"+str(int(self.weather.wind_speed)),True,(0,0,0))
        atm_info = font.render("Atmospheric Pressure:"+str(int(self.weather.atmospheric_pressure)),True,(0,0,0))
        weather_now = font.render("Weather Now:"+self.weather.weather_now,True,(0,0,0))
        
        species_info = font.render("•-> Species Info:",True,(255,0,0))
        Mingo_num = font.render("Mingo {Green} N°:"+str(self.mania.count_species[0])+"/"+str(self.mania.num_mingo),True,(0,0,0))
        Jingo_num = font.render("Jingo {Red} N°:"+str(self.mania.count_species[1])+"/"+str(self.mania.num_jingo),True,(0,0,0))
        Dingo_num = font.render("Dingo {Aqua} N°:"+str(self.mania.count_species[2])+"/"+str(self.mania.num_dingo),True,(0,0,0))
        
	    #Blit the texts to screen
        self.win.blit(day_info,(10,920))
        self.win.blit(day_num,(60,940))
        self.win.blit(heur_num,(60,960))
        self.win.blit(per_day,(60,980))
        self.win.blit(sunset,(60,1000))
        self.win.blit(sunrise,(60,1020))
        
        self.win.blit(weather_info,(270,920))
        self.win.blit(tem_info,(320,940))
        self.win.blit(hum_info,(320,960))
        self.win.blit(pre_info,(320,980))
        self.win.blit(win_info,(320,1000))
        self.win.blit(atm_info,(320,1020))
        self.win.blit(weather_now,(320,1040))
        
        self.win.blit(species_info,(560,920))
        self.win.blit(Mingo_num,(610,940))
        self.win.blit(Jingo_num,(610,960))
        self.win.blit(Dingo_num,(610,980))
        pygame.display.update()

    def run(self):
        for day in range(1, self.num_days + 1):
            for heur in range(self.num_heurs_per_day):
                self.mania.count_animals()
                self.win.fill((255, 255, 255))
                pygame.draw.rect(self.win, self.day_color, [10, 10, self.mania.length, self.mania.width], 0)
                pygame.draw.rect(self.win, (0, 200, 200), [10, 10, self.mania.length, self.mania.width], 2)
                pygame.draw.rect(self.win, (255, 0, 0), [10,915, self.mania.length, 150], 2)
                pygame.display.update()
                self.num_day = day
                self.heur = heur
                self.write_stats()
                data_collect= self.set_data()
                self.stock.start_data(data_collect)
                self.mania.simulate_environment()
                self.mania.launch_species()
                if heur == self.t_sunset:
                    self.switch_time_of_day()
                    self.Sunrising()
                elif heur == self.t_sunrise:
                    self.switch_time_of_day()
                    self.Sunset()
        self.stock.stop_data()