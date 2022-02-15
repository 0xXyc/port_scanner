
import sys
import socket
import pyfiglet
# Import modules that will allow code to run.
# You can also import modules within a single line e.g. import socket,sys

banner = pyfiglet.figlet_format("jswinss \n Py_Port_Scanner")
print(banner)


ip = '' 
open_ports =[] 
# Specify your target in ''.
# open_ports will be auto-populated when the ports are detected.

ports = range(1, 65535)
# All 65535 possible ports will be enumerated.
# If you would rather scan specific services change the code to the following (don't specify "range"): ports = {21, 22, 23, 53, 80, 135, 443, 445}
# A great example to use this is when you want a quick scan or if you want to keep a low network profile or signature.


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result
# Determines if a connection to a port is possible or not and prints out the result.


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
# Loops the above code in order to determine result of a port for the rest of the specified ports.   


if open_ports: 
  print ("Open Ports: ") 
  print (sorted(open_ports)) 
else: 
  print ("No ports are open")