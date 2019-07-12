import os, sys

filelist = os.listdir(input())

# Forward sort and print the filenames inside the folder
for i in filelist:
    print(i)

# Backward sort and print the filenames inside the folder
for i in filelist[::-1]:
    print(i)
