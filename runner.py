from download_checker import getCurrentDownloadSpeed
from time import sleep
from datetime import datetime

def main():
    while datetime.now() < datetime(2018, 1, 30, 18, 27):
        currSpeed = getCurrentDownloadSpeed()
        print("Current download speed is: " + str(currSpeed) + "! Going to sleep...")
        sleep(3600)

if __name__ == '__main__':
    main()
