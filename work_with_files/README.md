# WORK WITH FILES IN PYTHON

Open file:

```bash
file = open('filename.txt')
```

Always make sure that an open file is properly closed in order to avoid unwanted behavior. Use try-finally block or with statement:

```bash
reader = open('filename.txt')
try:
    # code
finally:
    reader.close()

```
OR 

```bash
with open('filename.txt') as reader:
    # code

```

While opening files can use: 
'r' - open only for reading
'w' - open for writing, overwriting the file first
'rb' or 'wb' - open in binary mode (read/write using byte data)

Read 10 chars, starting from the first char in file in line (with space characters)

```bash
reader.readline(10)
```

Return txt file as a list object
```bash
f.readlines()
list(f)
```

Read and print the entire file line by line

```bash
line = reader.readline()
```

Save text file in reversed order

```bash
with open('filename.txt', 'w') as writer:
    for line in reversed(filename):
        writer.write(line)
```

