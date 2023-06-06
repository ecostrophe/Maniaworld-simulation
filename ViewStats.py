import pygame

class ViewStats:
    def __init__(self, journey):
        self =journey
        
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
        weather_now = font.render("Weather Now:"+self.weather_now,True,(0,0,0))
        
        species_info = font.render("•-> Species Info:",True,(255,0,0))
        Mingo_num = font.render("Mingo N°:"+str(self.heur)+"/"+str(self.mania.num_mingo),True,(0,0,0))
        Jingo_num = font.render("Jingo N°:"+str(self.heur)+"/"+str(self.mania.num_jingo),True,(0,0,0))
        Dingo_num = font.render("Dingo N°:"+str(self.heur)+"/"+str(self.mania.num_dingo),True,(0,0,0))
        
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