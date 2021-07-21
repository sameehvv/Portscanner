import socket
import sys
x=0
y=0
target = input("Enter the target IP address: ")
portrange = input("Enter the Port range to scan eg: 2-300: ")

lowerport = int(portrange.split("-")[0])
higherport = int(portrange.split("-")[1])

print("Scanning target",target,"from port",lowerport,"to",higherport)

try:
    for port in range(lowerport,higherport):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = s.connect_ex((target,port))

        if (status == 0):
            y=y+1
            print("***Port",port,"is opened***")
        else:
            x=x+1
        s.close()

    print("Closed Ports:",x,"& Opened Ports:",y)
except KeyboardInterrupt:				
  	print("exiting program....")
  	sys.exit()
