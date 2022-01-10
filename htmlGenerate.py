import data
import htmlObject

def generateHTML():
	res = htmlObject.createHTML()
	for x in data.listID:
		#print(x[0])
		#print(data.arrayHTML[x[0]])
		if data.arrayHTML[x[0]][0] == "p":
			res += "<p id=\"" +data.arrayHTML[x[0]][1] +"\" class=\"" +data.arrayHTML[x[0]][2] +"\">" +data.arrayHTML[x[0]][3] +"</p>\n"
		elif data.arrayHTML[x[0]][0] == "opdiv":
			res += "<div id=\"" +data.arrayHTML[x[0]][1] +"\" class=\"" +data.arrayHTML[x[0]][2] +"\">\n"
		elif data.arrayHTML[x[0]][0] == "cldiv":
			res += "</div>\n"
		elif data.arrayHTML[x[0]][0] == "h":
			res += "<h" +data.arrayHTML[x[0]][3] +" id=\"" +data.arrayHTML[x[0]][1] +"\" class=\"" +data.arrayHTML[x[0]][2] +"\">" +data.arrayHTML[x[0]][4] +"</h" +data.arrayHTML[x[0]][3] +">\n"
		elif data.arrayHTML[x[0]][0] == "err":
			res += "<!-- " +data.arrayHTML[x[0]][1] +"-->\n"
		elif data.arrayHTML[x[0]][0] == "a":
			res += "<a id=\"" +data.arrayHTML[x[0]][1] +"\" class=\"" +data.arrayHTML[x[0]][2] +"\" href=\"" +data.arrayHTML[x[0]][3] +"\">" +data.arrayHTML[x[0]][4] +"</a>\n"
		elif data.arrayHTML[x[0]][0] == "img":
			res += "<img id=\"" +data.arrayHTML[x[0]][1] +"\" class=\"" +data.arrayHTML[x[0]][2] +"\" src=\"" +data.arrayHTML[x[0]][3] +"\" alt=\"" +data.arrayHTML[x[0]][4] +"\">\n"
	for i in range(data.countOpenDiv):
		res += "</div>\n"
	res+=htmlObject.endHTML()
	return res

def addItemToDict(myItem):
	'''myDict.update(myItem)
	data.listID.append(myItem.keys())'''
	if list(myItem.keys()) in data.listID:
		data.displayText("you tried to add item but it already exist")
		#updateItemInDict(myDict, myItem, data.listID)
	else:
		data.arrayHTML.update(myItem)
		data.listID.append(list(myItem.keys()))

def updateItemInDict(myItem):
	data.displayText(data.listID)
	data.displayText(myItem)
	data.displayText(list(myItem.values())[0][1])
	data.arrayHTML.update(myItem)

#myItem.keys()
"""
def updateItemInDict(myItem):
	if list(myItem.values())[0][1] in data.listID:
		data.arrayHTML.update(myItem)
	else:
		print("bot>> you tried to update an item but it didn't exist\n")
"""