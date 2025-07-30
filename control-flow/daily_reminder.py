Task = input("Enter your task:")
Time Bound = input("Is it time bound? (Yes/No):").lower()
Priority = input("Prioity (High/medium/low):").lower()
match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"Reminder: {'Task'} is a high priority task that requires immediate attention today.")
    case "low":
        if Time_Bound == "no":
            print(f"Note: '{Task}' is a low priority. consider finishing it on your free time.")
