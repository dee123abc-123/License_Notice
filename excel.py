import panda as pd
import json
def check_str(x): if isinstance(x, str):x.stip()
else:x                           #x is a value, isinstance - builtin function  cheack the specific type , str is a string type,x.strip: removes white space
#it is for example
def read_excel_content (excel_file_path):
   daata= pd.read_excel(excel_file_path, "sheet_name=sheet1")
   data1=data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
   data1.to_json(json_file_path, orient='records', indent=3)  
   print("excel file converted into the json file")
#print(dir(pd))
excel_file_path= "/home/ubuntu/python/sample.xlsx"

#concept function
jason_file_path="1.jason"
read_excel_content(excel_file_path, jason)
