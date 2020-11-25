#vars
p = "+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+."
memSize = 32 #num of avaliable variable spots

maxValue = 256 #standard for brainfuck


#code
import os;import platform as pf
clear = lambda: os.system((pf.system() == "Darwin") * 'clear' + (pf.system() != "Darwin") * 'cls')
clear()
print("input:\n"+p+"\n")
print("output:")
pointer = 0
tape = [0]*memSize

p = [ch for ch in p] #sanitize input
i = 0
while i < len(p):
    c = p[i]
    #increment/decrement functions
    if c == "+":
        tape[pointer]=(tape[pointer]+1)%maxValue  #increment at pointer
    if c == "-":
        tape[pointer]=(tape[pointer]-1)%maxValue  #decrement at pointer
    #moving pointer
    if c == ">":
        pointer=(pointer+1)%memSize #right
    elif c == "<":
        pointer=(pointer-1)%memSize #left
    #accepting input at pointer
    elif c == ",":
        tape[pointer] = ord(input()) #take input and convert to ASCII
    #output at pointer
    elif c == ".":
        print(chr(tape[pointer]), end = '') #print ASCII char inline

    #loop handles
    elif c == '[':
        if tape[pointer] == 0:
            open_braces = 1
            while open_braces > 0:
                i += 1
                if p[i] == '[':
                    open_braces += 1
                elif p[i] == ']':
                    open_braces -= 1
    elif c == ']':
        open_braces = 1
        while open_braces > 0:
            i -= 1
            if p[i] == '[':
                open_braces -= 1
            elif p[i] == ']':
                open_braces += 1
        i -= 1

    #next char
    i+=1
print("\n")
