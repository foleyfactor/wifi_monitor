import requests
from file_writer import writePingResult

testUrl = 'https://foleyfactor.github.io'

# Writes 1 if WiFi is up, otherwise 0
def checkWifiStatus():
    try:
        r = requests.get(testUrl)
    except requests.ConnectionError:
        writePingResult(0)
        return False
    writePingResult(1)
    return True

if __name__ == '__main__':
    checkWifiStatus()
