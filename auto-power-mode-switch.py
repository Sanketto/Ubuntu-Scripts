import subprocess

process = subprocess.run("on_ac_power && echo 1 || echo 0", shell=True, capture_output=True, text=True)

if process.stdout == "1":
    subprocess.run("powerprofilesctl set performance", shell=True, capture_output=True, text=True)
else:
    subprocess.run("powerprofilesctl set balance", shell=True, capture_output=True, text=True)