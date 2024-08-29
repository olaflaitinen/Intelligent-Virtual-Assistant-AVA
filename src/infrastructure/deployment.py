import os

def deploy():
    os.system('docker build -t ava .')
    os.system('docker run -d -p 5000:5000 ava')

if __name__ == "__main__":
    deploy()
