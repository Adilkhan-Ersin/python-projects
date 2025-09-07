import sys
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        c=0
        with open(sys.argv[1], 'r') as file:
            lines=file.readlines()
            for line in lines:
                if not (line.isspace() or line.lstrip().startswith("#")):
                    c+=1
            print(c)
    else:
        sys.exit("Not a Python file")
