import console, time, speech
def logo():
	console.set_font('AnonymousPro-Bold', 15.35)
	print "# -=-=-=-=-=-=- #  # -=-=-=-=-=-=- #"
	console.set_color(0, 0, 0)
	print ""
	print "     ____.------''''--.___"
	print "         ____.----'---._/ '--"
	print "              __.----./ '--"
	print "                    / '-"
	print "            __..--------..__"
	print "         _-'              '----'"
	print "        ||"
	print "        ||"
	console.set_color()
	print "        '.__   Savage"
	console.set_color(0, 0, 0)
	print "            '--------."
	console.set_color()
	print "            Official ''-."
	console.set_color(0, 0, 0)
	print "                        |'."
	print "                       /  |"
	print "                    __/__.'"
	print "                   ' /"
	print ""
	console.set_color()
	print "# -=-=-=-=-=-=- #  # -=-=-=-=-=-=- #"
	print ""
logo()
speech.say("Welcome To APDOS")
time.sleep(1)
speech.say("Powered by Sav Sec")
time.sleep(3)
console.set_font()
console.clear()
# SavSec / Savage Official Logo in ACSII (c) 2016
