__module_name__ = "mass slaps"
__module_version__ = "0.1"
__module_description__ = "Mass slaps module by mablo"

import xchat

def make_slaps(users):
    message = "me slaps "+users
    xchat.command(message)

def mass_slaps(word, word_eol, userdata):
    users_list = xchat.get_list("users")
    users = ""
    for i in users_list:
        if len(users) > 350:
            make_slaps(users)
            users = i.nick+" "
        else:
            users = users+i.nick+" "
    make_slaps(users)
xchat.hook_command("all", mass_slaps) 
