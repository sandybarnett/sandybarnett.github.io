#SAndy and Erika
#Lucy's Quest
#Python lesson


def introduction():
	print "Lucy's Quest"
	print "Lucy woke one day and her dog Marley was missing."
	print
	desert_jungle()

	
def desert_jungle():
	print "Where should she search for Marley, the Jungle or the Desert?"
	print "Type J for Jungle or D for Desert"
	answer = raw_input()
	if answer == "J":
		print "Scary choices!"
		bridge_cliff()
	else:
		print"I hope you brought lots of water!"
		pyramid_dunes()
		
def bridge_cliff():
	print "You are in a dangerous predicament. Which will you chose, the bridge or cliff path?"
	print "Type B or C."
	answer = raw_input()
	if answer == "B":
		print "The old bridge collapsed and you fell into the river below."
		try_again()
	else: 
		print "That cliff was too crumbly, you are a gonner."
		try_again()
def pyramid_dunes():
	print "You are really close to finding Marley! Choose wisely, where will you search, in the Pyramid or the Sand Dunes." 
	print "Type P or S."
	answer = raw_input()
	if answer == "P":
		print "The mummy ate you!"
		try_again()
	else:
		print "You found Marley!"
		print "Thanks for all your your help!"
		
def try_again():
	print "That didn't work, will you keep searching? Enter Y or N"
	answer = raw_input()
	if answer == "Y":
		print "Awesome, let's go!"
		desert_jungle()
	else:
		print "See you around..."
		
	
	
	
introduction()