"""
functions used to search something in the data
"""
import data

def findLastObject():
	#give back the ID of the last elem in the list
	lenID = len(data.listID)
	ID = "err"
	if lenID != 0:
		ID = data.listID[lenID-1]
	data.displayText("last object ID : "+str(ID))
	return ID

def findLast(objectType):
	#objectType is a string : p, a, img, opendiv, ...
	#return the ID of the object
	#return "err" if nothing found
	res = "err"
	lenID = len(data.listID)
	for i in range(lenID):
		theID = data.listID[lenID-i-1]
		theObjectType = data.arrayHTML[theID[0]][0]
		if theObjectType == objectType :
			if res=="err":
				res=theID
	return res

def findAll(objectType):
	#objectType is a string : p, a, img, opendiv, ...
	#return the list of ID of the objects with this type
	#return "err" if nothing found
	res = []
	lenID = len(data.listID)
	for i in range(lenID):
		theID = data.listID[lenID-i-1]
		theObjectType = data.arrayHTML[theID][0]
		if theObjectType == objectType :
			res.append(theID)
	if res == [] :
		res = "err"
	return res

def findWithIDandType(objectType, objectID):
	#objectType is a string : p, a, img, opendiv, ...
	#return the ID of the object
	#return "err" if nothing found
	res = "err"
	if (objectID in data.listID):
		if (objectType == data.arrayHTML[objectID[0]][0]):
			res = objectID
	return res

def findTypeWithID(objectID):
	#objectType is a string : p, a, img, opendiv, ...
	#return the ID of the object
	#return "err" if nothing found
	res = "err"
	if (objectID in data.listID):
		#print(objectID[0])
		#print(data.arrayHTML)
		res = data.arrayHTML[objectID[0]][0]
	return res

def compareObject(oldObjectID, newObjectClass = [], newArg1 = "", newArg2 = "", newArg3 = ""):
	#compare the new item to the object with the ID given in parameter
	oldObject = data.arrayHTML[oldObjectID[0]]
	data.displayText("oldObj : "+str(oldObject))
	resObjectClass = []
	resArg1 = ""
	resArg2 = ""

	if ((newArg1 == "") and (oldObject[0] != "div") and (oldObject[0] != "cldiv")):
		resArg1 = oldObject[3]
	elif ((newArg1 != "") and (oldObject[0] != "div") and (oldObject[0] != "cldiv")):
		resArg1 = newArg1
	if ((newArg2 == "") and (oldObject[0] != "p") and (oldObject[0] != "div") and (oldObject[0] != "cldiv")):
		resArg2 = oldObject[4]
	elif ((newArg2 != "") and (oldObject[0] != "p") and (oldObject[0] != "div") and (oldObject[0] != "cldiv")):
		resArg2 = newArg2


	# the next part is here to assure that we don't have 2 different class that affect the same property 
	# it looks for text-color, background-color and opacity
	# this part of the code is not optimized and might be hard to read 
	# creating subfunctions for this part should be a good idea
	conditionClass = False
	while newObjectClass != []:
		tempClass = newObjectClass.pop()
		resObjectClass.append(tempClass)
		#check if the class is a color or an opacity
		#conditionClass = False 
		colorClass = []
		opacityClass = []
		if tempClass.replace("text-","").replace("bg-","").strip() in data.colorName.values():
			conditionClass = True
			colorClass.append(tempClass)
		if tempClass.replace("text-","").replace("bg-","").strip().split("-",1)[0] == "opacity":
			conditionClass = True
			opacityClass.append(tempClass)
	if conditionClass:
		resTempObjClass = []
		while (colorClass!=[] and opacityClass!=[]):
			tempColClass = ""
			tempOpaClass = ""
			if colorClass != []:
				tempColClass = colorClass.pop()
			if opacityClass != []:
				tempOpaClass = opacityClass.pop()

			oldClass = oldObject[2].split(" ")
			colorIdentifier = tempColClass.split("-", 1)[0]
			opacityIdentifier = tempOpaClass.split("-", 1)[0]
			while oldClass != []:
				tempClass = oldClass.pop()
				if (colorIdentifier != "" and colorIdentifier in tempClass and colorIdentifier+"opacity" not in tempClass):
					#do nothing
					pass
				elif (opacityIdentifier != "" and opacityIdentifier+"opacity" in tempClass):
					#do nothing
					pass
				else:
					resTempObjClass.append(tempClass)
			oldClass = resTempObjClass.copy()
		while resTempObjClass!=[]:
			resObjectClass.append(resTempObjClass.pop())
	else:
		resObjectClass.append(oldObject[2])

	return resObjectClass, resArg1, resArg2