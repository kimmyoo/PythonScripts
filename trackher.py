#!/usr/local/bin/python3
# trackher.py - tracks instagram user's profile page by providing user name
import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    username = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.instagram.com/' + username)
else:
    print("please provide me with a username")
