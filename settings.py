#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

"""Application settings such as API keys are stored here."""

# World of Warcraft API Settings
WOW_CLIENT_ID = str(os.environ.get("WOW_CLIENT_ID"))
WOW_CLIENT_SECRET = str(os.environ.get("WOW_CLIENT_SECRET"))

WOW_REGION = str(os.environ.get("WOW_REGION"))
LOCALE = str(os.environ.get("LOCALE"))

# Discord API Settings
DISCORD_BOT_TOKEN = str(os.environ.get("DISCORD_BOT_TOKEN"))

# API Connection Errors
NOT_FOUND_ERROR = "Could not find a character with that name, realm or region combination. \
  Type `!armory help` for a list of valid commands. :hammer_pick:"
CONNECTION_ERROR = "There was an issue establishing a connection to the Blizzard API. \
  Please try again. :electric_plug:"
CREDENTIAL_ERROR = "There was an error generating the auth token. \
  Either the Blizzard auth API was not reachable or your Blizzard API credentials are not correct. :fire:"
UNKNOWN_ERROR = "An unknown error occurred while attempting to retrieve this character. \
  If this error continues to persist please create a bug report on Github: https://github.com/JamesIves/discord-wow-armory-bot/issues :space_invader:"
GOLD_ERROR = "There was an error retreiving the price of the WoW token for this region. Please try again. :electric_plug:"

