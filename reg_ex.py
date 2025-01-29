import re

emaildata="deepakpadmanabhan<deepakpadmanabhan@gmail.com>,shrikanta<shrikanta@gmail.com>"
result= re.search(r"shar", emaildata)
print(result)

result= re.search(r"deep[a-z]+\w+@\w+\.\w+"," emaildata)
print(result)

result= re.search(r"deep[a-z]{3}", emaildata)
print(result)

result= re.search(r"deep[a-z]+3", emaildata)
print(result)

result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", emaildata)
print(result)

result=re.search(r"deep[a-z]+", emaildata)
print(result)
