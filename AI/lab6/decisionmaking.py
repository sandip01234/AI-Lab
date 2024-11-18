def decision_making(time, weekday, weather):
    if 6 <= time < 8 and weekday:
        return "It's time to go to work."
    elif 12 <= time < 13:
        return "It's time for lunch."
    elif 21 <= time < 22:
        return "It's time to go to bed."
    elif not weekday and weather == "sunny":
        return "Go for a walk."
    else:
        return "No specific action."

# User input
time = int(input("Enter the current time (24-hour format): "))
weekday = input("Is it a weekday? (yes/no): ").lower() == "yes"
weather = input("Enter the weather condition (sunny/other): ").lower()

# Output
print(decision_making(time, weekday, weather))
