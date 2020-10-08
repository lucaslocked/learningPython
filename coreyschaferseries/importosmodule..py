import os

#Change directories
os.chdir('/aditya/home/programming/relearningpython')

#Make directories
# os.mkdir('import-os-demo/sub-dir')
#os.makedirs('import-os-demo/sub-dir')

#Remove directories
# os.rmdir()
#os.removedirs('import-os-demo/sub-dir')

#Rename files
# os.rename('demo.txt')

#File stats
# os.stat('demo.txt')

#Walk method
for dirpath, dirnames, filenames in os.walk('/aditya/home/programming/relearningpython'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()

print(os.listdir())