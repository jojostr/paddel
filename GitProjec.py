def ausgabe():

    with open('/Users/jstriedl/Git/GitProjects2022/testfile', 'r') as f:
        print(f.read())

f = open("testfile", "a")
i=1
n=10
while i<=n:
    f.write("Now the file has more content!"+"\n")
    ausgabe()
    i=i+1
f.close()
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist

import os
os.remove("testfile")