import subprocess
import os

FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
filename = "my_file.dat"
args = "./cvc4-1.8-x86_64-linux-opt --lang=sygus2 max.sygus --sygus-inference"
output = subprocess.getoutput(args)
print(output)