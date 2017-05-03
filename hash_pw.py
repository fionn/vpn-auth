#!/usr/bin/env python3

from sys import argv
import bcrypt

def hash(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def save_pw(client, pw):
    f = "/etc/openvpn/server/auth/" + client + ".password"
    g = open(f, "w")
    g.write(pw + "\n")
    g.close()
    print("Password saved to", f)
    return 0

if __name__ == "__main__":
    pw = input("Enter password: ")
    hashed_pw = hash(bytes(pw, "utf8"))
    print(hashed_pw.decode())

    if len(argv) == 2:
        save_pw(argv[1], hashed_pw.decode())

