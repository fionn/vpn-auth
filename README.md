Check VPN credentials
=====================
OpenVPN outsources username/password credential checking via the `auth-user-pass-verify` option. This program uses bcrypt to check passwords in a secure way.

Usage
-----
Install [bcrypt](https://github.com/pyca/bcrypt) (on Arch this is `python-bcrypt`, *not* `python-py-bcrypt`), put `auth.py` in `/etc/openvpn/server/auth/` and

    auth-user-pass-verify /etc/openvpn/server/auth/auth.py via-file
    
in `server.config`.

The bcrypt-hashed passwords are stored in `auth/username.password`, where `username` is the username and `password` is literally the word password. 

To generate the hash, use `hash.py`.

Shortcomings
------------
The `username.password` file has to be created by hand and the hash copied into it. It might be nice if `hash.py` did everything.

Caveats
-------
The whole point of this is to protect all the passwords from an attacker. However, the list of users is obviously unprotected.

It also prints some output, which shoud be disabled if running a minimal logging policy.

