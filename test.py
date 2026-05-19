# IAM Authentication system
# login system with 3 attemps lockout
# audit log with timestamps
# persistent lockout accounts file
# reading and checking locked accounts


from datetime import datetime

LOCKED_FILE = "/home/jerram/locked_accounts.txt"
AUDIT_FILE = "/home/jerram/audit_log.txt"


users = {
        "richard": "test123",
        "alice": "test234",
        "bob": "test123"
        }

def log_action(username, action):
    now = datetime.now()
    with open("AUDIT_FILE", "a") as f:
        f.write(f"{now} | {username} | {action}\n")
        
def is_locked(username):
    try:
        with open("LOCKED_FILE", "r") as f:
            locked = f.read().splitlines()
        return username in locked
    except FileNotFoundError:
        return False
            
def lock_account(username):
    with open("LOCKED_FILE", "a") as f:
        f.write(username + "\n")                    
            
attempts = 0

username = input("Enter username:")

if is_locked(username):
    print("this account is permanently locked. Contact your administraor.")
    log_action(username, "Attempted login on locked account")
else:
    while attempts <3:
        password = input("Enter password:")
        
        if username in users:
           if users[username] == password:
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
        