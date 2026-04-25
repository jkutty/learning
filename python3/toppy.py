# "top" reimplementation in python
# Gareth Morgan

# get argparser to allow command line arguments
from argparse import ArgumentParser
# import subprocess to run commands to interact with the os
import subprocess

parser = ArgumentParser(description="Show process information based on PID or name")
parser.add_argument("-p", "--pid", help="PID of process to analyze")
parser.add_argument("-r", "--regex", help="Regular expression of process name to analyze")
args = parser.parse_args()
if args.regex:
    #regex_pids = subprocess.run(["pgrep", args.regex], capture_output=True)
    regex_pids = subprocess.run(["pgrep", args.regex], encoding="utf-8", stdout=subprocess.PIPE)
    #print(regex_pids.stdout)
    regex_pid_list = regex_pids.stdout.splitlines()
    for i in regex_pid_list:
        namep = subprocess.run(["ps", "-o", "comm=", "-p", i], encoding="utf-8", stdout=subprocess.PIPE)
        ownerp = subprocess.run(["ps", "-o", "user=", "-p", i], encoding="utf-8", stdout=subprocess.PIPE)
        name = namep.stdout.rstrip()
        owner = ownerp.stdout.rstrip()
        memp = subprocess.run(["pmap", i], encoding="utf-8", stdout=subprocess.PIPE)
        mem = memp.stdout.rstrip()
        mem = mem.rsplit(' ', 1)[1]
        mem = mem[:-1]
        cpup = subprocess.run(["ps", "-o", "pcpu=", "-p", i], encoding="utf-8", stdout=subprocess.PIPE)
        cpu = cpup.stdout.rstrip()
        print(f"Process details for {i}: Name({name}), Owner({owner}), Memory({mem})K, CPU({cpu})%")
        
else:
    pid = args.pid
    namep = subprocess.run(["ps", "-o", "comm=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
    ownerp = subprocess.run(["ps", "-o", "user=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
    name = namep.stdout.rstrip()
    owner = ownerp.stdout.rstrip()
    memp = subprocess.run(["pmap", pid], encoding="utf-8", stdout=subprocess.PIPE)
    mem = memp.stdout.rstrip()
    mem = mem.rsplit(' ', 1)[1]
    mem = mem[:-1]
    cpup = subprocess.run(["ps", "-o", "pcpu=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
    cpu = cpup.stdout.rstrip()
    print(f"Process details for {pid}: Name({name}), Owner({owner}), Memory({mem})K, CPU({cpu})%")


# the PID is now stored in pid


#def toppy_once(name, owner):
#    namep = subprocess.run(["ps", "-o", "comm=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
#    ownerp = subprocess.run(["ps", "-o", "user=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
#    name = namep.stdout.rstrip()
#    owner = ownerp.stdout.rstrip()
    # initialize the lists that will be used in the memory and cpu loops
#    memlist = []
#    cpulist = []


class Pidinfo:
    #def __init__(self, pid):
    #    self.pid = pid
    
    def toppy_test(self):
        return "test complete"

    # toppy_once is a function that is run only once
    # it collects the owner and name of the process and stores them as strings
    def toppy_once():
        namep = subprocess.run(["ps", "-o", "comm=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
        ownerp = subprocess.run(["ps", "-o", "user=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
        name = namep.stdout.rstrip()
        owner = ownerp.stdout.rstrip()
        # initialize the lists that will be used in the memory and cpu loops
        #memlist = []
        #cpulist = []
        print("toppy_once has run")

    # toppy_loop is a function that is run every 5 seconds
    # it collects memory (in K) and cpu (%) usage and stores them in lists
    def toppy_loop(self):
        memp = subprocess.run(["pmap", pid], encoding="utf-8", stdout=subprocess.PIPE)
        mem = memp.stdout.rstrip()
        mem = mem.rsplit(' ', 1)[1]
        mem = mem[:-1]
        memlist.append(int(mem))

        cpup = subprocess.run(["ps", "-o", "pcpu=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
        cpu = cpup.stdout.rstrip()
        cpulist.append(int(str.split(cpu)[-1]))
        return "toppy_loop has run"

    # toppy_out is a function that runs every 30 seconds
    # it calculates the average of memory and cpu usage and formats the output
    def toppy_out():
        for num in memlist:
            mnum = mnum +num
        memout = mnum / len(memlist)
        memlist = []

        for num in cpulist:
            csum = csum +num
        cpuout = csum / len(cpulist)
        cpulist = []

#print(f"Process details for {pid}: Name({name}), Owner({owner}), Memory({memout}), CPU({cpuout})")
