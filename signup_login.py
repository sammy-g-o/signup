class IncorrectPasswordLength(Exception):
    pass

users = {
    "sammy": "@july18."
}

def signup(username, password):
    if username in users and users[username] == password:
        print("account already exists")
    elif len(password) < 8:
        raise IncorrectPasswordLength("password not up to 8 characters")
    else:
        users[username] = password
        print("account created")

def login(username, password):
    if username in users and users[username] == password:
        print("login successful")
    else:
        print("invalid username or password")

