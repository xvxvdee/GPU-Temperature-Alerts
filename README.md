# GPU-Temperature-Alerts
This Python script monitors the GPU temperature and sends desktop notifications if the temperature exceeds a certain threshold. It is compatible with both Windows 10 and Windows 11. The script also identifies the process with the highest CPU usage and includes it in the alert.

## Features
- Monitors GPU temperature
- Sends notifications for potential overheat and elevated temperatures
- Identifies the process with the highest CPU usage


## Set Up in Windows Task Scheduler
1. **Open Task Scheduler**: Search for “Task Scheduler” in the Start menu and open it.
2. **Create a New Task**:
   - Right-click on “Task Scheduler (Local)” and select “Create Task”.
   - Give your task a name and description.
3. **Create an Action**:
   - Go to the “Actions” tab and click “New”.
   - In the “Program/script” box, enter the path to your Python executable (e.g., `C:\Python39\python.exe`).
   - In the “Add arguments (optional)” box, enter the path to your Python script (e.g., `C:\path\to\gpu_temperature_alerts.py`).
4. **Create a Trigger**:
   - Go to the “Triggers” tab and click “New”.
   - Set the schedule for when you want the script to run (e.g., daily, weekly, at a specific time).
5. **Configure Additional Settings (optional)**:
   - You can set conditions and additional settings in the “Conditions” and “Settings” tabs as needed.

