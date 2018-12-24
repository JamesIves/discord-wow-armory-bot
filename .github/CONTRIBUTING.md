## Contribution Guide
> Before contributing please review the [provided license](https://github.com/JamesIves/discord-wow-armory-bot/blob/master/LICENSE). 

Welcome and thank you for your interest in contributing to the Discord WoW Armory Bot project. Before you start writing code please post an [issue on Github](https://github.com/JamesIves/discord-wow-armory-bot/issues) with your idea so it can be disucssed. Once discussed please fork the repository and open a pull request with your feature, code should be commented and tested as much as possible before it will be accepted.

## Best Practices & Scope
There are a few key points to keep in mind when it comes to the scope of this project.

* Only data which is surfaced in official Blizzard API's should be used. Maintaining multiple third party API's can be a bit of a hassle, and not something the bot supports right now.
* Only data which is relevent to the current expansion should be used by the bot. This means that Legion raids shouldn't be added when BFA comes out, etc.
* Things such as raid and achievement id's should be added to the [constants.py](https://github.com/JamesIves/discord-wow-armory-bot/blob/master/constants.py) file, this makes the code much more readable.
