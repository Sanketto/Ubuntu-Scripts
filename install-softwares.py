import subprocess
import lsb_release, os


def run_command(command):
        process = subprocess.call(command)
        
        if process == 0:
            print("Command executed successfully:")
            #print(process.stdout)
        else:
            print(f"Error executing command (exit code {process.returncode}):")
            #print(process.stderr)
        process = subprocess.run("wait", shell=True, capture_output=True, text=True)

#def call_func(commands):
#         for command in commands:
#          run_command(command)
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
     c3 = ""
     files = get_file("cortex")
     for file in files:
         c3 = ["dpkg", "-i", f"cortex/{file}"] 
     run_command(c1)
     run_command(c2)
     run_command(c3)

def install_globalprotect():
     #run_command(command)
     files = get_file("GlobalProtect")
     for file in files:
        run_command(["dpkg", "-i", f"GlobalProtect/{file}"])


def install_gtb_agent():
     file_folder = "GTB"
     release = lsb_release.get_os_release()['RELEASE']
     if release == "18.04":
          files = get_file(file_folder + "Ubuntu18.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu18.04/{file}"])
     elif release == "20.04":
          files = get_file(file_folder + "Ubuntu20.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu20.04/{file}"])
     elif release == "22.04":
          files = get_file(file_folder + "Ubuntu22.04")
          for file in files:
             run_command(["dpkg", "-i", f"GTB/Ubuntu22.04/{file}"])
     else:
          pass
     
     run_command(["/usr/local/gtb/endpoint/bin/support.sh", "-a", "con-hjph3gtb.kpit.com:443"])

     
def install_manage_engine():
     # c1 = ("cd", "Manage-Engine")

     files = get_file("Manage-Engine")
     old_dir = os.getcwd()
     os.chdir("Manage-Engine")
     for file in files:
        c1 = [f"./{file}"]
     os.chdir(old_dir)
     # c3 = ["cd", ".."]
     
     run_command(c1)
     

def install_other():
     files = get_file("Other")
     #command = ["dpkg", "-i", "Other/*.deb"]
     for file in files:
       print(file)
       if ".sh" not in file:
          run_command(["dpkg", "-i", f"Other/{file}"])

def install_trellix():
     #command = ["Trellix-Agent-ENS/Trellix/*.sh", "-i"]
     files = get_file("Trellix-Agent-ENS/Trellix")
     for file in files:
        run_command([f"Trellix-Agent-ENS/Trellix/{file}", "-i"])
     #command = ["Trellix-Agent-ENS/ENS/*.sh"]
     files = get_file("Trellix-Agent-ENS/ENS")
     for file in files:
        run_command([f"Trellix-Agent-ENS/ENS/{file}"])

def install_zscaler():
     files = get_file("Zscaler")
     #command = ["Zscaler/Zscaler-linux-1.5.0.41-installer.run", "--mode", "unattended"]
     for file in files:
        run_command([f"Zscaler/{file}", "--mode", "unattended"])

install_manage_engine()

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
