# NLP-project-chatbot_writing_web_page
This chat bot works in python, you can talk with it to create web pages. This is a work for my class of NLP at Unige




NLP PROJECT 
requierement python 3.7.9 or later
execution : python main.py

What it is ?
	a chat bot you can talk to that take a description of a web page and give you back the html of what you described

How does it work ?
	understand simple sentences (with one action per sentence) and use Bootstrap class for handling JS and CSS

Action recognised :
	create/make/add an object (paragraph, image, link, ...)
	create/make/add (open) a div
	close a div
	modify/change/find an existing object
	delete an object




test tried:
Giving certain sentences can trigger an answer from the program asking for more details about your request.
"a > b" means that after saying a you should say b when the program asks for details in order to get the same results.

	metadata > 1 > a title > save > it works
	metadata > 1 > another title > save > it works
	metadata > 2 > Clement Guerin > save > it works
	metadata > 3 > something > save > it works
	metadata > 3 > something else > save > it works
	metadata > 4 > Sofia > save > it works
	metadata > 4 > Roboto Mono > save > it works
	metadata > gdsi > return error > it works

	create paragraph > blabla > save > it works
	create title > 1 > monTitre > save > it works
	create title > a > return error > it works
	create link > http://truc > myLinkDisplayName > save > it works
	create image > img.png > altName > save > it works
	create div > save > it works
	(same with (in the create command), id:bla, class:blo, class:bli and class:blu)

	close div > save > it works

	modify last paragraph > blablabla > save > it works
	modify last title > 1 > myTitle > save > it works
	modify last image > test.jpg > alt-text > save > it works
	modify last link > asd > asads > save > it works
	(same with class:[x1 or x2] but not id:)

	modify class:myClass > save > it works (add some class to the last object)

	add blue paragraph > qwerrty > save > it works
	add red div > add blue paragraph > eywutr > save > it works
	add blue text > uydsagcf > save > it works

	add title > 1 > tfe > add text > dft > delete last title > it works
	add text > fyer > add text > yfeu > delete all > it works
	(cannot delete last div to avoid because of column and rows handling difficulties)

	add a big title > myTitle > it works
	add small title > otherTitle > it works
	add primary title > qwe > add secondary title > fheiw > it works

	using small, quarter, ... for column sizing (need row)



For more informations, see report.doc




Original subject:

The user will be able to tell the program to edit the Header and the Body of the html document
Header :
- add a font from googlefont link
- change the title of the page
- add metadata
Body :
- add object
- select a color for the object
- add parameters to the object
- add photo from web link
- chose placement 
- delete object
- move an object
- change parameters of an object

A first approach would be to use simple sentences containing the name of the object we want and the list of Bootstrap classes to have a first working program.
Then we could try more elaborate sentences with text recognition, trying to understand colors, placement, size, ... using NLTK or TextBlob. I don't know if this would be necessary because there might not be that much vocabulary to handle and hard coding everything might be enough. For example for the size : bigger, smaller, bolder, ...; for the color : red, light red, dark red, blue, ... 

With ID/Class identification we can store the requests in an array and later come back to those elements to modify them. For example "write the title bigger" would make all the h2 in h1, "put the paragraph #p1 in blue" would search for a paragraph with the #p1 ID and change its color for blue, ... 
