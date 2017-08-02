#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

"""Application settings such as API keys are stored here."""

# World of Warcraft API Settings
WOW_API_KEY = str(os.environ.get('WOW_API_KEY'))
WOW_REGION = str(os.environ.get('WOW_REGION'))
LOCALE = str(os.environ.get('LOCALE'))

# Discord API Settings
DISCORD_BOT_TOKEN = str(os.environ.get('DISCORD_BOT_TOKEN'))