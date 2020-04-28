from PySide2 import QtCore

from modules.encryptNote import AEScipher
from modules.userLogin import readUserInfo

class FILE():
    _file = None
    _details = {"path":""}
    _open = False
    def __init__(self):
        pass
    
    def openFile(self,item,details):
        if(self._open == True):
            self.closeFile() # In case a some previous file was open

        self._item = item
        self._name = item.text(0)
        self._details = details
        self._file = open(self._details["path"],"r+")
        self._open = True

    def closeFile(self):
        self._file.close()
        self._open = False

    def getText(self,encryptAll = True):
        if(encryptAll == True): # decrypt text
            userInfo = readUserInfo()
            aes = AEScipher(userInfo[1],self,encrypt = False)
            txt = aes.Decrypt()
        else:
            txt = self._file.read()
        self._file.seek(0)
        # print(txt)
        return txt

    def getFilename(self):
        return self._name
    
    def getRandomString(self):
        return self._details['randomString']
    
    def saveFile(self,text,encryptAll = True):
        if not self._open:
            return
        if('encrypted' in self._details and self._details['encrypted'] == 'True'): # don't save if file is encrypted
            return
        self._file.seek(0)
        self._file.truncate()
        if(encryptAll == True):
            userInfo = readUserInfo()
            aes = AEScipher(str(userInfo[1]),self,text,encrypt = True)
            text = aes.Encrypt()
            # print("text from encryption",text)
            with open(self._details["path"],"wb") as file:
                file.write(text)
                file.seek(0)
        else:
            self._file.write(text)
        self._file.seek(0)
        # self._file.flush()


currentNote = FILE()