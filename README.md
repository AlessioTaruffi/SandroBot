# SandroBot
A small discord bot to perform basic tasks related to the game "Escape From Tarkov" like checking the price of an item or the requirements to complete a given quest.

# How it Works
The bot uses Tarkov.dev's open APIs to get every information it then displays on text.  
The bot has 3 slash commands: 
- **/fleaprice** Takes the name of an object as its input and returns the object's ID, its name, short name and price history. The bot return every object the API returns, so if the name is not specific enough given how Tarkov.dev's APi work it will output every object whose full name contains the input string; 
- **/map** Allows the user to select the name of a map and return a 2d map of it and a link to the original file to enable the user to better see smaller objectives; 
- **/task** Takes the name of a task as its input and returns name, description, objectives and maps relative to the selected quest(s) and a link to the wiki article about it for further reading. 

# How to Use It
At the moment the bot works on a single server whose ID needs to be specified in the cog file. I had no need for the bot to be present on multiple server so that's how i made it.
To make the bot work on your personal server, first create a Discord bot via Discord's Developer Portal. Then copy the ID of the server you want the bot to be in inside the code at the end of "24hPriceMenu.py". Then invite the bot inside your server. 
In order to run the bot also needs its personal token. To do so, create a .env file inside the root directory and add the following: 
***
DISCORD_TOKEN=yourDiscordBotToken
***
Now just install the needed libraries and run ***python ./bot.py***

A huge thank you to the guys over at Tarkov.dev for making their APIs completely open source.
