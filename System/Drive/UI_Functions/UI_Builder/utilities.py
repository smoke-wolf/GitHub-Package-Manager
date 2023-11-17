''' This file contains the file handler that handles file reading and writing. '''


class FileHandler:

    '''
    This class provides handlers for reading from, writing to, or
    appending to a particular file. The methods are pretty much
    self explanatory. 
    '''

    def readTextFile(self, filePath):
        with open(filePath, mode='r', encoding='utf-8') as file:
            text = file.readlines()
            text = '\n'.join(text)

        return text

    def writeTextFile(self, filePath, data):
        with open(filePath, mode='w', encoding='utf-8') as file:
            file.write(data)
    
    def appendTextFile(self, filePath, data):
        with open(filePath, mode='a', encoding='utf-8') as file:
            file.write(data)
    
