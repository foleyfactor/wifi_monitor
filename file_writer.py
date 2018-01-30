import json, time

def writeOut(val):
    with open('output.json', 'r') as f:
        j = eval("".join(f.readlines()))
        j['speeds'][int(time.time())] = val
    with open('output.json', 'w') as f:
        f.truncate()
        f.write(json.dumps(j))
