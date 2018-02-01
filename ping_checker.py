import requests
from file_writer import writePingResult
from twilio_alert import alert

testUrl = 'https://foleyfactor.github.io'
failValue = 0
successValue = 1

# Writes 1 if WiFi is up, otherwise 0
def checkWifiStatus():
    try:
        r = requests.get(testUrl)
    except:
        writePingResult(failValue)
        checkForAlert(failValue)
        return False
    writePingResult(successValue)
    checkForAlert(successValue)
    return True

def checkForAlert(val):
    if val == failValue:
        return alert("Critical: wifi is currently down.")

if __name__ == '__main__':
    checkWifiStatus()
