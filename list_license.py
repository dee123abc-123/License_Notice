import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.lower().startswith(("notice", "license")):
            print(f"{root}/{file}")
