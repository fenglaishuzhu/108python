import os 

frompath = "/home/pi/Desktop/hello"
topath = "/home/pi/Desktop/temp"

x = os.listdir(frompath)

if not os.path.exists(topath):
    os.makedirs(topath)
    
for i in x:
    bf = "/".join([frompath,i])
    af = "/".join([topath,i])
    if os.path.exists(af):
        af_backup = af+"_backup"
        print("rename_dir", af, af_backup)
        os.rename(af, af_backup)
    print("copy_dir", bf, af)
    os.system(f"cp {bf} {af}")