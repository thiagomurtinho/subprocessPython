import sys

def runSubprocess(argv):
    try:
        sys.stdout(1)
    except Exception as e:
        print('error: %s'%e)
        return(123)

if __name__ == "__main__":
    rrunSubprocess(sys.argv)
