# Hatter command line version, This doesn't require
from aiml import Kernel
from os import listdir
import sys

files = listdir('standard')

bot = Kernel()
for file in files:
	bot.learn('standard/'+file)

respon = ' '
print "Hatter> Hello , I am Tarrant the Hatter. Some people call me the Mad Hatter. Good to see you. Type \"bye\" to exit"
while 1 :
	question=raw_input("You> ")
	reply=bot.respond(question)
	print "Hatter> ",reply
	if question=="bye":
		sys.exit(0)
		
