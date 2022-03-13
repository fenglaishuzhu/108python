import os 

def search_files(path, filetype):
    rlt = []
    for roots, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(filetype):
                rlt.append(roots+"\\"+filename)
    return rlt 

def search_files_rlt2txt(rlt,rltfile="search_files_rlt.txt"):
    if not os.path.exists(rltfile):
        mode = 'w'
    else:
        mode = "a+" #追加读写

    rlt = [i+"\n" for i in rlt]
    with open(rltfile, mode, encoding="utf-8") as f:
        f.writelines(rlt)

filetype = (".js", ".py")
path = "."
rlt = search_files(path, filetype)
search_files_rlt2txt(rlt)