#Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate file.


from pathlib import Path

filepath = 'E:\TryFilesforMeddiff\errorLog.txt'         #Previously logged error file, from which we are reading errors & warnings

if Path('E:\TryFilesforMeddiff\errorLogNewWrite.txt').is_file():        #code to create new error file to log errors and warnings into it,
    print("file exists")                                                #check whether it is already existing, then we should open and append the errors
    newfilepath = open('E:\TryFilesforMeddiff\errorLogNewWrite.txt', 'a')
else:
    newfilepath = open('E:\TryFilesforMeddiff\errorLogNewWrite.txt', 'x')

with open(filepath) as fp:
    line = fp.readline()
    count = 1                               #to check the line count
    while line:
        print("Line {}: {}".format(count, line.strip()))
        line = fp.readline()
        count += 1
        writeline = newfilepath.write(line)
    newfilepath.close()