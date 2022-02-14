"""
Contain the functions requiered to create basic html elements

createHTML and endHTML return raw html
other functions returns parameters to create html elements with the functions in htmlGenerate
"""

import data


def createParagraph(pID, pClass, pText):
	#return a dictionary item 
	item = {str(pID): ["p", pID, pClass, pText]}
	return item

def createHeader(hID, hClass, hSize, hText):
	#return a dictionary item 
	#check if the size is correct (h1, h2, ...)
	if hSize in ["1", "2", "3", "4", "5", "6"]:
		item = {str(hID): ["h", hID, hClass, hSize, hText]}
	else:
		item = {str(hID): ["err", hID+ "error : header size doesn't exist : "+hSize]}
	return item

def createLink(lID, lClass, lHref, lText):
	#return a dictionary item
	item = {str(lID): ["a", lID, lClass, lHref, lText]}
	return item

def createImage(imgID, imgClass, imgSRC, imgAlttext):
	#return a dictionary item
	item = {str(imgID): ["img", imgID, imgClass, imgSRC, imgAlttext]}
	return item

def createOpenDiv(dID, dClass):
	#return a dictionary item 
	#global data.countOpenDiv 
	data.countOpenDiv+=1
	item = {str(dID): ["div", dID, dClass]}
	return item

def createCloseDiv(dID):
	#return a dictionary item 
	#global data.countOpenDiv
	if data.countOpenDiv:
		data.countOpenDiv-=1
		item = {str(dID): ["cldiv"]}
	else:
		item = {str(dID): ["err", dID+ "error : try to close div that doesn't exist : "]}
	return item

def createHTML():
	res = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\">\n"
	for [typeMeta, contentMeta] in data.metadata:
		res = res + contentMeta + "\n"
	res += "</head>\n<body>\n"
	return res

def endHTML():
	return "<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p\" crossorigin=\"anonymous\"></script>\n</body>\n</html>\n"
