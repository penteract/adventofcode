#! /usr/bin/env python3
usage = """
Python script for advent of code which downloads the problem description,
attempts to extract sample input and corresponding output,
then builds and runs sol.hs on the sample input whenever sol.hs is modified until
sol.hs gives the sample output. When it does, sol.hs gets run on the real input
and if that succeeds, the last printed word gets submitted automatically.

call as `autotest.py {year} {day}` with the
environment variable $AOCSession set to the value of your session cookie


files used:
sol.hs       This program assumes that your solution for the part you are
             currently working on is in this file.
             Run as `ghc sol.hs; ./sol {input}` where {input} is the name of
             a file from which sol.hs is expected to read the input
             for the day's problem
            
input        Your personal input (https://adventofcode.com/{year}/day/{day}/input)
input1       the automatically extracted sample input
             By default this is the first non-inline code block.
             It may be wrong, and if so you must manually edit it and restart this
             program if you want it to work correctly.
             If no appropriate sample input is found, you must create this file
             to use this program.
            
output1      the automatically extracted sample output for part 1
             By default, this is the last highlighed thing at the end of a code tag.
             It may be wrong, and if so you must manually edit it and restart this
             program if you want it to work correctly.
             If no appropriate sample output is found, you must create this file
             to use this program.
            
output2      the automatically extracted sample output for part 2
1page.html   the page when solving part 1
2page.html   the page when solving part 2
wrongAnswers a text file containing a list of answers which have been rejected
             Hopefully avoids repeatedly submitting wrong answers
             Does not distinguish between part 1 and part 2
            
tmp          stores the output of sol.py on sample input
             Can be deleted without consequence except while sol.py is running
            
tmpreal      stores the output of sol.py on the real input
             Can be deleted without consequence except while sol.py is running
"""

import sys
import os
import subprocess
import math
from datetime import datetime

import urllib.request as r
print(sys.argv[0])
sesh = os.environ["AOCSession"]

headers={"Cookie":"session="+sesh, "User-Agent":"autotesths.py (using auto1/sol.hs) (https://github.com/penteract/adventofcode)"}
#headers={"User-Agent":"autotesths.py (using auto1/sol.hs) (https://github.com/penteract/adventofcode)"}

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
    #sys.argv=[None,"2022","1"]
    raise Exception("not given year and day")
year=sys.argv[1]
day=sys.argv[2]
dayurl = f"https://adventofcode.com/{year}/day/{day}"

print("PRIVATE INPUT:")
print(get_or_save(dayurl + "/input", "input"))

bad_answers=set()
bad_toohigh = None
bad_toolow = None

def fromMaybe(x,mx):
    return (mx if mx is not None else x)

if os.path.isfile("wrongAnswers"):
    with open("wrongAnswers") as f:
        for line in f:
            if "[TOO HIGH]" in line:
                line = line.split()[0]
                bad_toohigh = min(int(line), fromMaybe(math.inf, bad_toohigh))
            if "[TOO LOW]" in line:
                line = line.split()[0]
                bad_toolow = max(int(line), fromMaybe(-math.inf, bad_toolow))
            bad_answers.add(line.strip())

def add_bad(ans, content):
    global bad_toohigh, bad_toolow
    extra = ""
    if "too high" in content:
        bad_toohigh = min(int(ans), fromMaybe(math.inf, bad_toohigh))
        extra = " [TOO HIGH]"
    if "too low" in content:
        bad_toolow = max(int(ans), fromMaybe(-math.inf, bad_toolow))
        extra = " [TOO LOW]"
    bad_answers.add(ans)
    with open("wrongAnswers", mode="a") as f:
        print(ans + extra, file=f)
                  
def sanitize(eg):
    eg = eg.replace("<em>", "").replace("</em>", "")
    eg = eg.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    return eg

"""
An observational study on the tags used for the correct output given the sample input:
Prior to 2020, there's no hope (there wasn't always a clear sample input and sample output)
Since 2020, the sample output has usually been the last <em> tag inside a <code> tag.


exceptions
<em><code>ans</code></em>
2020 day 8, 9, 10 (and perhaps the rest of the year)
2021 day 1
2022 day 1


In 2020 there are some days with multiple exaples
2020 day 10 part 1


2020 day 1, there is a <code> tag in the middle of an <em> tag which is not an answer
"""
def get_out(s):
    last = s.rfind("</em></code>")
    last_ = s.rfind("</code></em>")
    if last <= last_:
        last = last_
        assert last!=-1 #can't find sample output
        start = s.rfind("<code>",0,last)+len("<code>")
        assert start >= len("<code>") # can't find start of sample output !!!
    else:
        start = s.rfind("<em>",0,last)+len("<em>")
        assert start >= len("<em>") # can't find start of sample output !!!
    return start,last

def surrounding_tag(s,i,tag):
    """find a tag surrounding location i"""
    opn = s.rfind("<"+tag+">",0,i)
    if opn == -1: return False
    opn+=len("<"+tag+">")
    close = s.find("</"+tag+">",opn)
    assert close!=-1 #cannot find matching tag
    if close<i:
        return False
    return (opn,close)

#potentially problematic examples
#https://adventofcode.com/2020/day/2
#https://adventofcode.com/2022/day/1
def find_list(s,start,last,part):
    t = surrounding_tag(s,start,"ul")
    if not t:
        return False
    ul = s[t[0]:t[1]]
    examples = []
    print("found list, looking for multiple examples")
    for line in ul.split("<li>"):
        try:
            start,end = get_out(line)
        except Exception:
            continue
        out = sanitize(line[start:end])
        start=line.find("<code>")+len("<code>")
        if start<len("<code>"):
            continue
        end=line.find("</code>")
        assert end!=-1 # no matching tag
        inp = line[start:end]
        if "<" in inp: #input contains a tag - this also 
            continue
        inp = sanitize(inp)
        if len(inp)<=1:
            continue
        i=len(examples)+1
        print("example",i,"input:")
        print(inp)
        print("example",i,"output:")
        print(out)
        writeTo(f"output{part}-{i}",out)
        writeTo(f"input{part}-{i}",inp)
        examples.append((f"input{part}-{i}", out))
    return examples

def find_examples(part):
    """begin by finding the output. If it's in a list, assume there's a list of examples,
       otherwise just assume there's one example"""
    s=get_or_save(dayurl, part+"page.html")
    outputfile = "output"+part+"-1"
    if not os.path.isfile("output"+part+"-1"):
        print("Trying to find sample output to save in ",outputfile)
        s=get_or_save(dayurl, str(part)+"page.html")
        completed=s.count("Your puzzle answer was")
        if str(completed+1)!=part:
            raise Exception(f"the given part ({part}) cannot be done when {completed} are completed")
        start,last=get_out(s)
        if part=="2" and start<=s.find("--- Part Two ---"):
            raise Exception("Can't find part 2 sample output")
        #check if it's in a list
        #if (result:=find_list(s,start,last,part)):
        #    return result #(don't check because it didn't work 2022 day 1)
        sampleout = sanitize(s[start:last])
        writeTo(outputfile,sampleout)
    else:
        i=1
        examples=[]
        while os.path.isfile(f"output{part}-{i}"):
            out = readString(f"output{part}-{i}").strip()
            if os.path.isfile(f"input{part}-{i}"):
                examples.append((f"input{part}-{i}",out))
            elif os.path.isfile(f"input{i}"):
                examples.append((f"input{i}",out))
            else:
                if part=="1":
                    sampleout = out
                break
            i+=1
        if examples:
            return examples
    if not os.path.isfile("input1"):
        print("Trying to find sample input to save in ","input1")
        s=get_or_save(dayurl, part+"page.html")
        
        start=s.find("<pre><code>")
        end=s.find("</code></pre>")
        assert start!=-1 # can't find pre block
        assert end!=-1 # can't find end of pre block !!!
        eg=sanitize(s[start+len("<pre><code>"):end])
        writeTo("input1",eg)
        print("sample input:")
        print(eg)
    return [("input1",sampleout)]



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
    if part=="2" and day=="25":
        submit(part="2", answer="0")
        
    examples = find_examples(part)
    sampleouts = { x[1] for x in examples}
    
    print("number of examples:",len(examples))
    ns=0
    firstIteration=True
    while True:
        while ns == (ns := os.stat("sol.hs").st_mtime_ns):
            if os.system("inotifywait -q sol.hs"):
                raise Exception("inotifywait did not terminate cleanly")
        ns=os.stat("sol.hs").st_mtime_ns
        
        error=None
        for inp,sampleout in examples:
            print("==== trying sample input (10 second timeout)")
            if firstIteration:
                p=tee_with_exitcode(f"timeout 20 ./sol {inp} 2>&1", "tmp")
                firstIteration=False
            else:
                p=tee_with_exitcode(f"ghc sol.hs && timeout 20 ./sol {inp} 2>&1", "tmp")
            #subprocess.run("(exit `((timeout 10 python3 sol.py input1 2>&1 ; echo $? >&3) | tee tmp >&4) 3>&1) 4>&1", shell=True)
            answers = readString("tmp").split()
            if not (p.returncode==0 and len(answers)>=1 and answers[-1]==sampleout):
                print("==== did not get output matching",sampleout)
                error=True
        if error is None:
            print("==== trying real input (no timeout)")
            #p=subprocess.run("python3 sol.py input | tee tmpreal", shell=True)
            p=tee_with_exitcode("./sol input","tmpreal")
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
            elif answer in sampleouts:
                print(repr(answer), "is the same as the example output. Not submitting")
            elif answer in bad_answers:
                print(repr(answer), "previously submitted and failed. Not submitting")
            elif bad_toohigh is not None and int(answer) >= bad_toohigh:
                print(repr(answer),
                      f"is too high; as {bad_toohigh} was. Not submitting.")
            elif bad_toolow is not None and int(answer) <= bad_toolow:
                print(repr(answer),
                      f"is too low; as {bad_toolow} was. Not submitting.")
            else:
                if not bad_answers or input("Do you want to submit "+repr(answer)+" (y/n)?")=="y":
                    print("submitting answer:",repr(answer))
                    resp,content = submit(part=part,answer=answer)
                    if "That's the right answer!" in content:
                        succeeded=True
                        os.system(f"cp sol.hs part{part}sol.hs")
                        break
                    elif "That's not the right answer" in content:
                        add_bad(answer,content)
                    else:
                        print("did not recognise success or incorrect, may be timeout or blank input or already completed")
        else:
            print("==== not trying real input")
    return part

if len(sys.argv)<4:
    if doPart() == "1":
        doPart("2")
else:
    doPart(sys.argv[3])
