import subprocess

def upload():
    try:
        subprocess.run(['cd', '~/wifi_monitor'])
        subprocess.run(['git', 'add', 'output.json'], stdout=subprocess.DEVNULL)
        subprocess.run(['git', 'commit', '-m', '"Another speed test"'], stdout=subprocess.DEVNULL)
        subprocess.run(['git', 'push', 'origin', 'master'], stdout=subprocess.DEVNULL)
    except:
        # oh well, we can try again next time
        pass
