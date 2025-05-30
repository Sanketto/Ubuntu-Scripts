import subprocess

process = subprocess.run("on_ac_power && echo 1 || echo 0", shell=True, capture_output=True, text=True)
#print(process)

if int(process.stdout) == 1:
    result = subprocess.run("powerprofilesctl set performance", shell=True, capture_output=True, text=True)
    print(result)
    
else:
    result = subprocess.run("powerprofilesctl set balanced", shell=True, capture_output=True, text=True)
    print(result)