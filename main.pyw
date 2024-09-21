import WinTmp
import subprocess
import platform
from win11toast import toast
from win10toast import ToastNotifier


def GetHighestUsageCPU():
    # Get the main window titles
    MainWindowTitles = []
    cmd_MainWindowTitles = 'powershell "gps | where {$_.MainWindowTitle } | select Name"'
    proc = subprocess.Popen(cmd_MainWindowTitles, shell=True, stdout=subprocess.PIPE)
    MainWindowTitles = [line.decode().rstrip() for line in proc.stdout if line.rstrip()]       
    MainWindowTitles = MainWindowTitles[2:]

    # Get the top processes by CPU usage
    ProcessCpuUsage = []
    cmd_ProcessCpuUsage = 'powershell "Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 10 -Property ProcessName,CPU"'
    proc = subprocess.Popen(cmd_ProcessCpuUsage, shell=True, stdout=subprocess.PIPE)
    ProcessCpuUsage = [line.decode().rstrip() for line in proc.stdout if line.rstrip()] 
    ProcessCpuUsage = ProcessCpuUsage[2:]
    ProcessCpuUsage = [tuple(line.split()) for line in ProcessCpuUsage]
    
    # Find the process with the highest CPU usage that also has a main window title
    for process_name, cpu_usage in ProcessCpuUsage:
        if process_name in MainWindowTitles:
            return process_name

def GetTemperatureConcern (temp):
    if temp >= 90: 
        return "Potential Overheat"
    elif temp >= 80:
        return "Elevated Temperature"
    else:
        return "Optimal Temperature"

def toastNotification (temp, warning, app):
        toast10 = ToastNotifier()

        if "Windows-11" in platform.platform():
            toast(
            "GPU Alert",
            f"\u2022  Tempurature: {temp}\u00B0\n\u2022  Warning: {warning}\n\u2022  Possible Cause: {app}",
            icon='https://images.pexels.com/photos/750225/pexels-photo-750225.jpeg',
            scenario='incomingCall'
            )
        elif "Windows-10" in platform.platform():
            toast10.show_toast("GPU Alert",
            f"\u2022  Tempurature: {temp}\u00B0\n\u2022  Warning: {warning}\n\u2022  Possible Cause: {app}")

GPU_temp =WinTmp.GPU_Temp()
if  GPU_temp >= 80:
    toastNotification(GPU_temp,GetTemperatureConcern(GPU_temp),GetHighestUsageCPU())
