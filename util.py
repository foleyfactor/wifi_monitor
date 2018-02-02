import subprocess, os

user = None

def getUser():
    global user
    if user is None:
        d = dict(os.environ)
        user = d['USER']
    return user

if __name__ == "__main__":
    print(getUser())
