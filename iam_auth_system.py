# IAM Authentication system
# login system with 3 attemps lockout
# audit log with timestamps
# persistent lockout accounts file
# reading and checking locked accounts
# SHA256 hashed passwords


import json 
import os
import hashlib
from datetime import datetime
from getpass import getpass


USERS_FILE =os.path.join(os.path.dirname(__file__), "users.json")
LOCKED_FILE = os.path.join(os.path.dirname(__file__), "locked_accounts.txt")
AUDIT_FILE = os.path.join(os.path.dirname(__file__), "audit_log.txt")



def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("users.json not found.")
        return {}   
def save_users(users):
        with open(USERS_FILE, "w") as f:
             json.dump(users, f)

def log_action(username, action):
    now = datetime.now()
    with open(AUDIT_FILE, "a") as f:
        f.write(f"{now} | {username} | {action}\n")
        
def is_locked(username):
    try:
        with open(LOCKED_FILE, "r") as f:
            locked = f.read().splitlines()
        return username in locked
    except FileNotFoundError:
        return False
            
def lock_account(username):
    with open(LOCKED_FILE, "a") as f:
        f.write(username + "\n")                    

users = load_users()            

attempts = 0

username = input("Enter username:")

if is_locked(username):
    print("this account is permanently locked. Contact your administraor.")
    log_action(username, "Attempted login on locked account")
else:
    while attempts <3:
        password = getpass("Enter password:")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in users:
           if users[username] == hashed_password:
               print("Access granted. Welcome" + username)
               log_action(username, "Successful login")
               break
           else:
               print("Wrong password.")
               log_action(username, "Failed login attempt")
               attempts = attempts + 1
        else:
          print("username not recognised.")
          log_action(username, "unkown username attemped")
          attempts = attempts +1
            
    if attempts ==3:
        print("Account Locked. Too many failed attemps.")
        lock_account(username)
        log_action(username, "account permanently locked")
        