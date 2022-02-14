"""
Functions that handle the interactions between user and the programm
Functions that "understand" what the user want
"""

import htmlObject 
import htmlGenerate
import data
import research

def init():
	#keep asking you what you want until you ask it to stop and then it end the programm
	data.displayText("Hello I'm a bot, I write html documents.\nAsk me to add things and I'll do it, \n\"stop\" to quit, \"save\" to get the code\n\"metadata\" to change the header content")
	x = data.requestToUser("i'm listening :")
	while(x!="stop"):
		if (x=="save"):
			saveFile()
			x = data.requestToUser("what else can I do for you ?")
		elif (x=="metadata"):
			#print("you ask metadata")
			changeMeta()
			x = data.requestToUser("what else can I do for you ?")
		else:
			action, objectType, objectClass, objectID, arg1, arg2, arg3 = inputWordExtraction(x)
			inputDataTreatment(action, objectType, objectClass, objectID, arg1, arg2, arg3)
			x = data.requestToUser("what else can I do for you ?")
	data.displayText("okay bye")


def saveFile():
	#take all the data in arrayHTML to generate the html code
	f = open("test.html", "w")
	f.write(htmlGenerate.generateHTML())
	f.close()
	data.displayText("file save in test.html")

def changeMeta():
	x = data.requestToUser("\"1\" or \"title\"  to change page title \n\"2\" or \"author\" to change author\n\"3\" or \"description\" to change description :\n\"4\" or \"font\" to add google font \n")
	#print("you typed "+x)
	if (x=="1") or (x=="title"):
		y = data.requestToUser("what title do you want your page to have : ")
		y = "<title>"+y+"</title>"
		#<title></title>
		condition = True
		temp = []
		while (data.metadata != []):
			tempMeta = data.metadata.pop()
			if tempMeta[0] == "title":
				tempMeta[1] = y 
				condition = False
			temp.append(tempMeta)
		while (temp != []):
			data.metadata.append(temp.pop())
		if condition:
			data.metadata.append(["title", y])
	elif (x=="2") or (x=="author"):
		y = data.requestToUser("author name : ")
		y = "<meta name=\"author\" content=\""+y+"\">"
		data.metadata.append(["author", y])
	#<meta name="" content="">
	elif (x=="3") or (x=="description"):
		y = data.requestToUser("description content : ")
		y = "<meta name=\"description\" content=\""+y+"\">"
		condition = True
		temp = []
		while (data.metadata != []):
			tempMeta = data.metadata.pop()
			if tempMeta[0] == "description":
				tempMeta[1] = y 
				condition = False
			temp.append(tempMeta)
		while (temp != []):
			data.metadata.append(temp.pop())
		if condition:
			data.metadata.append(["description", y])
	elif (x=="4") or (x=="font"):
		y = data.requestToUser("font name : ")
		z = "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family="+y.strip().replace(" ", "+")+"\">"
		z = z+"<style>body {font-family: \""+y+"\";}</style>"
		data.metadata.append(["font", z])
	else:
		data.displayText("something went wrong, you wrote \""+x+"\", only 1,2,3 accepted")

def listToString(myList):
	#take a list of string and concat them
	res = ""
	for x in myList:
		res += x + " "
	return res


def inputWordExtraction(myInput):
	
	#create variables
	arrayWords = myInput.split(" ")
	action, objectType, objectClass, objectID = "none", "none", [], ""
	arg1, arg2, arg3 = "", "", ""
	color = ""
	#search for words

	#search for actions
	if ("metadata" in arrayWords):
		changeMeta()
		action = "skip"
		return action, objectType, objectClass, objectID, arg1, arg2, arg3
	elif ("save" in arrayWords):
		saveFile()
		action = "skip"
		return action, objectType, objectClass, objectID, arg1, arg2, arg3
	elif (("create" in arrayWords) or ("make" in arrayWords) or ("add" in arrayWords)):
		data.displayText("I understand that you want to create something")
		action = "make"
	elif (("close" in arrayWords) and ("div" in arrayWords)):
		data.displayText("I understand that you want to close a div")
		action = "make"
		objectType = "closeDiv"
	elif (("find" in arrayWords) or ("modify" in arrayWords) or ("change" in arrayWords)):
		data.displayText("I understand that you want to modify some already existing elements")
		action = "change"
		if ("all" in arrayWords):
			arg3 = "all"
		elif ("last" in arrayWords):
			arg3 = "last"
		else:
			arg3 = "last"
	elif ("delete" in arrayWords):
		action = "delete"
		if ("all" in arrayWords):
			arg3 = "all"
		elif ("last" in arrayWords):
			arg3 = "last"
		else:
			arg3 = "last"
	else: 
		data.displayText("no action keyword find, using last element")
		action = "change"
	#search for object type
	if ("paragraph" in arrayWords or "text" in arrayWords):
		data.displayText("you are talking about a paragraph")
		objectType = "p"
		if action != "delete":
			arg1 = data.requestToUser("what do you want to write in your paragraph : ")
		for tempPlace in arrayWords:
			if tempPlace in data.placementRelation.keys() and arg3 == "":
				arg3 = tempPlace
	if "title" in arrayWords:
		data.displayText("you are talking about a title")
		objectType = "h"
		if action != "delete":
			for temp in arrayWords:
				if temp in data.titleSize.keys():
					arg1 = data.titleSize[temp]
			if arg1 == "":
				arg1 = data.requestToUser("what size you want you title ? [1,6] : ")
				while (arg1 not in ["1", "2", "3", "4", "5", "6"]):
					data.displayText("error incorect value")
					arg1 = data.requestToUser("what size you want you title ? [1,6] : ")
			arg2 = data.requestToUser("what do you want you title to say? : ")
		for tempPlace in arrayWords:
			if tempPlace in data.placementRelation.keys() and arg3 == "":
				arg3 = tempPlace
	if "link" in arrayWords:
		data.displayText("you are talking about a href")
		objectType = "a"
		if action != "delete":
			arg1 = data.requestToUser("What do you want your link to point at ? : ")
			arg2 = data.requestToUser("What do you want your link to be displayed as ? : ")
	if "image" in arrayWords:
		data.displayText("you are talking about a image")
		objectType = "img"
		if action != "delete":
			arg1 = data.requestToUser("What is the source of you image ? : ")
			arg2 = data.requestToUser("Enter the alternative image text value : ")
		for tempPlace in arrayWords:
			if tempPlace in data.placementRelation.keys() and arg3 == "":
				arg3 = tempPlace
	if "div" in arrayWords:
		data.displayText("you are talking about a div")
		if objectType != "closeDiv":
			objectType = "div"
	if "row" in arrayWords:
		data.displayText("you are talking about a row")
		objectType = "div"
		if data.countNestedRow == 0:
			data.countNestedRow += 1
		elif "inside" in arrayWords:
			data.countNestedRow += 1
		else:
			data.countNestedRow -= 1
			#add close div 
			closeDivID = str(len(data.listID))
			htmlGenerate.addItemToDict(htmlObject.createCloseDiv(closeDivID))
		objectClass.append("row")
	if "column" in arrayWords or "col" in arrayWords:
		# search size
		tempClass = "col"
		for temp in arrayWords:
			if temp in data.sizeRelation.keys():
				tempClass = data.sizeRelation[temp]
		data.displayText("you are talking about a column")
		objectType = "div"
		if data.countNestedCol == 0:
			data.countNestedCol += 1
		elif "inside" in arrayWords:
			data.countNestedCol += 1
		else:
			#data.countNestedCol -= 1
			#add close div 
			closeDivID = str(len(data.listID))
			htmlGenerate.addItemToDict(htmlObject.createCloseDiv(closeDivID))
		objectClass.append(tempClass)

	#search for class and id
	for x in arrayWords:
		if "class:" in x:
			objectClass.append(x.replace("class:", ""))
		if "id:" in x:
			if objectID == "":
				objectID = x.replace("id:", "")
			else:
				data.displayText("too many IDs in your request, only the first one will be considered")
	#search for color
	for x in arrayWords:
		#if we find a color in the user request we add the color as a bootstrap class to the object
		if x in data.colorName:
			if (objectType in ["p", "a", "h"]):
				objectClass.append("text-" + data.colorName[x])
			elif (objectType in ["div", "img"]):
				objectClass.append("bg-" + data.colorName[x])
		if (x.replace("background-", "")!=x and x.replace("background-", "") in data.colorName):
			if (objectType in ["p", "a", "h", "div", "img"]):
				objectClass.append("bg-" + data.colorName[x.replace("background-", "")])


	#final print to recap the data found in request
	if (action == "change" and objectType=="none"):
		objectType = "theLast"
	if (action == "none" or objectType=="none"):
		data.displayText("I'm not sur to understand")
	data.displayText("action : "+action+"\nobjectType : "+objectType+"\nobjectClass : "+listToString(objectClass)+"\nobjectID : "+objectID+"\narg1 : "+arg1)

	#return results
	return action, objectType, objectClass, objectID, arg1, arg2, arg3


def inputDataTreatment(action, objectType, objectClass, objectID, arg1 = "", arg2 = "", arg3 = ""):
	#in python it is possible to call a function with defaut args
	#it is also possible to give the args in different order by giving their name
	#here we have some args that have default value because they are not useful all the time
	#this function is not supposed to get called by the user so we suppose the code calls it correctly
	#
	if (action == "skip"):
		return None
	#need to check objectID value
	if ((objectID == "") and (action != "change")):
		objectID = str(len(data.listID))#+objectType
		data.displayText("new objectID : "+objectID)
	if action == "make":
		#arg3 = "center", "middle", "left", ...
		info = [0, 0]
		sizes = []
		if arg3 != "":
			temp = data.placementRelation[arg3]
			temp = temp.split(' ')
			info[0] = int(temp[0])
			info[1] = int(temp[1])
			for a in range(info[1]):
				sizes.append(temp[a+2])
			tempID = str(len(data.listID)+1)
			htmlGenerate.addItemToDict(htmlObject.createOpenDiv(tempID, "row"))
			for b in range(info[0]):
				tempID = str(len(data.listID)+1)
				htmlGenerate.addItemToDict(htmlObject.createOpenDiv(tempID, sizes[b]))
				tempID = str(len(data.listID)+1)
				htmlGenerate.addItemToDict(htmlObject.createCloseDiv(tempID))
			tempID = str(len(data.listID)+1)
			htmlGenerate.addItemToDict(htmlObject.createOpenDiv(tempID, sizes[info[0]]))

		if (objectType == "p"):
			#arg1: inside text
			htmlGenerate.addItemToDict(htmlObject.createParagraph(objectID, listToString(objectClass), arg1))
		elif (objectType == "h"):
			#arg1: title size (1-6)
			#arg2: inside text
			htmlGenerate.addItemToDict(htmlObject.createHeader(objectID, listToString(objectClass), arg1, arg2))
		elif (objectType == "a"):
			#arg1: href
			#arg2: inside text
			htmlGenerate.addItemToDict(htmlObject.createLink(objectID, listToString(objectClass), arg1, arg2))
		elif (objectType == "img"):
			#arg1: src
			#arg2: alt
			htmlGenerate.addItemToDict(htmlObject.createImage(objectID, listToString(objectClass), arg1, arg2))
		elif (objectType == "div"):
			htmlGenerate.addItemToDict(htmlObject.createOpenDiv(objectID, listToString(objectClass)))
		elif (objectType == "closeDiv"):
			htmlGenerate.addItemToDict(htmlObject.createCloseDiv(objectID))
		else:
			data.displayText("error in request treatment, arg for inputDataTreatment:objectType not correct")
	
		if arg3 != "":
			tempID = str(len(data.listID))
			htmlGenerate.addItemToDict(htmlObject.createCloseDiv(tempID))
			# close remaining columns
			for c in range(info[0]+1, info[1]):
				tempID = str(len(data.listID))
				htmlGenerate.addItemToDict(htmlObject.createOpenDiv(tempID, sizes[c]))
				tempID = str(len(data.listID))
				htmlGenerate.addItemToDict(htmlObject.createCloseDiv(tempID))
			# close row
			tempID = str(len(data.listID))
			htmlGenerate.addItemToDict(htmlObject.createCloseDiv(tempID))

	elif action == "change":
		#arg3 = "all" or "last"
		if (objectType == "theLast"):
			objectID = research.findLastObject()
			objectType = research.findTypeWithID(objectID)
			if (objectType != "theLast"):
				inputDataTreatment(action, objectType, objectClass, objectID, arg1, arg2, "last")
			else:
				data.displayText("no object already created")
		elif ((objectID == "") and (arg3 == "last")):
			objectID = research.findLast(objectType)[0]
			if objectID == "err":
				data.displayText("err there is no such object already existing")
			else:
				#updateItemInDict(myItem)
				nObjClass, nArg1, nArg2 = research.compareObject(objectID, objectClass, arg1, arg2, arg3)
				#objectID.replace(objectType, "")
				if (objectType == "p"):
					#arg1: inside text
					htmlGenerate.updateItemInDict(htmlObject.createParagraph(objectID, listToString(nObjClass), nArg1))
				elif (objectType == "h"):
					#arg1: title size (1-6)
					#arg2: inside text
					htmlGenerate.updateItemInDict(htmlObject.createHeader(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "a"):
					#arg1: href
					#arg2: inside text
					htmlGenerate.updateItemInDict(htmlObject.createLink(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "img"):
					#arg1: src
					#arg2: alt
					htmlGenerate.updateItemInDict(htmlObject.createImage(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "div"):
					htmlGenerate.updateItemInDict(htmlObject.createOpenDiv(objectID, listToString(nObjClass)))
					# we use createOpenDiv() that add 1 to countOpenDiv but we just modify an already existing one so we substract 1
					data.countOpenDiv-=1
				#elif (objectType == "closeDiv"):
				#	htmlGenerate.updateItemInDict(htmlObject.createCloseDiv(objectID))
				else:
					data.displayText("error in request treatment, arg for inputDataTreatment:objectType not correct")
		elif ((objectID != "") and (arg3 == "last")):
			if objectID == "err":
				data.displayText("err there is no such object already existing")
			else:
				#updateItemInDict(myItem)
				nObjClass, nArg1, nArg2 = research.compareObject(objectID, objectClass, arg1, arg2, arg3)
				#objectID.replace(objectType, "")
				if (objectType == "p"):
					#arg1: inside text
					htmlGenerate.updateItemInDict(htmlObject.createParagraph(objectID, listToString(nObjClass), nArg1))
				elif (objectType == "h"):
					#arg1: title size (1-6)
					#arg2: inside text
					htmlGenerate.updateItemInDict(htmlObject.createHeader(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "a"):
					#arg1: href
					#arg2: inside text
					htmlGenerate.updateItemInDict(htmlObject.createLink(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "img"):
					#arg1: src
					#arg2: alt
					htmlGenerate.updateItemInDict(htmlObject.createImage(objectID, listToString(nObjClass), nArg1, nArg2))
				elif (objectType == "div"):
					htmlGenerate.updateItemInDict(htmlObject.createOpenDiv(objectID, listToString(nObjClass)))
					# we use createOpenDiv() that add 1 to countOpenDiv but we just modify an already existing one so we substract 1
					data.countOpenDiv-=1
				#elif (objectType == "closeDiv"):
				#	htmlGenerate.updateItemInDict(htmlObject.createCloseDiv(objectID))
				else:
					data.displayText("error in request treatment, arg for inputDataTreatment:objectType not correct")
	elif action == "delete":
		#arg3 = "all" or "last"
		if arg3 == "all" and objectType == "none":
			data.init()
		elif arg3 == "last" and objectType == "none":
			objectID = research.findLastObject()
			htmlGenerate.deleteItemInDict(objectID[0])
			data.listID.remove(objectID)
		elif arg3 == "last" and objectType != "none" and objectType != "div":
			objectID = research.findLast(objectType)
			htmlGenerate.deleteItemInDict(objectID[0])
			data.listID.remove(objectID)