#!/usr/bin/python3
# crap code that took me forever to implement, but it WORKS!
from requests import get, post
from sys import exit as sysexit
from time import sleep
from urllib.parse import quote_plus


BOT_TOKEN = ""
CHAT_ID = ""
REPO_LINK = ""
REPO_NAME = ""


def get_new_repo_data();
    try:
        CURRENT_DATA = get(REPO_LINK).json()["apps"]
        CURRENT = [app["name"] for app in CURRENT_DATA]
        sleep(5)
        return CURRENT
    except (KeyError, IndexError):
        print("there currently seems to be an issue with the repository.")
        sysexit(1)


CURRENT = get_new_repo_data()


def send_update_message(app):
    global BOT_TOKEN, CHAT_ID
    text = quote_plus(f"{app} has been added to the {REPO_NAME}!")
    post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}")


while 1:
    try:
        REPO_DATA = get(REPO_LINK).json()["apps"]
    except (KeyError, IndexError):
        print("there currently seems to be an issue with the repository.")
        sysexit(1)

    x = [app['name'] for app in REPO_DATA]

    print(x == CURRENT)

    if x != CURRENT:
        new_apps = [app for app in x if app not in CURRENT]
        for app in new_apps:
            send_update_message(app)
            sleep(5)
        CURRENT = get_new_repo_data()
        print(f"rechecking in 2 minutes, sent new app message for the following apps: {new_apps}")
    else:
        print("no new apps, rechecking in 2 minutes")
    sleep(120)
