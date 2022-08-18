#read contents of a file
#file name if in project folder
#file name with path if in computer

#using open() will close file automatically
#try:
#    with open('text.xt') as file:
##except FileNotFoundError:
#    print('file not found')




#....... writing files in python .........
#text = 'hi i hope you are well'
#let = 'a' # 'w' overwrites and writes, 'a' appends or adds, 'r' reads

#with open('test.txt', let) as file:
#    file.write(text)



#......copying files in python
#import shutil
#all below functions have same arguments but copy different things
#depending on needs for project/program
#copyfile() = copies contents
#copy() = copyfile() + permission mode + destination can be dir
#copy2() = copy() + copies metadata (file's creation and mod times)

#shutil.copyfile('test.txt', 'copy.txt') #src,dst


#........move files using python.....
#import os
#source = " " if on project directory, file name; else file path
#dest = " "



#............delete file using python......
#shutil.rmtree(path) will delete direcotry with filesi n it  from import shutil
#os.rmdir(path) #deletes directory with no files
#os.remove(path)
#cannot delete empty files


#..........modules.......
#modular programming, separate a program into separate parts
import os
destination = 'day6dir'
source = 'day6'

#try:
#    if os.path.exists(destination):
#        print('there is already a file')
#    else:
#        os.replace(source,destination)
#        print(source+" was moved")
#except FileNotFoundError:
#   print(source+' not found')

