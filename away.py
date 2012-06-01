#
# Away module for XChat.
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
#   /on - delete suffix from the nickname and disable 'away' mode
#   /off message - add suffix '`off' to the nickname and enable `away` mode (default message: 'I'm not on IRC. Leave a message.')
#

__module_name__ = 'Away script'
__module_version__ = '0.3'
__module_description__ = 'Away module'

import xchat, re

def on(word, wordEol, userData):
    nickname = xchat.get_info('nick')
    xchat.command('NICK ' + re.sub('`off$', '', nickname))
    xchat.command('BACK')
    return xchat.EAT_ALL

def off(word, wordEol, userData):
    nickname = xchat.get_info('nick')
    if (re.search('`off$', nickname) == None):
        xchat.command('NICK ' + nickname + '`off')
        message = 'I\'m not on IRC. Leave a message.'
        if len(word) > 3:
            message = wordEol[2]
        xchat.command('AWAY ' + message)
    else:
        xchat.prnt('You are \'Away\' now.')
    return xchat.EAT_ALL

xchat.hook_command('on', on)
xchat.hook_command('off', off)