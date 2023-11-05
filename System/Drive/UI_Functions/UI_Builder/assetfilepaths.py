import os
from pprint import pprint


def generateFilePathDict(filePath):
    dirDict = {}    
    dirLst = os.listdir(filePath)

    for file in dirLst:
        if (file[0] == "^"):
            dirDict[file[1:]] = generateFilePathDict(os.path.join(filePath, file))
        
        else:
            dirDict[file[:-4]] = os.path.join(filePath, file)

    return dirDict


if __name__ == "__main__":
    pprint(generateFilePathDict("/System/Drive/Assets"))
