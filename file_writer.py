import json, time
from util import getUser

def writeSpeedResult(val):
    writeResult('speeds', val)

def writePingResult(val):
    writeResult('pings', val)

def writeResult(field, val):
    with open('/home/' + getUser() + '/wifi_monitor/output.json', 'r') as f:
        j = eval("".join(f.readlines()))
        j[field][int(time.time())] = val
    with open('/home/' + getUser() + '/wifi_monitor/output.json', 'w') as f:
        f.truncate()
        f.write(json.dumps(j))
