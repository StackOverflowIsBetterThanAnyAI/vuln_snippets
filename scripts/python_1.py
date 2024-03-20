import subprocess


def echoHello():
    try:
        cmd = "echo Hello from subprocess module, using echo!"
        subprocess.run(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error {e} occured")
    
if __name__ == '__main__':
    echoHello()