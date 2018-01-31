from download_checker import getCurrentDownloadSpeed
from ping_checker import checkWifiStatus
from git_commit import upload
from time import sleep
from datetime import datetime

def main():
    count = 0
    while datetime.now() < datetime(2018, 2, 1):
        if count == 0:
            currSpeed = getCurrentDownloadSpeed()
            print("Current download speed is: " + str(currSpeed) + "!")
        res = checkWifiStatus()
        print("Hooray! The Wifi is up!" if res else "Boo! Hiss! No Wifi. :(")
        upload()
        sleep(300)
        count = (count + 1) % 12

if __name__ == '__main__':
    main()
