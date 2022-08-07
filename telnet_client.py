import sys
import telnetlib


HOST = input("Enter host: ")
PORT = input("Enter port: ")

telnet_obj = telnetlib.Telnet(HOST, PORT)

message = ("GET /index.html HTTP/1.1\nHost: "+ HOST +"\n\n").encode('ascii')

telnet_obj.write(message)
