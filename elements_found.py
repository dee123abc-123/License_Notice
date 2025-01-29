mylist=[".", 34, "!", "now_what"]

mydict={
        "name": "vibs",
        "age": 26,
        "from": "bengaluru"
        }
mylist1=[]
if "now_what" in mylist:
    print("element found")
else:
    print("element not found")

if mylist1:
    print("list contains values")
else:
    print("list is empty")
if "name" in mydict:
    print("key_found")
else:
    print("key not found")

#comparing if the key and value

found = True

if found:
    print("true")
if not found:
    print("false")
