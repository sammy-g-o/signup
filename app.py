from signup_login import IncorrectPasswordLength, signup, login, users

print("welcome\nto sign up, type sign up\nto login type login")

decision = input()

if decision == "sign up":
    try:
        signup(username=input("enter username:\n"),password=input("enter password:\n"))
    except IncorrectPasswordLength as error:
        print(error)
    else:
        print("do you want to login?\nenter login or q to quit")
        decision = input()
        if decision == "login":
            login(username=input("enter username:\n"),password=input("enter password:\n"))
        elif decision == "q":
            pass
elif decision == "login":
    login(username=input("enter username:\n"),password=input("enter password:\n"))
