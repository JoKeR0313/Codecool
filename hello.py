import sys

def hellopy(): 							#Definition of hellopy function

	if len(sys.argv) > 1:			#If you give a name, it will welcomes
		print("Hello " + sys.argv[1] + "!")
  
	else:											#If you didn't, it will welcomes the whole world
		print("Hello World!")

hellopy()										#Running function	
