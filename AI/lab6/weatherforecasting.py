def weather_forecast(sky, wind, temperature):
    if sky == "cloudy" and not wind:
        return "It might rain."
    elif temperature < 0 and sky == "clear":
        return "It might snow."
    elif temperature > 30 and not wind:
        return "It might be a hot day."
    elif sky == "clear" and wind:
        return "It might be a pleasant day."
    else:
        return "No forecast available."

# User input
sky = input("Enter the sky condition (cloudy/clear): ").lower()
wind = input("Is there wind? (yes/no): ").lower() == "yes"
temperature = float(input("Enter the temperature in °C: "))

# Output
print(weather_forecast(sky, wind, temperature))
