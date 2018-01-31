import subprocess

def upload():
    subprocess.run(['git', 'add', 'output.json'], stdout=subprocess.DEVNULL)
    subprocess.run(['git', 'commit', '-m', '"Another speed test"'], stdout=subprocess.DEVNULL)
    subprocess.run(['git', 'push'], stdout=subprocess.DEVNULL)
