import shutil, glob, os

#Prints all text files in directory
directory_txt = "C:\\Users\\Student\\Desktop\\A\\*.txt"
for path in glob.glob(directory_txt):
    print( path )
    
#Moves all files with .txt extension from folder 'A' to folder 'B'
sourcepath='C:/Users/Student/Desktop/A/'
source = os.listdir('C:/Users/Student/Desktop/A/')
destinationpath = 'C:/Users/Student/Desktop/B/'
for files in source:
    if files.endswith('.txt'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))
    else:
        print('No files with .txt extension to move!')
