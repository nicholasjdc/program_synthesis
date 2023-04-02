import subprocess
import os

def solveSyg(filename):
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = "./cvc4-1.8-x86_64-linux-opt --lang=sygus2 " + filename + " --sygus-inference"
    output = subprocess.getoutput(args)
    return output