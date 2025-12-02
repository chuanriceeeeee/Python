file_paths = [ "/home/user/documents/file1.txt", "/var/log/system.log", "/tmp/temp_file.py"]
fileName=[]
IndexList=[]
TempStr="/Users/user"
Count=len(list(TempStr))
for _ in file_paths:
    str=_[_.rfind('/')+1:]
    fileName.append(str)
print(fileName)
for _ in fileName:
    AfterAppend=_[_.rfind('.'):]
    if AfterAppend=='.py':
        IndexList.append(_)
for _ in IndexList:
    print({_})
for _ in file_paths:
    boolIndex=_.find('/home/user')
    if boolIndex!=-1:
        file_paths[file_paths.index(_)]=TempStr+_[int(boolIndex)+Count-1:]
print(file_paths)