import datetime
import matplotlib.pyplot as plt
import subprocess
from plyer import notification  # For desktop notifications

# Class Task
class Task:
    def __init__(self, task_id, name, task_type, start_time, end_time, priority, deadline):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type  # "personal" or "academic"
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.deadline = deadline

# Sorting implementation with priority (Higher priority first)
def merge_sort(tasks, key):
    if len(tasks) > 1:
        mid = len(tasks) // 2
        left_half = tasks[:mid]
        right_half = tasks[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], key) >= getattr(right_half[j], key):  # Higher priority first
                tasks[k] = left_half[i]
                i += 1
            else:
                tasks[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            tasks[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            tasks[k] = right_half[j]
            j += 1
            k += 1

# Find upcoming tasks using binary search
def find_upcoming_tasks(tasks, current_time):
    upcoming_tasks = [task for task in tasks if task.start_time > current_time]
    return upcoming_tasks

# Find missed tasks
def find_missed_tasks(tasks, current_time):
    missed_tasks = [task for task in tasks if task.end_time < current_time]
    return missed_tasks

# Find completed tasks
def find_completed_tasks(tasks, current_time):
    completed_tasks = [task for task in tasks if task.start_time <= current_time <= task.end_time]
    return completed_tasks

# Analyze Task Density with Priorities
def analyze_task_density_with_priorities(tasks):
    time_slots = {hour: 0 for hour in range(24)}

    for task in tasks:
        for hour in range(task.start_time, task.end_time):
            if hour in time_slots:
                time_slots[hour] += task.priority  # Weight by priority

    return time_slots

# Plot Task Density with Priorities
def plot_task_density(density):
    times = list(density.keys())
    counts = list(density.values())

    plt.figure(figsize=(10, 6))
    plt.bar(times, counts, color='tab:orange', alpha=0.8)
    plt.xlabel("Time (Hours)")
    plt.ylabel("Priority-Weighted Task Count")
    plt.title("Task Density Analysis (Weighted by Priority)")
    plt.xticks(range(0, 24, 1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Visualization of tasks as a Gantt chart
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots()
    for i, task in enumerate(tasks):
        color = 'tab:blue' if task.task_type == "academic" else 'tab:green'
        ax.broken_barh([(task.start_time, task.end_time - task.start_time)], (i - 0.4, 0.8), facecolors=color)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task.name for task in tasks])
    ax.set_xlabel('Time (Hours)')
    ax.set_title('Task Schedule')
    plt.show()

# Notifications (For desktop)
def notify(title, message):
    try:
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "{title}"'
        ])
    except Exception as e:
        print(f"Notification Error: {e}")

# Main function to interact with the scheduler
def main():
    print("Welcome to the Enhanced Task Scheduler!")
    tasks = []
    task_id = 1

    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View upcoming tasks")
        print("4. View missed tasks")
        print("5. View completed tasks")
        print("6. Analyze task density")
        print("7. Generate Gantt chart")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"\nEnter details for Task {task_id}:")
            name = input("Task Name: ")
            task_type = input("Task Type (personal/academic): ").lower()
            start_time = int(input("Start Time (0-23): "))
            end_time = int(input("End Time (1-24): "))
            priority = int(input("Priority (1-10, higher is more important): "))
            deadline = int(input("Deadline (day of the month): "))

            tasks.append(Task(task_id, name, task_type, start_time, end_time, priority, deadline))
            task_id += 1
            print("Task added successfully!")

        elif choice == '2':
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(f"ID: {task.task_id}, Name: {task.name}, Type: {task.task_type}, Start: {task.start_time}:00, End: {task.end_time}:00, Priority: {task.priority}, Deadline: {task.deadline}")
            else:
                print("No tasks available.")

        elif choice == '3':
            current_time = datetime.datetime.now().time().hour
            upcoming_tasks = find_upcoming_tasks(tasks, current_time)
            if upcoming_tasks:
                print("\nUpcoming Tasks:")
                for task in upcoming_tasks:
                    print(f"Name: {task.name}, Priority: {task.priority}, Starts at: {task.start_time}:00")
            else:
                print("No upcoming tasks.")

        elif choice == '4':
            current_time = datetime.datetime.now().time().hour
            missed_tasks = find_missed_tasks(tasks, current_time)
            if missed_tasks:
                print("\nMissed Tasks:")
                for task in missed_tasks:
                    print(f"Name: {task.name}, Priority: {task.priority}, Ended at: {task.end_time}:00")
            else:
                print("No missed tasks.")

        elif choice == '5':
            current_time = datetime.datetime.now().time().hour
            completed_tasks = find_completed_tasks(tasks, current_time)
            if completed_tasks:
                print("\nCompleted Tasks:")
                for task in completed_tasks:
                    print(f"Name: {task.name}, Priority: {task.priority}, In progress")
            else:
                print("No completed tasks.")

        elif choice == '6':
            task_density = analyze_task_density_with_priorities(tasks)
            plot_task_density(task_density)

        elif choice == '7':
            if tasks:
                plot_gantt_chart(tasks)
            else:
                print("No tasks available to generate a Gantt chart.")

        elif choice == '8':
            print("Exiting the Task Scheduler. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
