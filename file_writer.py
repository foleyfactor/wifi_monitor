import json, time

def writeSpeedResult(val):
    writeResult('speeds', val)

def writePingResult(val):
    writeResult('pings', val)

def writeResult(field, val):
    with open('output.json', 'r') as f:
        j = eval("".join(f.readlines()))
        j[field][int(time.time())] = val
    with open('output.json', 'w') as f:
        f.truncate()
        f.write(json.dumps(j))
