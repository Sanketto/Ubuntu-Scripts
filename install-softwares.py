import subprocess
import lsb_release, os


def run_command(command):
     #    process = subprocess.check_call(command)
        
     #    if process == 0:
     #        print("Command executed successfully:")
     #    else:
     #        print(f"Error executing command (exit code {process.returncode}):")
     #    subprocess.run("wait", shell=True, capture_output=True, text=True)
     #    subprocess.run("echo", shell=True, capture_output=True, text=True)
     #    subprocess.run("echo", shell=True, capture_output=True, text=True)
        try:
          subprocess.check_call(command)
        except subprocess.CalledProcessError as e:
          print(f"Error executing command: {e}")
          print(f"Return code: {e.returncode}")
          return e.returncode

def get_file(file_folder):
     file_path = os.getcwd() + f"/{file_folder}"
     files = os.listdir(file_path)
     n = len(files) - 1
     while n >= 0:
          if ".deb" in files[n] or ".sh" in files[n] or ".run" in files[n] or ".bin" in files[n]:
             pass
          else:
             files.remove(files[n])
          n -= 1 
     print(files)
     return files

def install_cortex():
     files = get_file("cortex")
     process = subprocess.run("mkdir -p /etc/panw", shell=True, capture_output=True, text=True)
     process = subprocess.run("cp -rv cortex/*conf /etc/panw", shell=True, capture_output=True, text=True)
     for file in files:
         subprocess.call(["dpkg", "-i", f"cortex/{file}"] )

def install_globalprotect():
     files = get_file("GlobalProtect")
     for file in files:
        run_command(["dpkg", "-i", f"GlobalProtect/{file}"])


def install_gtb_agent():
     file_folder = "GTB"
     release = lsb_release.get_os_release()['RELEASE']
     if release == "18.04":
          files = get_file(file_folder + "/Ubuntu18.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu18.04/{file}"])
     elif release == "20.04":
          files = get_file(file_folder + "/Ubuntu20.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu20.04/{file}"])
     elif release == "22.04":
          files = get_file(file_folder + "/Ubuntu22.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu22.04/{file}"])
     else:
          pass
     
     run_command(["/usr/local/gtb/endpoint/bin/support.sh", "-a", "con-hjph3gtb.kpit.com:443"])

     
def install_manage_engine():
     files = get_file("Manage-Engine")
     old_dir = os.getcwd()
     os.chdir("Manage-Engine")
     print(os.getcwd())
     for file in files:
        run_command([f"./{file}"])
     os.chdir(old_dir)
     
def install_other():
     files = get_file("Other")
     for file in files:
       if ".sh" not in file:
          run_command(["dpkg", "-i", f"Other/{file}"])

def install_trellix():
     files = get_file("Trellix-Agent-ENS/Trellix")
     for file in files:
        run_command([f"Trellix-Agent-ENS/Trellix/{file}", "-i"])
     files = get_file("Trellix-Agent-ENS/ENS")
     for file in files:
        run_command([f"Trellix-Agent-ENS/ENS/{file}"])

def install_zscaler():
     packages = "libglib2.0-0 net-tools libqt5dbus5 libqt5core5a libqt5gui5 libqt5opengl5 libqt5qml5 libqt5quick5 libqt5quickcontrols2-5 libqt5quickparticles5 libqt5quickwidgets5 libqt5sql5 libqt5sql5-sqlite libqt5webchannel5 libqt5webengine5 libqt5webenginecore5 libqt5webenginewidgets5 libqt5webkit5 libqt5webview5 libqt5widgets5 dbus libdbus-glib-1-2 libnss3-tools libnss-resolve curl jq systemd-coredump ca-certificates"
     packages = packages.split(" ")
     install_dependecy_packages(packages)
     files = get_file("Zscaler")
     for file in files:
        run_command([f"Zscaler/{file}", "--mode", "unattended"])

def join_domain():
    packages = "dnsmasq ssh realmd libnss-sss libpam-sss sssd sssd-tools adcli oddjob-mkhomedir oddjob packagekit samba-common-bin"
    packages = packages.split(" ")
    install_dependecy_packages(packages)
    current_path = os.getcwd()
    new_path = current_path + "/Domain"
    os.chdir(new_path)
    run_command(["bash", "join-domain.sh"])
    os.chdir(current_path)

def install_dependecy_packages(package_list = None):
    update = 1
    while update != 0:
      update = run_command(["apt", "update"])

install_dependecy_packages()