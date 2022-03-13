import os

filetype = (".py", ".js")
path = ".."

for roots, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith(filetype):
            print(roots+"\\"+filename)

