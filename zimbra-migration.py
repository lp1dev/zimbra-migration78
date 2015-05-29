#!./env/bin/python

import requests
import json
from sys import argv
from serv1 import server1
from serv2 import server2
from requests import session

def usage():
    return print("%s : import [accounts|mailing-lists|aliases]" %argv[0])

def importer(token):
    if argv[2] == "accounts":
        print("Importing accounts")
        success, value = server1.get_users(token)
        for user in value:
            server2.create_user(user['name'])
    elif argv[2] == "mailing-lists":
        print("Importing mailing-lists")
        success, value = server1.get_mailing_lists(token)
        for ml in value:
            server2.create_ml(ml, token)
            server2.add_users_to_ml(ml, token)
    elif argv[2] == "aliases":
        print("Importing aliases")
        success, value = server1.get_aliases(token)
        for alias in value:
            server2.create_alias(alias['name'], alias['targetName'])
    return True

def main():
    if len(argv) != 3:
        return usage()
    success, value = server1.login()
    if success is True:
        auth_token = json.loads(value)['Body']['AuthResponse']['authToken'][0]['_content']
    importer(auth_token)

if __name__ == "__main__":
    main()
