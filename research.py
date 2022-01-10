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
	return ID

def findLast(objectType):
	#objectType is a string : p, a, img, opendiv, ...
	#return the ID of the object
	#return "err" if nothing found
	"""
	for x in data.listID:
		#print(x[0])
		#print(data.arrayHTML[x[0]])
		if data.arrayHTML[x[0]][0] == "p":
	"""
	res = "err"
	lenID = len(data.listID)
	for i in range(lenID):
		theID = data.listID[lenID-i-1][0]
		theObjectType = data.arrayHTML[theID][0]
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
		if (objectType == data.arrayHTML[objectID][0]):
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
	oldObject = data.arrayHTML[oldObjectID]
	data.displayText("oldObj : "+str(oldObject))
	resObjectClass = []
	resArg1 = ""
	resArg2 = ""
	while newObjectClass != []:
		resObjectClass.append(newObjectClass.pop())
	resObjectClass.append(oldObject[2])
	if ((newArg1 == "") and (oldObject[0] != "opdiv") and (oldObject[0] != "cldiv")):
		resArg1 = oldObject[3]
	elif ((newArg1 != "") and (oldObject[0] != "opdiv") and (oldObject[0] != "cldiv")):
		resArg1 = newArg1
	if ((newArg2 == "") and (oldObject[0] != "p") and (oldObject[0] != "opdiv") and (oldObject[0] != "cldiv")):
		resArg2 = oldObject[4]
	elif ((newArg2 != "") and (oldObject[0] != "p") and (oldObject[0] != "opdiv") and (oldObject[0] != "cldiv")):
		resArg2 = newArg2
	return resObjectClass, resArg1, resArg2