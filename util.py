#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def split_query(message, content):
    """Helper function that splits a string and returns data
    in a predictable order. """

    # If the word 'worldofwarcraft' or 'battle.net' exist
    # it splits the string starting at 'character/'
    if 'worldofwarcraft' in message or 'battle.net' in message:
        url = re.split('\\bcharacter/\\b', message)[-1]
        split = url.split('/')
        return [split[1], split[0], content]

    # Assumes it's not a url path, and splits the string normally.
    else:
        split = message.split(' ')
        return [split[2], split[3], content]
