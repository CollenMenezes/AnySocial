#!/bin/python3

import requests
import os
import time


def main():

    class Color:
        WARNING = '\033[93m'
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        END = '\033[0m'
        BD = "\033[1m"

    #banner
    def logo():
        os.system("clear")
        print (f"     _                      {Color.FAIL}____{Color.END}                   _           _ ")
        print (f"    / \     _ __    _   _  {Color.FAIL}/ ___|{Color.END}    ___     ___  (_)   __ _  | |")
        print (f"   / _ \   | '_ \  | | | | {Color.FAIL}\___ \{Color.END}   / _ \   / __| | |  / _` | | |")
        print (f"  / ___ \  | | | | | |_| |  {Color.FAIL}___) |{Color.END} | (_) | | (__  | | | (_| | | |")
        print (f" /_/   \_\ |_| |_|  \__, | {Color.FAIL}|____/{Color.END}   \___/   \___| |_|  \__,_| |_|")
        print ("                    |___/                                        ")
        print ("\n")
    #function scan
    def scan():

        global var_username
        logo()
        var_username = str(input("[-] ENTER USERNAME: "))

        while var_username == "":
            logo()
            print(f"[-] {Color.BD}THE USERNAME FIELD CANNOT BE EMPTY!{Color.END}")
            time.sleep(3)
            os.system("clear")
            logo()
            var_username = input("[-] ENTER USERNAME: ")


    scan()

    os.system("clear")
    logo()
    print (f"[-] {Color.BD}SEARCHING:{Color.END}", var_username)
    print ("\n")

    #YouTube check
    check_youtube = f"https://www.youtube.com/c/{var_username}"
    youtube_get = requests.get(check_youtube)
    if youtube_get.status_code == 404:
        print(f"[-] {Color.FAIL}YOUTUBE NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}YOUTUBE FOUND!{Color.END} https://www.youtube.com/c/{var_username}")

    #instagram check
    check_ig = f"https://www.instagram.com/{var_username}"
    ig_get = requests.get(check_ig)
    if ig_get == 200:
        print(f"[-] {Color.FAIL}INSTAGRAM NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}INSTAGRAM FOUND!{Color.END} https://www.instagram.com/{var_username}")
        
    #facebook check
    check_fb = f"https://www.facebook.com/{var_username}"
    fb_get = requests.get(check_fb)
    if fb_get.status_code == 404:
        print(f"[-]{Color.FAIL} FACEBOOK NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}FACEBOOK FOUND!{Color.END} https://www.facebook.com/{var_username}")

    #messenger check
    mess_check = f"https://www.messenger.com/t/{var_username}"
    mess_get = requests.get(mess_check)
    if mess_get.status_code == 404:
        print(f"[-]{Color.FAIL} MESSENGER NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}MESSENGER FOUND!{Color.END} https://www.messenger.com/t/{var_username}")

    #tumblr check 
    check_tumblr = f"https://www.tumblr.com/blog/view/{var_username}"
    tumblr_get = requests.get(check_tumblr)
    if tumblr_get.status_code == 404:
        print(f"[-]{Color.FAIL} TUMBLR NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}TUMBLR FOUND!{Color.END} https://www.tumblr.com/blog/view/{var_username}")
    
    #reddit check
    reddit_check = f"https://www.reddit.com/user/{var_username}"
    reddit_get = requests.get(reddit_check)
    if reddit_get.status_code == 404:
        print(f"[-]{Color.FAIL} REDDIT NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}REDDIT FOUND!{Color.END} https://www.reddit.com/user/{var_username}")

    #telegram_check
    telegram_check = f"https://t.me/{var_username}"
    telegram_get = requests.get(telegram_check)
    if telegram_get.status_code == 404:
        print(f"[-]{Color.FAIL} TELEGRAM NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}TELEGRAM FOUND!{Color.END} https://t.me/{var_username}")

    #twitter check 
    twitter_check = f"https://twitter.com/{var_username}"
    twitter_get = requests.get(twitter_check)
    if twitter_get.status_code == 404:
        print(f"[-]{Color.FAIL} TWITTER NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}TWITTER FOUND!{Color.END} https://twitter.com/{var_username}")

    #linkedin check
    linkedin_check = f"https://www.linkedin.com/in/{var_username}"
    linkedin_get = requests.get(linkedin_check)
    if linkedin_get.status_code == 404:
        print(f"[-]{Color.FAIL} LINKEDIN NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}LINKEDIN FOUND!{Color.END} https://www.linkedin.com/in/{var_username}")

    #pinterest check
    pin_check = f"https://br.pinterest.com/{var_username}"
    check_pin = requests.get(pin_check)
    if check_pin.status_code == 404:
        print(f"[-]{Color.FAIL} PINTEREST NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}PINTEREST FOUND!{Color.END} https://br.pinterest.com/{var_username}")

    #github check
    check_github = f"https://github.com/{var_username}"
    github_get = requests.get(check_github)
    if github_get.status_code == 404:
        print(f"[-]{Color.FAIL} GITHUB NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}GITHUB FOUND!{Color.END} https://github.com/{var_username}")

    #check vimeo 
    check_vimeo = f"https://vimeo.com/{var_username}"
    vimeo_get = requests.get(check_vimeo)
    if vimeo_get.status_code == 404:
        print(f"[-]{Color.FAIL} VIMEO NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}VIMEO FOUND!{Color.END} https://vimeo.com/{var_username}")

    #snapchat
    check_snap = f"https://www.snapchat.com/add/{var_username}"
    snap_get = requests.get(check_snap)
    if snap_get.status_code == 404:
        print(f"[-]{Color.FAIL} SNAPCHAT NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}SNAPCHAT FOUND!{Color.END} https://www.snapchat.com/add/{var_username}")

    #flickr check
    check_flickr = f"https://www.flickr.com/photos/{var_username}"
    flickr_get = requests.get(check_flickr)
    if flickr_get.status_code == 404:
        print(f"[-]{Color.FAIL} FLICKR NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}FLICKR FOUND!{Color.END} https://www.flickr.com/photos/{var_username}")
        
    #replit check
    check_replit = f"https://replit.com/@{var_username}"
    repl_get = requests.get(check_replit)
    if repl_get.status_code == 404:
        print(f"[-] {Color.FAIL}REPLIT NOT FOUND!{Color.END}")
    else:
        print(f"[-] {Color.OKGREEN}REPLIT FOUND!{Color.END} https://replit.com/@{var_username}")

    file = open (var_username + ".txt", "a")

    if youtube_get.status_code == 200:
        file.write ("https://www.youtube.com/c/" + var_username + "\n")

    if ig_get.status_code == 200:
        file.write ("https://www.instagram.com/" + var_username + "\n")

    if fb_get.status_code == 200:
        file.write ("https://www.facebook.com/" + var_username + "\n")

    if mess_get.status_code == 200:
        file.write ("https://www.messenger.com/t/" + var_username + "\n")

    if tumblr_get.status_code == 200:
        file.write ("https://www.tumblr.com/blog/view/" + var_username + "\n")

    if reddit_get.status_code == 200:
        file.write ("https://www.reddit.com/user/" + var_username + "\n")

    if telegram_get.status_code == 200:
        file.write ("https://t.me/" + var_username + "\n")

    if twitter_get.status_code == 200:
        file.write ("https://twitter.com/" + var_username + "\n")

    if linkedin_get.status_code == 200:
        file.write ("https://www.linkedin.com/in/" + var_username + "\n")

    if check_pin.status_code == 200:
        file.write ("https://br.pinterest.com/" + var_username + "\n")

    if github_get.status_code == 200:
        file.write ("https://github.com/" + var_username + "\n")

    if vimeo_get.status_code == 200:
        file.write ("https://vimeo.com/" + var_username + "\n")

    if snap_get.status_code == 200:
        file.write ("https://www.snapchat.com/add/" + var_username + "\n")

    if flickr_get.status_code == 200:
        file.write ("https://www.flickr.com/photos/" + var_username + "\n")

    if repl_get.status_code == 200:
        file.write ("https://replit.com/@" + var_username)

    file.close()

    def func_new_search():
        global new_search
        new_search = input ("\n[-] DO YOU WANT TO MAKE A NEW SEARCH? (Y/N) ")

        if new_search == "y" or new_search == "Y":
            main()
        elif new_search == "n" or new_search == "N":
            os.system("clear")
            exit()
        elif new_search == "":
            print (f"[-] {Color.FAIL}{Color.BD}INVALID OPTION!{Color.END}")
            time.sleep(3)
            func_new_search()
        else:
            print (f"[-] {Color.FAIL}{Color.BD}INVALID OPTION!{Color.END}")
            time.sleep(3)
            func_new_search()

    func_new_search()

main()