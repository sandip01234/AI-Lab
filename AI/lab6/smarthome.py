def smart_home_automation(temperature, is_dark_outside, someone_home, security_armed, door_opened):
    if temperature < 18:
        return "Turn on the heater."
    elif temperature > 25:
        return "Turn on the air conditioner."
    elif is_dark_outside and someone_home:
        return "Turn on the lights."
    elif security_armed and door_opened:
        return "Sound the alarm."
    else:
        return "No action needed."

# User input
temperature = float(input("Enter the current temperature in °C: "))
is_dark_outside = input("Is it dark outside? (yes/no): ").lower() == "yes"
someone_home = input("Is someone at home? (yes/no): ").lower() == "yes"
security_armed = input("Is the security system armed? (yes/no): ").lower() == "yes"
door_opened = input("Has a door been opened? (yes/no): ").lower() == "yes"

# Output
print(smart_home_automation(temperature, is_dark_outside, someone_home, security_armed, door_opened))
