from download_checker import getCurrentDownloadSpeed
from ping_checker import checkWifiStatus
from git_commit import upload, pull
from time import sleep
from datetime import datetime
from util import getPingInterval, getDownloadInterval

def main():
    lastRunDownload = time.time() - 10000
    lastRunPing = time.time() - 10000
    pingInterval = getPingInterval() * 1000
    downloadInterval = getDownloadInterval() * 1000
    while True:
        pull()

        needUpload = False
        if time.time() - lastRunDownload >= runInterval:
            print("Performing Download Test")
            currSpeed = getCurrentDownloadSpeed()
            needUpload = True
        if time.time() - lastRunDownload >= pingInterval:
            print("Performing Connection Test")
            res = checkWifiStatus()
            needUpload = True
        if needUpload: upload()

        sleep(30)

if __name__ == '__main__':
    main()
