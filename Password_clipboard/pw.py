#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'linkedin':'your linkedin password','google':'your google account password','facebook':'your facebook password','twitter':'your twitter password'}


import sys, pyperclip
if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("password for " + account + " copied to clipboard.")
else:
    print("there is no account named " + account)