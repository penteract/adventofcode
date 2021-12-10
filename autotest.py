#! /usr/bin/env python3
usage = """
Python script for advent of code which downloads the problem description,
attempts to extract sample input and corresponding output,
then runs sol.py on the sample input whenever sol.py is modified until
sol.py gives the sample output. When it does, sol.py gets run on the real input
and if that succeeds, the last printed word gets submitted automatically.

call as `autotest.py {year} {day}` with the
environment variable $AOCSession set to the value of your session cookie

files used:
sol.py      This program assumes that your solution for the part you are
            currently working on is in this file.
            Run as `python3 sol.py {input}` where {input} is the name of
            a file from which sol.py is expected to read the input
            for the day's problem
            
input       Your personal input (https://adventofcode.com/{year}/day/{day}/input)
input1      the automatically extracted sample input
            By default this is the first non-inline code block.
            It may be wrong, and if so you must manually edit it and restart this
            program if you want it to work correctly.
            If no appropriate sample input is found, you must create this file
            to use this program.
            
output1     the automatically extracted sample output for part 1
            By default, this is the last highlighed thing at the end of a code tag.
            It may be wrong, and if so you must manually edit it and restart this
            program if you want it to work correctly.
            If no appropriate sample output is found, you must create this file
            to use this program.
            
output2     the automatically extracted sample output for part 2
1page.html  the page when solving part 1
2page.html  the page when solving part 2
badAns      a text file containing a list of answers which have been rejected
            Hopefully avoids repeatedly submitting wrong answers
            Does not distinguish between part 1 and part 2
            
tmp         stores the output of sol.py on sample input
            Can be deleted without consequence except while sol.py is running
            
tmpreal     stores the output of sol.py on the real input
            Can be deleted without consequence except while sol.py is running
"""

import sys
import os
import subprocess
from datetime import datetime

import urllib.request as r

sesh = os.environ["AOCSession"]

headers={"Cookie":"session="+sesh}

def writeTo(file,content):
    with open(file,mode="w") as f:
        f.write(content)

def readString(file):
    with open(file) as f:
        return "".join(f)

def get_or_save(url,file):
    if file is None or not os.path.isfile(file):
        print("requesting url",repr(url))
        r1=r.urlopen(r.Request(url,headers=headers))
        s = "".join(l.decode() for l in r1)
        if file is not None:
            writeTo(file,s)
    else:
        s=readString(file)
    return s

def tee_with_exitcode(command,file):
    #print (f"(exit `(({command} 2>&1 ; echo $? >&3) | tee ${file} >&4) 3>&1` ) 4>&1")
    return subprocess.run(f"(exit `(({command} 2>&1 ; echo $? >&3) | tee {file} >&4) 3>&1` ) 4>&1", shell=True)

def submit(part,answer):
    global submittime
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    print(f"submitting",repr(answer),"to url",repr(url))
    resp = r.urlopen(r.Request(url,data=bytes(f"level={part}&answer={answer}","utf8"),headers=headers))
    submittime=datetime.now()
    print("time",submittime)
    print("response:")
    prnt=False
    content = ""
    correct=False
    for line in resp:
        line = line.decode()
        if "<article>" in line:
            prnt=True
        if prnt:
            print(line,end="")
            content+=line
        if "</article>" in line:
            prnt=False
    return resp,content

for arg in sys.argv[1:]:
    if "help" in arg or "-h" in arg:
        print(usage)
        exit(0)
if len(sys.argv)<3:
    raise Exception("not given year and day")
year=sys.argv[1]
day=sys.argv[2]
dayurl = f"https://adventofcode.com/{year}/day/{day}"

print("PRIVATE INPUT:")
print(get_or_save(dayurl + "/input", "input"))

bad_answers=set()
if os.path.isfile("wrongAnswers"):
    with open("wrongAnswers") as f:
        for line in f:
            bad_answers.add(line.strip())

def addBad(ans):
    bad_answers.add(ans)
    with open("wrongAnswers",mode="a") as f:
        print(ans,file=f)

def doPart(part=None):
    if part is None:
        s = get_or_save(dayurl, None)
        completed=s.count("Your puzzle answer was")
        if completed > 1:
            raise Exception("You've already done enough parts")
        part=str(completed+1)
        writeTo(part+"page.html",s)
    else:
        part=str(part)
    
    if not os.path.isfile("input1"):
        print("Trying to find sample input to save in ","input1")
        s=get_or_save(dayurl, part+"page.html")
        
        start=s.find("<pre><code>")
        end=s.find("</code></pre>")
        assert start!=-1 # can't find pre block
        assert end!=-1 # can't find end of pre block !!!

        eg = s[start+len("<pre><code>"):end].replace("<em>","").replace("</em>","")
        writeTo("input1",eg)
        print("sample input:")
        print(eg)
    outputfile = "output"+part
    if not os.path.isfile(outputfile):
        print("Trying to find sample output to save in ",outputfile)
        s=get_or_save(dayurl, str(part)+"page.html")
        completed=s.count("Your puzzle answer was")
        if str(completed+1)!=part:
            raise Exception(f"the given part ({part}) cannot be done when {completed} are completed")
        last = s.rfind("</em></code>")
        assert last!=-1 #can't find sample output
        start = s.rfind("<em>",0,last)+len("<em>")
        assert start >= len("<em>") # can't find start of sample output !!!
        if part=="2" and start<=s.find("--- Part Two ---"):
            raise Exception("Can't find part 2 sample output")
        sampleout = s[start:last]
        writeTo(outputfile,sampleout)
    else:
        sampleout=readString(outputfile).strip()
    print("assumed output:",sampleout)
    print("""    suggested code for sol.py:
import sys
fname=sys.argv[1] if len(sys.argv)>1 else "input"
f=list(open(fname))
    """)
    ns=0
    while True:
        while ns == (ns := os.stat("sol.py").st_mtime_ns):
            if os.system("inotifywait -q sol.py"):
                raise Exception("inotifywait did not terminate cleanly")
        ns=os.stat("sol.py").st_mtime_ns
        
        print("==== trying sample input (10 second timeout)")
        p=tee_with_exitcode("timeout 10 python3 sol.py input1 2>&1", "tmp")
        #subprocess.run("(exit `((timeout 10 python3 sol.py input1 2>&1 ; echo $? >&3) | tee tmp >&4) 3>&1) 4>&1", shell=True)
        answers = readString("tmp").split()
        if p.returncode==0 and len(answers)>=1 and answers[-1]==sampleout:
            print("==== trying real input (no timeout)")
            #p=subprocess.run("python3 sol.py input | tee tmpreal", shell=True)
            p=tee_with_exitcode("python3 sol.py input","tmpreal")
            print("==== end of program output")
            if p.returncode:
                print("error when called on real input")
                continue
            answer = readString("tmpreal").split()
            if len(answer)<1:
                print("answer is empty when called on real input")
                continue
            answer=answer[-1]
            #do some checks on answer
            if(len(answer)<=2):
                print(repr(answer),"looks too small. Not submitting")
            elif answer==sampleout:
                print(repr(answer), "is the same as the example output. Not submitting")
            elif answer in bad_answers:
                print(repr(answer), "previously submitted and failed. Not submitting")
            else:
                if not bad_answers or input("Do you want to submit "+repr(answer)+" (y/n)?")=="y":
                    print("submitting answer:",repr(answer))
                    resp,content = submit(part=part,answer=answer)
                    if "That's the right answer!" in content:
                        succeeded=True
                        break
                    elif "That's not the right answer" in content:
                        addBad(answer)
                    else:
                        print("did not recognise success or incorrect, may be timeout or blank input or already completed")
        else:
            print("==== did not get output matching",sampleout)
    return part

if len(sys.argv)<4:
    if doPart() == "1":
        doPart("2")
    
