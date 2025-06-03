# daily_reminder.py

def main():
    # Prompt for Task
    task = input("Enter your task: ").strip()
    while not task:
        print("Task cannot be empty. Please enter a task.")
        task = input("Enter your task: ").strip()

    # Prompt for Priority with validation
    priority = input("Priority (high/medium/low): ").strip().lower()
    while priority not in ("high", "medium", "low"):
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt for Time Bound with validation
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    while time_bound not in ("yes", "no"):
        print("Invalid input. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Use match-case for priority response
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"

    # Use if statement to modify reminder if time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print customized reminder
    print("\nReminder:", reminder)


if __name__ == "__main__":
    main()
