def traffic_light_control(light_color, pedestrian_button_pressed):
    if light_color == "red":
        return "Cars must stop."
    elif light_color == "green":
        return "Cars can go."
    elif light_color == "yellow":
        return "Cars must slow down and prepare to stop."
    elif pedestrian_button_pressed:
        return "Light will turn red after a short delay."
    else:
        return "No action needed."

# User input
light_color = input("Enter the traffic light color (red/green/yellow): ").lower()
pedestrian_button_pressed = input("Is the pedestrian button pressed? (yes/no): ").lower() == "yes"

# Output
print(traffic_light_control(light_color, pedestrian_button_pressed))
