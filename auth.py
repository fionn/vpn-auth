#!/usr/bin/env python3

import sys
import os.path
import bcrypt

def realuser(username):
    f = "/etc/openvpn/server/auth/" + username + ".password"
    if os.path.isfile(f):
        return True
    return False

def parseword(tempfile):
    userpass = open(tempfile, "r").read().splitlines()
    if len(userpass) == 2:
        return userpass
    else:
        print("Malformed credentials")
        sys.exit(1)

def verify(username, pw_submitted):
    try:
        f = "/etc/openvpn/server/auth/" + username + ".password"
        pw_stored = open(f, "r").read().strip()
        pw_stored = bytes(pw_stored, "utf8")
        pw_submitted = bytes(pw_submitted, "utf8")
        if bcrypt.checkpw(pw_submitted, pw_stored):
            return True
        else:
            return False
    except Exception:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " tempfile")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("No credentials supplied")
        sys.exit(1)

    up = parseword(sys.argv[1])
    username = up[0]
    pw_submitted = up[1]

    if realuser(username):
        print("Authenticating for user", username)
        if verify(username, pw_submitted):
            print("Authenticated")
            sys.exit(0)
        else:
            print("Incorect password for user", username)
            sys.exit(1)
    else:
        print("Username", username, "does not exist")
        sys.exit(1)

    sys.exit(1)


