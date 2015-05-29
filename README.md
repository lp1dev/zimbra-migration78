# Zimbra Migration Tool

Unnoficial CLI Zimbra Migration Tool using Zimbra's SOAP API and zmprov

## What's in it ?

You can import accounts (without redirections for the moment, it's on the todolist !) , mailing-lists and aliases from a Zimbra 7-8 (maybe some others ?!) server to another one.

This migration tool is not working like the other ones you can find, it is using the SOAP API to get accounts, aliases and mailing-lists and zmprov to recreate them on your new server.

## How to install this ?

You must have a version of at least Python 3.3 and Pip with Virtualenv for easier installation.

To install using virtualenv and pip on an Unix-like system use (in the cloned path):

	source env/bin/activate
	pip install -r requirements.txt

Then a simple chmod +x on zimbra-migration.py should make

	./zimbra_migration.py import [accounts|mailing-lists|aliases]

work.

## How to configure it ?

Just fill the informations in the conf.py file

## What else ?

Nothing, have fun and please report the bugs you might encounter using this tool on github !

## Todo

- Migrate redirections when migrating Accounts
- Maybe sexier interface