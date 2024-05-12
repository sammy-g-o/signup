"""This module allows a user to create an account and to login"""
class IncorrectPasswordLength(Exception):
    """raises exception if password length doesn't meet the required length"""
    pass

users = {
    "sammy": "@july18."
}

def signup(username, password):
    """
    stores users given username and password, also checks if a users data already exists

    Args:
        username (str): Accepts users username
        password (str): Accepts users password

    Raises:
        IncorrectPasswordLength: _description_
    """
    if username in users and users[username] == password:
        print("account already exists")
    elif len(password) < 8:
        raise IncorrectPasswordLength("password not up to 8 characters")
    else:
        users[username] = password
        print("account created")

def login(username, password):
    """checks if given username already exists and logs the user in

    Args:
        username (str): users username
        password (str): users password
    """
    if username in users and users[username] == password:
        print("login successful")
    else:
        print("invalid username or password")

