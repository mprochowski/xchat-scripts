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
#   /slap username message - slaps user (default message: 'around a bit with a large trout.')
#   /slap-all - slaps all users in channel
#

__module_name__ = 'Slap script'
__module_version__ = '0.8'
__module_description__ = 'Slap module'

import xchat  

def makeSlap(users, message = 'around a bit with a large trout.'):
    xchat.command('me slaps ' + users + ' ' + message)

def slapAll(word, wordEol, userData):
    usersList = xchat.get_list('users')
    usersToSlap = ''
    for i in usersList:
        if len(usersToSlap) > 300:
            makeSlap(usersToSlap[:-1])
            usersToSlap = i.nick + ' '
        else:
            usersToSlap = usersToSlap + i.nick + ' '
    makeSlap(usersToSlap[:-1])
    return xchat.EAT_ALL

def slap(word, wordEol, userData):
    if len(word) > 3:
        makeSlap(word[1], wordEol[2])
    else: 
        makeSlap(word[1])
    return xchat.EAT_ALL

xchat.hook_command('slap', slap)
xchat.hook_command('slap-all', slapAll)