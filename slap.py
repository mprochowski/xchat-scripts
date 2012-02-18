#
# Slap module for XChat.
#
# Author: Michal Prochowski <michal@prochowski.pl>
# URL: http://github.com/mablo/xchat-scripts
#
# Copyright(c) 2012 Michal Prochowski
# License: MIT
#
# Installation:
#   Copy script to ~/.xchat2/ directory or load module in XChat.
#
# Usage:
#   /slapall - slaps all users in channel
#   /slap username - slaps user
#

__module_name__ = "Slap script"
__module_version__ = "0.7"
__module_description__ = "Slap module"

import xchat  

def slapAll(word, wordEol, userData):
    usersList = xchat.get_list("users")
    usersToSlap = ""
    for i in usersList:
        if len(usersToSlap) > 300:
            xchat.command("me slaps " + usersToSlap + " around a bit with a large trout.")
            usersToSlap = i.nick + " "
        else:
            usersToSlap = usersToSlap + i.nick + " "
    xchat.command("me slaps " + usersToSlap + " around a bit with a large trout.")
    return xchat.EAT_ALL

def slap(word, wordEol, userData):
    xchat.command("me slaps " + word[1] + " around a bit with a large trout.")
    return xchat.EAT_ALL

xchat.hook_command("slap", slap)
xchat.hook_command("slapall", slapAll)