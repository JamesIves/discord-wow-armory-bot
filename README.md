# World of Warcraft Armory Discord Bot
This is a simple Discord bot built on [discord.py](https://github.com/Rapptz/discord.py) using [Python 3.6.1](https://www.python.org/). You're able to enter a character name and realm to get a quick view at a characters item level, notable achievements, and raid progression.


## Requirements
This application requires [Python 3.6.1](https://www.python.org/) and the following packages which can be installed via pip.

```
discord.py==0.16.7
requests==2.14.2
```


## Configuration
In order to power this bot you'll require a Discord API bot token, and an API key for the Blizzard API. These credentials are stored as environment variables.

| Key  | Value Information |
| ------------- | ------------- |
| `WOW_API_KEY`  | Required to make calls to the Blizzard API, you can sign up for a key [here](https://dev.battle.net/).  |
| `WOW_REGION`  | The server region you'd like to query, for example `us`.  |
| `LOCALE`  | The language for your selected WoW region, for example `en_US`. Locale depends on region, please refer to the [Blizzard API documents](https://dev.battle.net/) for more information. At this time this bot will only return data in English.   |
| `DISCORD_BOT_TOKEN`  | The token for your Discord bot user, you can sign up for one [here](https://discordapp.com/developers/docs/intro). |


## Running the Application
This application can be executed by running `$ python3 app.py`. This will initialize the script and connect the bot to the server.


## Deploying to Heroku
This bot can be deployed to [Heroku](https://www.heroku.com), simply deploy the most recent version and assign your free dyno to the worker specified in the Procfile. You then need to type the following in the terminal.

```
$ heroku ps:scale --app discord-wow-armory-bot worker=1
```

You'll also need to setup your config variables within the `Settings` tab.


## Commands
The following commands are accepted.

```
# PVP/Arena Ratings
!armory pvp Helenek illidan

# PVE Progression/Raids
!armory pve Jimo burning-legion

# Command List
!armory help

# Command Formatting
!armory <content> <name> <realm>
```

![Screenshot](assets/screenshot.png)
