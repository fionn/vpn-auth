Check VPN credentials
=====================

OpenVPN outsources username/password credential checking via the `auth-user-pass-verify` option. This program uses bcrypt to check passwords in a secure way.

Usage
-----
Install [bcrypt](https://github.com/pyca/bcrypt) (on Arch this is `python-bcrypt`, *not* `python-py-bcrypt`), put `auth.py` in `/etc/openvpn/server/auth/` and

    auth-user-pass-verify /etc/openvpn/server/auth/auth.py via-file
    
in `server.conf`.

The bcrypt-hashed passwords are stored in `auth/username.password`, where `username` is the username and `password` is literally the word password. 

To generate the hash, use `hash_pw.py`. `hash_pw.py username` will write this hash to `auth/username.password`.

Generating Configurations
-------------------------
Run `gen_config.sh` to go through the motions of setting up a new user and making a configuration file for them.

It depends on [easy-rsa](https://github.com/OpenVPN/easy-rsa) and the CA installed on the same machine as the OpenVPN server, as well as a `client_template.conf` file in `/etc/openvpn/`. In the end, it'll produce all the credentials, save the hashed password and generate an `.ovpn` file.

Caveats
-------
The whole point of this is to protect all the passwords from an attacker. However, the list of users is obviously unprotected.

It also prints some output, which should be disabled if running a minimal logging policy.

