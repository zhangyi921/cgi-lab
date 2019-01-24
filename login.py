#!/usr/bin/env python3
import cgi
import cgitb
import os
import json
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
cgitb.enable()

print("Content-Type: text/html")
# print()
# print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
# print(os.environ)

# print(login_page())

c_password = ""
c_username = ""
try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(";")
    for pair in cookie_pairs:
        key, val = pari.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_password = val
    print(cookie_string)
except:
    pass

if c_username and c_password:
    print("\n\n")
    print(secret_page(c_username, c_password))

elif os.environ.get("REQUEST_METHOD", "GET") == "POST":
    form = cgi.FieldStorage()
    p_user = form.getvalue("username")
    p_password = form.getvalue("password")
    if p_user == username and p_password == password:
        print("Set-Cookie: username={};".format(p_user))
        print("Set-Cookie: password={};".format(p_password))
        print(secret_page(username, password))
    else:
        print(after_login_incorrect())
else:
    print(login_page())