import os

for dpath, dnames, fnames in os.walk('D:\\03 Python\\'):
    for f in fnames:
        #os.chdir(dpath)
        print(f)
        # if f.startswith('[FreeCourseLab.com] Udemy - '):
        #         #         #     print(f)