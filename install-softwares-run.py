import subprocess
import lsb_release, os


def run_command(command):
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if process == 0:
            print("Command executed successfully:")
            print(process.stdout)
        else:
            print(f"Error executing command (exit code {process.returncode}):")
            print(process.stderr)
        subprocess.call(["wait"])

def call_func(commands):
         for command in commands:
          run_command(command)
def get_file(file_folder):
     file_path = os.getcwd() + f"/{file_folder}"
     files = os.listdir(file_path)
     print(files)
     for file in files:
          # process = subprocess.run(f"file {file_path}/{file}", shell=True, capture_output=True, text=True)
          # print(process.stdout)
          if ".deb" in file or ".sh" in file or ".run" in file or ".bin" in file:
             pass
          else:
             files.remove(file)
     return files

def install_cortex():
     c1 = ["mkdir", "-p", "/etc/panw"]
     c2 = ["cp", "-rv", "cortex/*.conf", "/etc/panw/"]
     c3 = ["dpkg", "-i", "cortex/*.deb"]
     run_command(c1)
     run_command(c2)
     run_command(c3)

def install_globalprotect():
     file_folder = "GlobalProtect"
     #run_command(command)
     files = get_file("GlobalProtect")
     for file in files:
        run_command(["dpkg", "-i", f"GlobalProtect/{file}"])


def install_gtb_agent():
     release = lsb_release.get_os_release()['RELEASE']
     if release == "18.04":
          run_command(["dpkg", "-i", "GTB/Ubuntu18.04/*.deb"])
     elif release == "20.04":
          run_command(["dpkg", "-i", "GTB/Ubuntu20.04/*.deb"])
     elif release == "22.04":
          run_command(["dpkg", "-i", "GTB/Ubuntu22.04/*.deb"])
     else:
          pass
     
     run_command(["/usr/local/gtb/endpoint/bin/support.sh", "-a", "con-hjph3gtb.kpit.com:443"])

     
def install_manage_engine():
     c1 = ("cd", "Manage-Engine")
     c2 = ["./*.bin"]
     c3 = ["cd", ".."]
     run_command(c1)
     run_command(c2)
     run_command(c3)

def install_other():
     command = ["dpkg", "-i", "Other/*.deb"]
     run_command(command)

def install_trellix():
     command = ["Trellix-Agent-ENS/Trellix/*.sh", "-i"]
     run_command(command)
     command = ["Trellix-Agent-ENS/ENS/*.sh"]
     run_command(command)

def install_zscaler():
     command = ["Zscaler/Zscaler-linux-1.5.0.41-installer.run", "--mode", "unattended"]
     run_command(command)

install_globalprotect()

#def run_command(command):
#        process = subprocess.run(command, shell=True, capture_output=True, text=True)
#        
#        if process.returncode == 0:
#            print("Command executed successfully:")
#            print(process.stdout)
#        else:
#            print(f"Error executing command (exit code {process.returncode}):")
#            print(process.stderr)
#        process = subprocess.run("wait", shell=True, capture_output=True, text=True)