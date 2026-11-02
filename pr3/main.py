import psutil

GREEN = '\033[92m'
YELLOW = '\033[93m'   
RED = "\033[91m"
RESET = "\033[0m"

cpu = psutil.cpu_percent(interval=1)
gpu=psutil.virtual_memory().percent
ram=psutil.virtual_memory().percent
disk=psutil.disk_usage('/').percent
ff=psutil.users()
ff.sort(key=lambda x: x.name)

def zjisti_hodnoty(hodnota):
    if hodnota < 70:
        return "OK"
    elif hodnota < 90:
        return "WARNING"
    else:
        return "CRITICAL"

print("CPU Usage: {cpu_percent}%".format(cpu_percent=cpu))
print("GPU Usage: {gpu_percent}%".format(gpu_percent=gpu))
print("RAM Usage: {ram_percent}%".format(ram_percent=ram))
print("Disk Usage: {disk_percent}%".format(disk_percent=disk))
print(f"{GREEN}CPU Usage: {cpu}%{RESET}")
print(f"{YELLOW}RAM Usage: {ram}%{RESET}")
print(f"{RED}Disk Usage: {disk}%{RESET}")
