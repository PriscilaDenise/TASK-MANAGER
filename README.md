## Overview
The Enhanced Task Scheduler is a Python-based program that helps users manage and organize their tasks effectively. It includes features such as task prioritization, task analysis, Gantt chart visualization, and desktop notifications to ensure that users stay on top of their schedules.

## Features
1. **Add Tasks**: Create tasks with details such as name, type (personal or academic), start and end times, priority, and deadlines.
2. **View Tasks**:
   - All tasks.
   - Upcoming tasks.
   - Missed tasks.
   - Completed tasks.
3. **Task Analysis**:
   - Analyze task density based on priority.
   - View priority-weighted task density using bar charts.
4. **Visualization**:
   - Generate Gantt charts to visually represent the task schedule.
5. **Desktop Notifications**: Notify users of tasks using system notifications.

## Requirements
- Python 3.7 or later
- Libraries:
  - `datetime`
  - `matplotlib`
  - `subprocess`
  - `plyer`

Install required libraries using:
```bash
pip install matplotlib plyer
```

## Usage
1. Clone or download the repository containing the scheduler.
2. Run the script using:
   ```bash
   python scheduler.py
   ```
3. Follow the interactive menu to manage tasks.

## Menu Options
- **1. Add a new task**: Enter the details for the task to add it to the schedule.
- **2. View all tasks**: Display a list of all tasks with their details.
- **3. View upcoming tasks**: See tasks scheduled to start after the current time.
- **4. View missed tasks**: Check tasks that have already ended without completion.
- **5. View completed tasks**: List tasks that are currently in progress.
- **6. Analyze task density**: Visualize priority-weighted task density.
- **7. Generate Gantt chart**: Create a Gantt chart for all tasks.
- **8. Exit**: Exit the program.

## How It Works
### Task Prioritization
- Tasks are stored as objects of the `Task` class.
- Tasks are sorted using the Merge Sort algorithm, prioritizing higher-priority tasks.

### Task Analysis
- The program calculates task density based on priority for each hour.
- Density is displayed as a bar chart using `matplotlib`.

### Visualization
- Tasks are represented as bars in a Gantt chart, differentiated by color based on type (academic or personal).

### Notifications
- Desktop notifications alert users about tasks. Notifications use the `plyer` library for cross-platform support.

## Example Task Entry
When prompted to add a task:
1. Task Name: `Prepare for Exam`
2. Task Type: `academic`
3. Start Time: `9` (9 AM)
4. End Time: `11` (11 AM)
5. Priority: `8`
6. Deadline: `15` (15th day of the month)

## Notes
- The time for tasks should be entered in 24-hour format.
- The priority scale is from 1 (low) to 10 (high).
- Notifications may require additional setup depending on the operating system.

## Future Enhancements
- Add recurring task functionality.
- Integrate with external calendars (e.g., Google Calendar).
- Add support for user authentication.
- Include task reminders based on deadlines.



## Contact
For questions or suggestions, feel free to reach out:
- Email: denisepriscilamuwanguzi@gmail.com
- GitHub: https://github.com/PriscilaDenise/TASK-MANAGER

