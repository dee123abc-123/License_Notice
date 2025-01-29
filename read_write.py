with open("loops.py", "r") as fh:
    content=fh.read()
    print(f"{content}")
    fh.close()
with open("1.txt", "w") as fh:
    fh.write("hello" "all")

with open("1.txt", "r") as fh:
    print(fh.read())

with open("1.txt", "a") as fh:
    fh.write("\n new ocontents added")
    
with open("1.txt", "r") as fh:
    print(fh.read())
