#!/usr/bin/env python3

import bcrypt

def hash(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

if __name__ == "__main__":
    pw = input("Enter password: ")
    hashed_pw = hash(bytes(pw, "utf8"))
    print(hashed_pw.decode())

