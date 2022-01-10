"""
Create all the global variables requiered to make the project work
Display function and requests functions
easier to create an UI from these functions than if we use prints in the code
"""

def init():
	global arrayHTML
	arrayHTML = {}
	#dictionary of the html elements
	global listID
	listID = []
	#list of the string of the ID used
	global countOpenDiv
	countOpenDiv = 0
	#int of the number of div not closed
	global metadata
	metadata = []
	#list of the [type, strings] of metadata to put in the head
	#type : title, author, descrition


def displayText(text=""):
	print("\n\nbot>>\n"+text)

def requestToUser(text=""):
	print("\n\nbot>>\n"+text)
	x = input ("\n\nyou>>\n")
	return x