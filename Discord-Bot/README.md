- Setup
* how to get an API token
	- For this instance, you can get an API token by first creating an application, and then a bot, and then a server. The bot will give you a token to refer to it with. An API token is like a password and you can even have your API regenerate this token if it compromised by going to the bot tab and selecting regenerate.

* where to put it to work with the code
	- You put the Token in the .env file and your code reads it with dotenv and allows you to keep your secrets. The .env is important to keep seperate and remain untracked so you do not expose your token. 

* dependencies (what packages need to be installed to run the code)
	- your program depends on the installation of python3, discord.py, and python-dotenv packages.

* Usage
	- When you type "talk!", the bot will respond to a random quote from the movie "Step Brothers". For example, when i type "talk!", the bot responds with the quote "That is so funny, the last time I heard that I laughed so hard I fell off my dinosaur."
* Research
* 	- One possible solution is hosting the program on a server. This would work because the server will wait for the computer/user to respond and will provide a response.
	- Another possible solution could be buying a server that runs a bot 24/7. Using a remote computer program can run a bot 24/7. if you want to have a server running 24/7, you'd have to buy, or rent a server.
