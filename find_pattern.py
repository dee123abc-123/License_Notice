#WAS to find a specific pattern

import re

email_data="deepakpadmanabhan <deepakpadmanabhan@gmail.com>, edison <edison@gmail.com>, parashu <parashu@gmail.com>"

result=re.search(r"deep", email_data)
print(result)
print("\n")

result=re.findall(r"dee", email_data)
print(result)
print("\n")

result=re.search(r"deep[a, j]", email_data)
print(result)
print("\n")

result=re.search(r"deep[a-z]", email_data)
print(result)
print("\n")

result=re.search(r"deep[a-z]{2}", email_data)
print(result)
print("\n")

result=re.search(r"deep[a-z]+", email_data)
print(result)
print("\n")

result=re.search(r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)
print("\n")

result=re.findall(r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)
print("\n")

result= re.search(r"(\w)+@(\w)+\.(\w)+", email_data)
print(result[0])
