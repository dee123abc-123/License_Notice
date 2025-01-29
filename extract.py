import json
import sys
import requests
import tarfile

with open("1.json", "r") as fh:
    json_data=json.load(fh)
    #load: funtion used to read the data from file;  loads:from strings
    print(json_data)
file_path="/home/ubuntu/behave.tar.gz"

#work with list use for loop

for ele in json_data:
   # for key,values in ele.items():
        source_url=ele("source url")
        response.raise_for_status()  #raise : an exceptionfor 4xx 5xx status codes
        with open ( "/home/ubuntu/behave.tar.gz","wb")as files:
        file.write(response.content)
        print("the file downoaded succesfully")
        break
print
file = tarfile.open( "/home/ubuntu/behave.tar.gz") 
  
# extracting file 
file.extractall('./Destination_FolderName') 
     #   print(ele["source URL"])
        print(key)
        print(value)
        print("................")
    #print(ele)
    sys.exit
