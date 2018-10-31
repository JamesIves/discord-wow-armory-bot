# World of Warcraft Armory Discord Bot ⚔️🗡️

[![Build Status](https://travis-ci.org/JamesIves/discord-wow-armory-bot.svg?branch=master)](https://travis-ci.org/JamesIves/discord-wow-armory-bot) [![Issues](https://img.shields.io/github/issues/JamesIves/discord-wow-armory-bot.svg)](https://github.com/JamesIves/discord-wow-armory-bot/issues)

With this bot you're able to lookup a World of Warcraft character's item level, notable achievements, and pve/pvp progression with a command within Discord. 

## Installation Steps :minidisc: 

1. Visit the Blizzard API site and sign up for an API key.
2. Visit the Discord API site and sign up. You'll need to create a bot user and retrieve the provided bot token.
3. Invite the bot to your server using the following URL, replacing the `YOUR_CLIENT_SECRET` portion with the one found within your Discord API settings: `https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENT_ID_HERE&scope=bot&permissions=0`
4. Click the button below and enter the required fields to deploy the bot to Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/JamesIves/discord-wow-armory-bot/master)

If you'd like to run the application outside of Heroku you can run add the required secrets as environment variables and then run the following commands using Python and Pip.

```
# Install & Run
$ pip install -r requirements.txt
$ python app.py

# Tests
$ python tests.py
```

## Configuration :file_folder: 

The installation button will require you to enter a number of API keys. Below you'll find an explanation of each.

| Key  | Value Information |
| ------------- | ------------- |
| `WOW_API_KEY`  | Required to make calls to the Blizzard API, you can sign up for a key [here](https://dev.battle.net/).  |
| `WOW_REGION`  | The server region you'd like to query, for example `us`, or `eu`.  |
| `LOCALE`  | The language for your selected WoW region, for example `en_US`, or `en_GB`. Locale depends on region. Please refer to the [Blizzard API documents](https://dev.battle.net/) for more information. At this time this bot will only return data in English.   |
| `DISCORD_BOT_TOKEN`  | The token for your Discord bot user, you can sign up for one [here](https://discordapp.com/developers/docs/intro). |

If a variable is missing the terminal you executed the bot from will display an error message.


## Commands :computer: 
The following commands are accepted by the bot.

```
# Displays a players PVE progression, dungeon kills, keystone achievements, etc.
!armory pve <name> <realm>
!armory pve <armory-link>

# Displays a players PVP progression, arena ratings, honorable kills, etc.
!armory pvp <name> <realm>
!armory pvp <armory-link>

# You can also provide an optional region to each query to display players from other WoW regions outside of the bot default, for example EU, US, etc.
!armory pve <name> <realm> <region>
!armory pvp <armory-link> <region>

# Command list/help
!armory help
```

## FAQ :speech_balloon: 
Here's a list of frequently asked questions.
```
Q: Why does it show that my alt has completed an achievement?
A: Some achievements are account wide so the API response for your alt will be the same as your main.

Q: Do you plan on supporting Mythic+ scores?
A: Only if the official Blizzard API begins supporting their own metric.

Q: Why don't you show this raid?
A: I aim to support the most recent raids in the current expansion. Because Discord has a character limit I will start trimming the oldest raid in the current expansion if necessary.

Q: What expansion does this bot currently support?
A: Battle for Azeroth.
```

![Screenshot](assets/screenshot.png)
