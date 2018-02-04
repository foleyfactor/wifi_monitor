from download_checker import getCurrentDownloadSpeed
from ping_checker import checkWifiStatus
from git_commit import upload, pull
from time import sleep, time
from datetime import datetime
from util import getPingInterval, getDownloadInterval

def main():
    lastRunDownload = time() - 10000
    lastRunPing = time() - 10000
    pingInterval = getPingInterval()
    downloadInterval = getDownloadInterval()
    while True:
        pull()

        needUpload = False
        if time() - lastRunDownload >= downloadInterval:
            print("Performing Download Test")
            currSpeed = getCurrentDownloadSpeed()
            needUpload = True
            lastRunDownload = time()
        if time() - lastRunPing >= pingInterval:
            print("Performing Connection Test")
            res = checkWifiStatus()
            needUpload = True
            lastRunPing = time()
        if needUpload: upload()

        sleep(30)

if __name__ == '__main__':
    main()
