import subprocess, os

user = None

def getUser():
    global user
    if user is None:
        with open('/home/.user', 'r') as f:
            user = f.readline().strip()
    return user

if __name__ == "__main__":
    print(getUser())
