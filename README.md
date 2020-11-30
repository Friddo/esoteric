# Esoteric Interpreters

A library of esoteric language interpreters

**These are made to be the bare minimum, and is a stepping stone to write a more complete interpreter**

Languages:
1. [Fractran](#fractran)
2. [Brainfuck](#brainfuck)
3. [Slashes (///) ](#slashes)
4. [Deadfish](#deadfish)
5. [Subleq](#subleq)
- parser

To Do:
* Piet

<a name="fractran"></a>
## Fractran

For more info on the language, visit: 
* [Fractran on Wikipedia](https://en.wikipedia.org/wiki/FRACTRAN)
* [Fractran on Esolangs](https://esolangs.org/wiki/Fractran)

### Languages:

* Python 3.8.x

### Usage:

1. choose N, your input
2. define p, the program (format: "2/3,11/3")
3. choose whether you want to step through the program or not

### Output:

The program will display prime factors and their exponents, such that A^B will turn out vA: B


<a name="brainfuck"></a>
## Brainfuck

For more info on the language, visit: 
* [Brainfuck on Wikipedia](https://en.wikipedia.org/wiki/Brainfuck)
* [Brainfuck on Esolangs](https://esolangs.org/wiki/Brainfuck)

### Languages:

* Python 3.8.x

### Usage:

```
python3 brainfuck.py filename
```
filename is a file containing any valid brainfuck code
* valid characters include: `> < [ ] + - . ,`

### Output:

* inline print from `.` operator

### Examples:

* Hello World:
```
program:
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

output:
Hello World!
```


<a name="slashes"></a>
## Slashes (///)

For more info on the language, visit: 
* [Slashes on Esolangs](https://esolangs.org/wiki////)

### Languages:

* Python 3.8.x

### Usage:

```
python3 slashes.py filename
```
filename is a file containing any valid slash code
### Output:

* final state of program

### Examples:

* Hello World:
```
program:
/foo/Hello, world!//bar/foo/bar

output:
Hello, World!
```

<a name="deadfish"></a>
## Deadfish

For more info on the language, visit: 
* [Deadfish on Esolangs](https://esolangs.org/wiki/Deadfish)

### Languages:

* Python 3.8.x

### Usage:

```
python3 deadfish.py filename
```
filename is a file containing any valid deadfish code
* valid characters include: `i d s o`
### Output:

* outputs accumulator value when reaching `o` , prints newline after

### Examples:

* Hello World: (will output unicode values, since no text can be outputted)
```
program:
iisiiiisiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiio
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddo
dddddddddddddddddddddsddoddddddddoiiioddddddoddddddddo

output:
72
101
108
108
111
32
119
111
114
108
100
```


<a name="subleq"></a>
## Subleq

For more info on the language, visit: 
* [Subleq on Esolangs](https://esolangs.org/wiki/Subleq)

### Languages:

* Python 3.8.x

### Usage:

```
python3 subleq.py filename.subleq
```
filename is a file containing any valid subleq code

### Output:

Prints inline when reaching instruction where `B = -1`

### Examples:

* Hello World:
```
program:
15 17 -1
17 -1 -1
16 1 -1
16 3 -1
15 15 0
0 -1 72
101
108
108
111
44
32
119
111
114
108
100
33
10
10
0

output:
Hello, World!
```




