import subprocess

def upload():
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', '"Another speed test"'])
    subprocess.run(['git', 'push'])
