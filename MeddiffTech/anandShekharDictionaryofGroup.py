#Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner name, in any order.


def group_by_owners(ownerfiles):            #ownerfiles is taken as input
    ownersdictionary = {}
    for key,value in ownerfiles.items():            #file name is taken as key and its owner as value
        if value in ownersdictionary.keys():
            ownersdictionary[value].append(key)
        else:
            ownersdictionary[value] = [key]
    return ownersdictionary

ownerfiles = {
            'dataInputFiles.txt': 'Shekhar',
            'somePythonCode.py': 'Shekhar',
            'dataOutputFilesForDict.txt': 'Anand',
'dataOutputFilesForPython.py': 'Anand'
        }



print(group_by_owners(ownerfiles))
