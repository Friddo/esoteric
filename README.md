# Esoteric Interpreters

A library of esoteric language interpreters

**These are made to be the bare minimum, and is a stepping stone to write a more complete interpreter*

Languages:
1. [Fractran](#fractran)
2. [Brainfuck](#brainfuck)
3. [Slashes (///) ](#slashes)




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
python3 brainfuck.py filename.bf
```
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
python3 slashes.py filename.slash
```
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






