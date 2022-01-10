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

Action to implement :
	delet object
	research object
	modify object
	(the three by ID, by objectType and last one)
	change object order maybe ? 

ideas : 
	use "make" for modification not creation 
	implement more objects (navbar, tooltips, ...)
	change style for a substring of a paragraph

Pb :
	when modifying paragraph ID error p0 -> 0 but pp0 
	weird


test effectués 
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

	modify last paragraph > blablabla > save > DON'T WORK

	(same with class:[x1 or x2] but not id:)
























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





manual placement (bootstrap reminder)

grid:
class:row and class:col to align elements 
to select size according to the screen you can use a number between 1 and 12 
for example class:col-6 will create a div that take half of the screen
Be sure to close div between two column, or you will create a row inside the column


Font usage

you need to get the google font name of the font 
in metadata select 4 and follow instructions 
You can only use one font at the moment 
font to try Sofia, Trirong, Audiowide, Tangerine, Roboto Mono, ...








buttons
gestion rows and cols without saying div
gestion font not all doc (on/off)



<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled">Disabled</a>
      </div>
    </div>
  </div>
</nav>
