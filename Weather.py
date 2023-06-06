import random

class Weather:
    def __init__(self ,temperature, humidity, precipitation, wind_speed, atmospheric_pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.atmospheric_pressure = atmospheric_pressure
        self.weathers = ["Rain","Blow","Clear","Normal"]
        self.weather_now = ""

    def calculate_atmospheric_pressure(self, altitude, temperature):
        """Calculates atmospheric pressure at a given altitude and temperature using the barometric formula."""
        # Define constants for standard temperature and pressure at sea level
        sea_level_pressure = 1013.25  # millibars
        sea_level_temperature = 288.15  # Kelvin
        
        # Define constants for the lapse rate and gas constant
        lapse_rate = -0.0065  # degrees Celsius per meter
        gas_constant = 8.31432  # joules per mole Kelvin
        
        # Convert temperature from Celsius to Kelvin
        temperature_kelvin = temperature + 273.15
        
        # Calculate the pressure at the given altitude using the barometric formula
        pressure_at_altitude = sea_level_pressure * ((1 - (lapse_rate * altitude) / temperature_kelvin) ** (9.80665 / (lapse_rate * gas_constant)))
        return pressure_at_altitude


    def Raining(self):
        """Change weather properties when it is raining."""
        self.temperature = random.uniform(10,20)
        self.humidity = random.uniform(80,90)
        self.precipitation = random.uniform(1,10)
        self.wind_speed = random.uniform(20,40)
        self.atmospheric_pressure = self.calculate_atmospheric_pressure(10,self.temperature)


    def Blowing(self):
        """Change weather properties when it is windy."""
        self.temperature = random.uniform(-5,10)
        self.humidity = random.uniform(70,90)
        self.precipitation = random.uniform(5,15)
        self.wind_speed = random.uniform(40,100)
        self.atmospheric_pressure = self.calculate_atmospheric_pressure(10,self.temperature)
        
    def normal(self):
        """Change weather properties when it is normal."""
        self.temperature = random.uniform(25,28)
        self.humidity = random.uniform(40,60)
        self.precipitation = random.uniform(0,5)
        self.wind_speed = random.uniform(10,20)
        self.atmospheric_pressure = self.calculate_atmospheric_pressure(10,self.temperature)
        
    def isClear(self):
        """Change weather properties when it is clear."""
        self.temperature = random.uniform(25,28)#if stat
        self.humidity = random.uniform(40,60)
        self.precipitation = random.uniform(0,2)
        self.wind_speed = random.uniform(5,10)
        self.atmospheric_pressure = self.calculate_atmospheric_pressure(10,self.temperature)

    def set_weather(self):
    #set the weather
        self.weather_now = random.choice(self.weathers)
        if self.weather_now == "Rain":
            self.Raining()
        elif self.weather_now == "Blow":
            self.Blowing()
        elif self.weather_now == "Clear":
            self.isClear()
        elif self.weather_now == "Normal":
            self.normal()
        else:
            pass