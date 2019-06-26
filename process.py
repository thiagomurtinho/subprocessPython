import subprocess

def callSubprocess():
    spReturn = subprocess.Popen(
            [
                'python', 
                'subprocess01.py',
                'Rodando'
            ],
                stdout = subprocess.PIPE,
                shell = True
            )
    print(spReturn.communicate())
    
if __name__ == "__main__":
    callSubprocess()
