task = input("Enter your task:")
task_priority = input("Prioity (High/medium/low):").lower()
time_bound = input("Is it time-bound? (Yes/No):").lower()
match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {'task'} is a high priority task that requires immediate attention today.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority. consider finishing it on your free time.")