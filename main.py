""" 
REMARQUES
Certaines balises necessitent d'être ouvertes puis fermées (cf div),
il faut prendre en compte le contenu qu'on peut vouloir mettre dedans

avoir la liste des ID deja utilisés pour eviter les erreurs

pour fermer les div, avoir une liste des div ouvertes, on add a la fin et on pop par la fin
si a la fin la liste est pas vide on pop et on add un closeDiv pour chaque element
on suppose que si l'utilisateur est con c'est pas de notre faute
=> pour l'instant on utilise un compteur de div ouvertes, plus tard on pourra essayer de gerer quelque chose avec les ID

type de balises et elements importants
Use dictionary for array

<p>
	class
	id
	inner

<div>
	class
	id
	inner!!!!!!

<a>
	class
	id
	href
	inner

<h> 
	class
	id
	size (1, 2, ...)
	inner

aussi err





dictionary 
myDict = {}
myDict["jeff"] = "jeff value"
#or
myDict = { "jeff":"jeff value", "max": "max value" }
print(myDict["jeff"])
#get keys : myDict.keys() => dict_key(["jeff", ...])
#length len(myDict)
#access item myDict.get("jeff")
#check if key (if "myKey" in myDict:)
myDict.update({"year": 2020}) #create if not exist
.pop() and .popitem() to remove, or (del myDict["jeff"])
.clear() #empty
for x in myDict (.keys(), .values(), .items())


"""
import htmlObject 
import htmlGenerate
import data
import userInteraction
import research

data.init()
userInteraction.init()