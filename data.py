"""
Create all the global variables requiered to make the project work
Display function and requests functions
easier to create an UI from these functions than if we use prints in the code
"""

def init():
	#dictionary of the html elements
	global arrayHTML
	arrayHTML = {}
	#list of the string of the ID used
	global listID
	listID = []
	#int of the number of div not closed
	global countOpenDiv
	countOpenDiv = 0

	#reminder : we suppose that we open column inside rows and not the oposit to create a grid
	#int of the number of nested rows currently open
	global countNestedRow
	countNestedRow = 0
	#int of number of nested column currently open
	global countNestedCol
	countNestedCol = 0
	#list of the [type, strings] of metadata to put in the head
	#type : title, author, descrition
	global metadata
	metadata = []
	
	#dict of the color names
	global colorName
	colorName = {
		"red" : "danger",
		"blue" : "primary",
		"yellow" : "warning",
		"green" : "success",
		"white" : "light",
		"black" : "dark",
		"gray" : "secondary",
		"cyan" : "info",
	}
	#dict of the opacity level
	global opacity
	opacity = [
		"opacity-10",
		"opacity-20",
		"opacity-30",
		"opacity-40",
		"opacity-50",
		"opacity-60",
		"opacity-70",
		"opacity-80",
		"opacity-90",
		"opacity-100"
	]
	# dict of the sizes of columns
	global sizeRelation
	sizeRelation = {
		"quarter" : "col-3",
		"third" : "col-4",
		"half" : "col-6",
		"entire" : "col-12",
		"small" : "col-2",
		"tiny" : "col-1",
		"medium" : "col-6",
		"big" : "col-10",
		"smallest" : "col-1",
		"biggest" : "col-12",
		"two-third" : "col-8",
		"three-quarter" : "col-9",
	}
	#dict of the relative placements
	# "1 3 col-3 col-6 col-3" 
	# means that there are 3 column to be created (3),
	# that we want to place the object in the second one (1),
	# the first column is of size "col-3", ...
	# not implemented yet
	global placementRelation
	placementRelation = {
		"middle" : "1 3 col-3 col-6 col-3",
		"center" : "1 3 col-3 col-6 col-3",
		"centered" : "1 3 col-3 col-6 col-3",
		"far-left" : "0 2 col-4 col-8",
		"far-right" : "1 2 col-8 col-4",
		"left" : "0 2 col-6 col-6",
		"right" : "1 2 col-6 col-6",
	}
	#dict of title sizes
	global titleSize
	titleSize = {
		"big" : "1",
		"bigger" : "1",
		"smaller" : "6",
		"small" : "5",
		"tiny" : "6",
		"average" : "3",
		"medium" : "3",
		"primary" : "1",
		"secondary" : "2",
		"tertiary" : "3",
	}



def displayText(text):
	if isinstance(text, str):
		print("\n\nbot>>\n"+text)
	elif isinstance(text, list):
		concatStr = "\n\nbot>>"
		for i in text:
			concatStr = concatStr + "\n" + str(i)
		print(concatStr)

def requestToUser(text=""):
	print("\n\nbot>>\n"+text)
	x = input ("\n\nyou>>\n")
	return x