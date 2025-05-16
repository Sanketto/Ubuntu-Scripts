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
     # print(files)
     n = len(files) - 1
     while n >= 0:
          # print(files[n])
          # process = subprocess.run(f"file {file_path}/{file}", shell=True, capture_output=True, text=True)
          # print(process.stdout)
          if ".deb" in files[n] or ".sh" in files[n] or ".run" in files[n] or ".bin" in files[n]:
          #    print(files[n])
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
     #run_command(command)
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
     # c1 = ("cd", "Manage-Engine")

     files = get_file("Manage-Engine")
     old_dir = os.getcwd()
     os.chdir("Manage-Engine")
     print(os.getcwd())
     for file in files:
        run_command([f"./{file}"])
     os.chdir(old_dir)
     # c3 = ["cd", ".."]
     
def install_other():
     files = get_file("Other")
     #command = ["dpkg", "-i", "Other/*.deb"]
     for file in files:
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

# install_cortex()
# install_globalprotect()
# install_gtb_agent()
# install_manage_engine()
# install_other()
# install_trellix()
install_zscaler()

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
