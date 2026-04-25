# "top" reimplementation in python
# Gareth Morgan

# get argparser to allow command line arguments
from argparse import ArgumentParser
# import subprocess to run commands to interact with the os
import subprocess
# import time for timing to work
import time

# setup parser with 2 arguments (either pid or regex)
parser = ArgumentParser(description="Show process information based on PID or name")
parser.add_argument("-p", "--pid", help="PID of process to analyze")
parser.add_argument("-r", "--regex", help="Regular expression of process name to analyze")
args = parser.parse_args()

# first part of the script handles regex input with an if statement
if args.regex:
    regex_pids = subprocess.run(["pgrep", args.regex], encoding="utf-8", stdout=subprocess.PIPE)
    regex_pid_list = regex_pids.stdout.splitlines()
    # setup the counter and the dictionaries
    shortcount = 0
    namedict = {}
    ownerdict = {}
    memdict = {}
    cpudict = {}
    outputdict = {}
    print("Gathering data to calculate average values")
    # populating the dictionaries with values that are gathered via subprocesses
    for i in regex_pid_list:
        namep = subprocess.run(["ps", "-o", "comm=", "-p", i], encoding="utf-8", stdout=subprocess.PIPE)
        namedict.update({ i : namep.stdout.rstrip() })
        ownerp = subprocess.run(["ps", "-o", "user=", "-p", i], encoding="utf-8", stdout=subprocess.PIPE)
        ownerdict.update({ i : ownerp.stdout.rstrip() })
        memdict = { i : [] for i in regex_pid_list}
        cpudict = { i : [] for i in regex_pid_list}
        # combining the dictionaries to make it easier to format the output
        dictlist = [ namedict, ownerdict, memdict, cpudict ]
        outputdict = {}
        for k in namedict.keys():
            outputdict[k] = tuple(outputdict[k] for outputdict in dictlist)
    # this while loop will go forever, and prints to stdout when the shortcount counter reaches 7, which should take about 30 seconds
    while True == True:
        # this while loop samples the memory and cpu use about every 4 seconds and adds the value to a list inside a dictionary
        while shortcount < 8:
            for key in memdict.keys():
                memp = subprocess.run(["pmap", key], encoding="utf-8", stdout=subprocess.PIPE)
                mem = memp.stdout.rstrip()
                mem = mem.rsplit(' ', 1)[1]
                mem = mem[:-1]
                memdict[key].append(int(mem))
            for key in cpudict.keys():
                cpup = subprocess.run(["ps", "-o", "pcpu=", "-p", key], encoding="utf-8", stdout=subprocess.PIPE)
                cpu = cpup.stdout.rstrip()
                cpudict[key].append(float(str.split(cpu)[-1]))
            # printing the shortcount counter to makes sure the loop is iterating correctly
            #print(shortcount)
            shortcount += 1
            time.sleep(4)
        for key,list in outputdict.items():
            outname = list[0]
            outowner = list[1]
            outmem = sum(list[2]) / shortcount
            outcpu = sum(list[3]) / shortcount
            print(f"Process details for {key}: Name({outname}), Owner({outowner}), Memory({outmem}K), CPU({outcpu}%)")
        # clearing the counter and the lists that contain memory and cpu values
        shortcount = 0
        for key in memdict.keys():
            memdict = { key : [] }
        for key in cpudict.keys():
            cpudict = { key : [] }
        print("----------------------------------------------------------------------------------------------")

# the else statement handles the simpler process for the PID flag
else:
    pid = args.pid
    namep = subprocess.run(["ps", "-o", "comm=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
    ownerp = subprocess.run(["ps", "-o", "user=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
    name = namep.stdout.rstrip()
    owner = ownerp.stdout.rstrip()
    shortcount = 0
    memlist = []
    cpulist = []
    memsum = 0
    cpusum = 0
    print("Gathering data to calculate average values")
    while True == True:
        while shortcount < 8:
            memp = subprocess.run(["pmap", pid], encoding="utf-8", stdout=subprocess.PIPE)
            mem = memp.stdout.rstrip()
            mem = mem.rsplit(' ', 1)[1]
            mem = mem[:-1]
            memlist.append(int(mem))
            cpup = subprocess.run(["ps", "-o", "pcpu=", "-p", pid], encoding="utf-8", stdout=subprocess.PIPE)
            cpu = cpup.stdout.rstrip()
            cpulist.append(float(str.split(cpu)[-1]))
            #print(shortcount)
            shortcount += 1
            time.sleep(4)
        for num in memlist:
            memsum = memsum +num
        memout = memsum / len(memlist)
        memlist = []
        for num in cpulist:
            cpusum = cpusum +num
        cpuout = cpusum / len(cpulist)
        cpulist = []
        shortcount = 0
        print(f"Process details for {pid}: Name({name}), Owner({owner}), Memory({memout}K), CPU({cpuout}%)")
        print("----------------------------------------------------------------------------------------------")



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
