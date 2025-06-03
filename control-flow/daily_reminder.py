# daily_reminder.py

def main():
    # Loop until valid task is entered (non-empty)
    while True:
        task = input("Enter your task: ").strip()
        if task:
            break
        print("Task description cannot be empty. Please try again.")

    # Loop until valid priority entered
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Invalid priority. Please enter high, medium, or low.")

    # Loop until valid time-bound answer entered
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ["yes", "no"]:
            break
        print("Invalid input. Please enter yes or no.")

    # Use match-case to determine base reminder message
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print(f"\nReminder: {reminder}")

if __name__ == "__main__":
    main()

