import psutil
from datetime import datetime

def check_health():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log = f"""
Time: {datetime.now()}
CPU Usage: {cpu}%
RAM Usage: {ram}%
Disk Usage: {disk}%
-------------------------
"""

    with open("health.log", "a") as f:
        f.write(log)

    print(log)

if __name__ == "__main__":
    check_health()
