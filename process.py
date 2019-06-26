import subprocess

def callSubprocess():
    spReturn = subprocess.Popen(
            [
                'python', 
                'subprocess01.py',
                'Rodando'
            ],
                shell=True
            )

if __name__ == "__main__":
    callSubprocess()
