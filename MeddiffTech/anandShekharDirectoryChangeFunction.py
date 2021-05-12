class directoryChange:
    def __init__(self, path):           #initializing
        self.currentPath = path

    def cd(self, getNewPath):
        i=0;
        newPath=getNewPath.split('/')                 #..direct
        pathLen=len(newPath)                          #8
        pathList=self.currentPath.split('/')          #e: TryfilesforMediff directorychange
        print(newPath)
        print(pathList)
        if newPath[0]=='':
            del pathList[:]
            pathList.append('/'+newPath[1])
            i=i+2
        while(i<pathLen):
            j=len(pathList)-1
            if newPath[i]=='..':
                #parent directory
                pathList.pop(j)
            else:
                pathList.append(newPath[i])
            i=i+1
        self.currentPath="/".join(pathList)

        pass

path = directoryChange('E:/TryFilesforMeddiff/DirectoryChange')
path.cd('../direct')
print(path.currentPath)