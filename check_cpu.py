import psutil
import time

# Get CPU usage for a specific interval (e.g., 1 second)
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current CPU usage: {cpu_usage}%")

# To continuously monitor CPU usage, you can use a loop:
print("\nMonitoring CPU usage for 5 seconds:")
for _ in range(5):
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_usage}%")
    time.sleep(1) # Wait for 1 second before the next check