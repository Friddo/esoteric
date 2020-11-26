#load program
import sys
p = ""
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")
    p = ''.join(filter(lambda x: x in ['i', 'd', 's', 'o'], f.read()))
    f.close()
else:
    print("bad file")
    quit()
a,i = 0,0
while i < len(p):
    c=p[i]
    if a==256 or a<0:
        a=0
    if c=='i':
        a+=1
    elif c=='d':
        a-=1
    elif c=='o':
        print(a)
    elif c=='s':
        a*=a
    i+=1
