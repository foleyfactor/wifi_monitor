import subprocess, os

user = None
pings = None
download = None

def getUser():
    global user
    if user is None:
        with open('/home/.user', 'r') as f:
            user = f.readline().strip()
    return user

def getPingInterval():
    if pings is None:
        loadAllIntervals()
    return pings

def getDownloadInterval():
    if downloads is None:
        loadAllIntervals()
    return downloads

def loadAllIntervals():
    global pings, downloads
    with open('/home/' + getUser() + '/wifi_monitor/interval.json') as f:
        d = eval(''.join([i.strip() for i in f.readlines()]))
        pings = d['pings']
        download = d['downloads']

if __name__ == "__main__":
    print(getUser())
