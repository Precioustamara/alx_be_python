task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority :
    case _ if priority == 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case _ if priority == 'low':
        if time_bound == 'no':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")