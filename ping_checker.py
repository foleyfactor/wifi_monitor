import requests, time
from file_writer import writePingResult, writeDowntimeResult
from twilio_alert import alert
from git_commit import upload

testUrl = 'https://foleyfactor.github.io'
failValue = 0
successValue = 1

# Writes 1 if WiFi is up, otherwise 0
def checkWifiStatus():
    try:
        r = requests.get(testUrl)
    except:
        return checkUntilDowntimeEnd(int(time.time()))
    writePingResult()

def checkUntilDowntimeEnd(start_time):
    try:
        r = requests.get(testUrl)
    except:
        time.sleep(60)
        return checkUntilDowntimeEnd(start_time)
    writeDowntimeResult(start_time, int(time.time()))
    sendDowntimeAlert()
    writePingResult()

def sendDowntimeAlert():
    return alert("Critical: wifi was just down. System is now up.\nSee details at: foleyfactor.github.io/wifi_monitor.")

if __name__ == '__main__':
    checkWifiStatus()
