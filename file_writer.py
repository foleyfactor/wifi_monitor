import json, time
from util import getUser

def writeSpeedResult(val):
    writeResult('speeds', int(time.time()), val)

def writePingResult():
    writeResult('pings', 'most_recent', int(time.time()))

def writeDowntimeResult(start, end):
    writeResult('downtimes', start, end)

def writeResult(field, key, val):
    with open('/home/' + getUser() + '/wifi_monitor/output.json', 'r') as f:
        j = eval("".join(f.readlines()))
        if not field in j:
            j[field] = {}
        j[field][key] = val
    with open('/home/' + getUser() + '/wifi_monitor/output.json', 'w') as f:
        f.truncate()
        f.write(json.dumps(j))
