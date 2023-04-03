# ========== ========== ========== ==========
#
#   Author      : Hatmaji Ismu Wicaksono
#   Date        : 2023-04-03
#   Description :
#       This is a simple python script 
#       to monitor the resources usage 
#       of your computer.
#
# ========== ========== ========== ==========

# Import the libraries
import os
import psutil
import csv
import datetime

# Get the current time
directory = "output"
time_start = datetime.datetime.now().replace(microsecond=0)
file_name = f"./{directory}/resources-monitor-{time_start.strftime('%Y-%m-%d-%H-%M-%S')}.csv"

# Function to start the monitoring
def start_monitoring():
    print("Monitoring Started")
    print("Press Ctrl + C to stop monitoring")
    while True:
        monitor()

def monitor():
    # Timestamp
    timestamp = datetime.datetime.now().replace(microsecond=0)

    # CPU usage percentage per seconds
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM usage
    ram_usage_percentage = psutil.virtual_memory()[2]
    ram_usage = psutil.virtual_memory()[3]/1000000000

    # Disk usage
    disk_usage_percentage = psutil.disk_usage('/')[3]
    disk_usage = psutil.disk_usage('/')[1]/1000000000

    # Show the results
    print("------------------------------------------------")
    print("Timestamp: ", datetime.datetime.now().replace(microsecond=0))
    print("The CPU usage is : ", cpu_usage)
    print('RAM memory % used:', ram_usage_percentage)
    print('RAM Used (GB):', ram_usage)
    print('Disk % used:', disk_usage_percentage)
    print('Disk Used (GB):', disk_usage)

    # If the file does not exist, create it
    if not os.path.exists(file_name):
        # create new folder
        os.makedirs(directory, exist_ok=True)
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "CPU Usage (%) Per Seconds", "RAM Usage (GB) Per Seconds",
                            "RAM Usage (%) Per Seconds", "Disk Usage (GB) Per Seconds", "Disk Usage (%) Per Seconds"])

    # Write to new lines in csv file
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [timestamp, cpu_usage, ram_usage, ram_usage_percentage, disk_usage, disk_usage_percentage])


# Main function
if __name__ == "__main__":
    function = input("Do you want to start monitoring? (y/n): ")
    if function == "y":
        start_monitoring()
    else:
        print("Monitoring Stopped")
