#! /usr/bin/env python3
import sys
import os
import subprocess
from datetime import datetime

import urllib.request as r

sesh = os.environ["AOCSession"]

print(sesh)

headers={"Cookie":"session="+sesh}

def writeTo(file,content):
    with open(file,mode="w") as f:
        f.write(content)

def get_or_save(url,file):
    if file is None or not os.path.isfile(file):
        print("requesting url",repr(url))
        r1=r.urlopen(r.Request(url,headers=headers))
        s = "".join(l.decode() for l in r1)
        if file is not None:
            writeTo(file,s)
    else:
        s="".join(open(file))
    return s

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
    
if len(sys.argv)<3:
    raise Exception("not given day and year")
year=sys.argv[1]
day=sys.argv[2]
dayurl = f"https://adventofcode.com/{year}/day/{day}"

get_or_save(dayurl + "/input", "input")

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
        s=get_or_save(dayurl, part+"page.html")
        
        start=s.find("<pre><code>")
        end=s.find("</code></pre>")
        assert start!=-1 # can't find pre block
        assert end!=-1 # can't find end of pre block !!!

        eg = s[start+len("<pre><code>"):end].replace("<em>","").replace("</em>","")
        writeTo("input1",eg)
        print("assumed input:")
        print(eg)
    if not os.path.isfile("output"+part):
        s=get_or_save(dayurl, str(part)+"page.html")
        completed=s.count("Your puzzle answer was")
        if str(completed+1)!=part:
            raise Exception(f"the given part ({part}) cannot be done when {completed} are completed")
        last = s.rfind("</em></code>")
        assert last!=-1 #can't find output1
        start = s.rfind("<em>",0,last)+len("<em>")
        assert start >= len("<em>") # can't find start of output1 !!!
        sampleout = s[start:last]
        writeTo("output"+part,sampleout)
    else:
        sampleout="".join(open("output"+part)).strip()
    print("assumed output:",sampleout)
    ns=0
    while True:
        while ns == (ns := os.stat("sol.py").st_mtime_ns):
            if os.system("inotifywait -q sol.py"):
                raise Exception("inotifywait did not terminate cleanly")
        ns=os.stat("sol.py").st_mtime_ns
        
        print("==== trying sample input (10 second timeout)")
        p=subprocess.run("timeout 10 python3 sol.py input1 | tee tmp", shell=True)
        answers = "".join(open("tmp")).split()
        if p.returncode==0 and len(answers)>=1 and answers[-1]==sampleout:
            print("==== trying real input (no timeout)")
            p=subprocess.run("python3 sol.py input | tee tmpreal", shell=True)
            print("==== end of program output")
            if p.returncode:
                print("error when called on real input")
                continue
            answer = "".join(open("tmpreal")).split()
            if len(answer)<1:
                print("answer is empty when called on real input")
                continue
            answer=answer[-1]
            #do some checks on answer
            if(len(answer)<=3):
                print(repr(anwser),"looks too small. Not submitting")
            elif answer==sampleout:
                print(repr(answer), "is the same as the example output. Not submitting")
            elif answer in bad_answers:
                print(repr(answer), "previously submitted and failed. Not submitting")
            else:
                if not bad_answers or input("Do you want to submit",repr(answer),"(y/n)?")=="y":
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
    
