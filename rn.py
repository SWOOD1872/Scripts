import os

os.chdir('/Users/sam1872/Desktop')

for f in os.listdir(os.getcwd()):
    if f.startswith("'") and f.endswith("'"):
        os.rename(f, f[1:len(f)-1] + '.txt')