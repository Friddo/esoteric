import sys
p = ""
if len(sys.argv) == 2:
    f = open(sys.argv[1], "r")
    p = [int(a) for a in f.read().replace("\n"," ").split(" ")]
    f.close()
else:
    print("bad file")
    quit()

memSize = 256 #num of memory cells

mem = p + [0]*(memSize-len(p)) #load program into memory
i = 0
while 1:
    a = mem[i]
    b = mem[i+1]
    c = mem[i+2]
    if a == -1:
        mem[b] = ord(input())
    elif b == -1:
        print(chr(mem[a]), end='')
    else:
        mem[b] = mem[b] - mem[a]
        #branch if less than or equal to 0
        if mem[b] <= 0:
            if c < 0:
                break
            else:
                i = c-3
    i+=3