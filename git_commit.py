import subprocess, os
from util import getUser

def upload():
    try:
        os.chdir('/home/' + getUser() + '/wifi_monitor')
        subprocess.run(['git', 'add', 'output.json'], stdout=subprocess.DEVNULL)
        subprocess.run(['git', 'commit', '-m', '"Another speed test"'], stdout=subprocess.DEVNULL)
        subprocess.run(['git', 'push', 'origin', 'master'], stdout=subprocess.DEVNULL)
    except Exception as e:
        # oh well, we can try again next time
        pass
