import subprocess

def callSubprocess():
    spReturn = subprocess.Popen(
            [
                'python', 
                'subprocess01.py',
                'Rodando'
            ],
                stdout = subprocess.PIPE,
                stderr = subprocess.STDOUT,
                shell = True
            )
    output, stderr = spReturn.communicate()
    print('output > %s' %output)
    print('stderr > %s' %stderr)
    
if __name__ == "__main__":
    callSubprocess()
