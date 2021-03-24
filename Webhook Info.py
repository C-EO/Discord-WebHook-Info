# Modules importation
import os
try:
    from dhooks import Webhook
except:
    os.system("py -m pip install dhooks")
    from dhooks import Webhook
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
    
init()
banner = (Fore.MAGENTA + """
  █     █░▓█████  ▄▄▄▄    ██░ ██  ▒█████   ▒█████   ██ ▄█▀    ██▓ ███▄    █   █████▒▒█████
 ▓█░ █ ░█░▓█   ▀ ▓█████▄ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
 ▒█░ █ ░█ ▒███   ▒██▒ ▄██▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░    ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
 ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄    ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
 ░░██▒██▓ ░▒████▒░▓█  ▀█▓░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
 ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░
   ▒ ░ ░   ░ ░  ░▒░▒   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░
   ░   ░     ░    ░    ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒
     ░       ░  ░ ░       ░  ░  ░    ░ ░      ░ ░  ░  ░       ░           ░            ░ ░\n""" + Fore.LIGHTCYAN_EX)

print(banner)
hook = Webhook(input(" WEBHOOK : "))
hook.get_info()
print(f"\n GUILD ID    : {hook.guild_id}")
print(f" CHANNEL ID  : {hook.channel_id}")
print(f" USERNAME    : {hook.default_name}")
print(f" IMAGE       : {hook.default_avatar_url}")
os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
exit()
