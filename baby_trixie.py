import os
import subprocess
from trixie_functions import *


hello = "\n\nWelcome back Ma'am!\nWhat can I do for you?"
hello3 = "\nLet me know if you want to open another app, I'll wait.\n"
nope = "\nNo worries. Unfortunately I can't do much else at the moment. Learn more and give me more options!"
in_two = "\nAight! Which app? \n"
limits = "\nMy programing is limited. Give Me More Code!\n"
goodbye = "\nCatch ya next time!\n"


print(hello)
abc = ""
while True:
    abc = input("> ").lower()
    if abc == "open":
        print(in_two)
        bcd = input("> ").lower()
        if bcd == "quit":
            break
        elif bcd == "discord":
            print("Coming up!")
            os.startfile('C:\\Users\\fetidapple\\Desktop\\Discord.lnk')
        elif bcd == "ffxiv":
            from trixie_functions import ffxiv
            ffxiv()
        elif bcd == "destiny":
            print("""Gottcha. This one takes a while, why not go make some hot coco?""")
            os.startfile('C\\Users\\fetidapple\\Desktop\\Destiny 2.lnk')
            print(hello3)
        elif bcd == "movie":
            print("Initializing VLC Media Player")
            # set AACS_DEBUG_MASK=65535
            # set BD_DEBUG_MASK=512
            # set AACS_DEBUG_FILE=c:\temp\debuglog_aacs.txt
            # set BDPLUS_DEBUG_FILE=c:\temp\debuglog_bdplus.txt
            # set BD_DEBUG_FILE=c:\temp\debuglog_libbluray.txt
            subprocess.call('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')
            print(hello3)
        elif bcd == "calc":
            print("""What, I can't do enough math for you? Fine.""")
            subprocess.call('C:\\Windows\\System32\\calc.exe')
        else:
            print(f"""Sorry, I couldn't understand {bcd!r}""")
            print(limits)
    elif abc == "mini-game":
        print("Alright! You want a guessing game or a car game?")
        game_name = input("> ").lower()
        if game_name == "guess":
            guessing_game()
        elif game_name == "car":
            car_game()
    elif abc == "exit":
        print(goodbye)
        break
    else:
        print(f"""Sorry, I couldn't understand {abc!r}""")
