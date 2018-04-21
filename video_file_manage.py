import os
from collections import defaultdict
#from pprint import pprint
import shutil

# work_dir = r"d:\Downloads\TV\了不起的麦瑟尔夫人\\"
# work_dir = r"d:\Downloads\TV"
work_dir = os.getcwd()
print('\nwork_dir: ', work_dir,'\n')

def split2group(string,seperator,groups,groupBy=0):
    nameSplits=string.split(seperator)
#     print('[split]@',seperator,'\t',nameSplits)
    if( len(nameSplits)>=2 ):
        dirName = nameSplits[groupBy].strip()
        groups[dirName].append(string)
#         print(dirName)
        return(True)
    else:
        return(False)


dirs = defaultdict(lambda:[])
seps = ['.S0', '.S1', '.第', "第","]EP",".Ep"]
include_suffix = ['.mp4','.rmvb','mkv','.avi']
with os.scandir(work_dir) as it:
    for entry in it:
        isIncludedSuffix = False
        for suf in include_suffix:
            if entry.name.endswith(suf):
                isIncludedSuffix = True
                break
            else:
                continue
        if entry.is_file() and  not entry.name.startswith('.') and isIncludedSuffix:
#             print(entry.name)
            for sep in seps:
                if split2group( string=entry.name, seperator=sep, groups=dirs ):
                    isGrouped = True
                    break
            else:
                isGrouped = False
#             print(isGrouped,'\t', entry.name)
            if not isGrouped:
                dirs['[]'].append(entry.name)
            
            
print("================Starting================")
# pprint(dirs)
for (k) in dirs:
    # print(work_dir,'\t',k)
    path = os.path.join(work_dir,k)
    print(k,'\t',path)
    if not os.path.exists(path):
        print('Making dir:'+path)
        os.mkdir(path)
    for v in dirs[k]:
        print('  +',v,'\t==>>\t'+ os.path.join(work_dir,v))
        shutil.move(src=os.path.join(work_dir,v), dst=os.path.join(path, v))
print("================Finished================")