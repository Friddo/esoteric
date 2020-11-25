
#load program
import sys
p = ""
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")
    p = r''.join(f.read().replace("\n",""))
    f.close()
else:
    print("bad file")
    quit()
print(p)

#load clear command
import os;import platform as pf
clear = lambda: os.system((pf.system() == "Darwin") * 'clear' + (pf.system() != "Darwin") * 'cls')
clear()

#interpreter
def slashes(s):
  while s:
    buff = ["","",1]
    for t in (0,1,2):
      while s:
        if s[0] == "/" :         s = s[1:]; break
        if s[0] == "\\":         s = s[1:]
        if t: buff[t-1] += s[0]; s = s[1:]
        else: yield        s[0]; s = s[1:]
    while s and buff[0] in s: s = s.replace(*buff)

#output
out = "".join(slashes(p))

print("input:\n"+p+"\n")
print("output:\n"+out+"\n")
