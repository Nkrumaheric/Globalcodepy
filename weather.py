import pyowm

apiKey = '068621f4a90b1effbedc0cb603ac031'
owm = pyowm.OWM(apiKey)
location = input('Enter any City you want: ')
observation = owm.weather_at_place(location)
w = observation.get_weather()

print("the weather in the world")
print("Wind: ",w.get_wind())
print("Humidity: ",w.get_humidity())
print("pressure: ",w.get_pressure())
print("Temperature: ",w.get_temperature())