import subprocess
from file_writer import writeSpeedResult
from git_commit import upload
from twilio_alert import alert

fileLink = 'http://ipv4.download.thinkbroadband.com/10MB.zip'
fileSize = fileLink.split('/')[-1]
fileSize = int(fileSize[:fileSize.index('M')])
magicRatio = 1
warnLevel = 10
criticalLevel = 5

def getCurrentDownloadSpeed():
    result = subprocess.run(['bash', '-c', 'time wget ' + fileLink,
        '-U "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-GB; rv:1.9.0.1) Gecko/2008070206 Firefox/3.0.1"',
        '--no-check-certificate'], stderr=subprocess.PIPE)

    stderr = str(result.stderr.decode('utf-8'))
    outputGarbage = stderr.split(' ')[-1]
    splitGarbage = outputGarbage.split('\n')

    time = [i for i in splitGarbage if 'real' in i][0].split('\t')[1]

    seconds = parseTimeToSeconds(time)
    downloadSpeed = (fileSize/seconds)*8*magicRatio

    cleanup()
    writeSpeedResult(downloadSpeed)
    checkForAlert(downloadSpeed)

    return downloadSpeed

def checkForAlert(speed):
    if speed <= criticalLevel:
        return alert("Critical: download speed is at critical level. " + str(speed) + "Mb/s")
    if speed <= warnLevel:
        return alert("Warning: download speed is at warning level. " + str(speed) + "Mb/s")

# parses a time of the form MMmSS.SSSs
def parseTimeToSeconds(time):
    mi, rest = time.strip().split('m')
    return float(rest[:rest.index('s')]) + int(mi) * 60

def cleanup():
    filename = fileLink.split('/')[-1]
    subprocess.run(['rm', filename])

if __name__ == '__main__':
    print(getCurrentDownloadSpeed())
