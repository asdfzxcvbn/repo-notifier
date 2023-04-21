#!/usr/bin/python3
# crap code that took me forever to implement, but it WORKS!
from requests import get, post
from sys import exit as sysexit
from time import sleep
from urllib.parse import quote_plus

# change the 4 vars below
BOT_TOKEN = ""
CHAT_ID = ""
REPO_LINK = ""
REPO_NAME = ""


# this function will fetch the current repo data and return it, meaning you have to save it to a variable.
def get_new_repo_data();
    try:
        CURRENT_DATA = get(REPO_LINK).json()["apps"]
        CURRENT = [app["name"] for app in CURRENT_DATA]
        sleep(5)  # idk why i did this but u can remove it if u want lol
        return CURRENT
    except (KeyError, IndexError):
        print("there currently seems to be an issue with the repository.")
        sysexit(1)


CURRENT = get_new_repo_data()  # get repo data and save it to `CURRENT` so you can check for updates.


def send_update_message(app):
    global BOT_TOKEN, CHAT_ID
    text = quote_plus(f"{app} has been added to the {REPO_NAME}!")  # quote_plus is used to url encode the text so you can send it as a POST request.
    post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}")


while 1:
    try:
        REPO_DATA = get(REPO_LINK).json()["apps"]
    except (KeyError, IndexError):
        print("there currently seems to be an issue with the repository.")
        sysexit(1)

    x = [app['name'] for app in REPO_DATA]

    print(x == CURRENT)  # will print True or False, you can remove this if you want.

    if x != CURRENT:
        # list comprehension, saves a list of every app in the recently fetched repo data IF the app isnt in the data fetched 2 minutes earlier.
        new_apps = [app for app in x if app not in CURRENT] 
        for app in new_apps:
            send_update_message(app)
            sleep(5)
        CURRENT = get_new_repo_data()  # set CURRENT again.
        print(f"rechecking in 2 minutes, sent new app message for the following apps: {new_apps}")
    else:
        print("no new apps, rechecking in 2 minutes")
    sleep(120)
