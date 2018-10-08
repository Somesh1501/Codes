import os , shutil
path = open(r"/home/ironman/Desktop/lists.txt","r+")
svg = '/home/ironman/Pictures/Wallpapers'
i = 0
def is_file(s):
    if s.endswith('.jpg') or s.endswith('.png'):
         return s
    else:
         pass
for fil in path:
    for folder , subfolder , files in os.walk(fil.strip()):
        for f , s , t in os.walk(folder):
            for te in t:
                s = te.split('.')
                a = s[-2] + '_1'
                s[-2] = a
                p = '.'.join(s)
                path = os.path.join(f,p)
                print(i,path)
                try:
                    if is_file(te):
                        shutil.move(path,svg)
                except shutil.Error:
                    continue

