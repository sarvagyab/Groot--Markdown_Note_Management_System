from PySide2 import QtWidgets

#GUI
from GUIs.passwordDialog import Ui_passwordDialog

from modules.Exceptions import *
from modules.passwordHashing import hashPassword
from modules.treeHandling import itemVal,_itemVal
from modules.noteHandling import loadNote


class password(object):
    def __init__(self):
        self.ERROR_MSG = ""
        self.passwordset = False
    
    def openPasswordDialog(self,Window):
        print("Encryption button clicked")
        self.currentNote = Window.ui.treeWidget.selectedItems()
        self.currentFileName = Window.ui.treeWidget.selectedItems()[0].text(0)
        print("Trying to encrypt {}".format(self.currentFileName))
        self.main_Window = Window
        # First check whether any note is selected or not
        if(self.selectedNote()):

            self.ui_p = Ui_passwordDialog()

            # slot-signals
            self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda:self.passwordEntered())
            self.ui_p.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda:self.ui_p.passwordDialog.close())


    def selectedNote(self):
        if(len(self.currentNote) == 0): 
            print("Any note is not selected") # nothing is selected.
            return False
        else:
            item = itemVal(self.currentNote[0])
            if("path" in item and type(item["path"]) == str):
                self.currentNote = item
                return True
            else:
                print("select note")
                return False
    
    def passwordEntered(self):
        self.pass1 = self.ui_p.passwordLineEdit.text()
        self.pass2 = self.ui_p.RepasswordLineEdit.text()
        self.setPassword()
        if(self.passwordset == True):
            print("Password valid")
            self.closeDialog()
            hashPassword(self.currentNote,self.currentFileName,self.pass1)
            loadNote(self.currentNote['path'],self.main_Window.ui.plainTextEdit) # reload text window
            
            
    def setPassword(self):
        """ Check whether password entered in 'password' and 're-enter password' fields are same or not."""
        try:
            self.arePasswordSame()
            self.doesLengthGt8()
            self.doesContainCapitalLetter()
            self.doesContainDigit()
        except:
            self.displayInstruction()
        else:
            self.ERROR_MSG = "Password is set successfully."
            self.passwordset = True
            self.displayInstruction()
    
    def displayInstruction(self):
        # Prepare message to display
        if(self.passwordset == False):
            MSG ="<html><head/><body><p><span style=\" color:#ff0000;\">"+self.ERROR_MSG+"</span></p></body></html>"
        else:
            MSG ="<html><head/><body><p><span style=\" color:#00ff0d;\">"+self.ERROR_MSG+"</span></p></body></html>"
        self.ui_p.Errortext.setText(MSG)


    def arePasswordSame(self):
        """Check whether entered passwards are same or not"""
        if(self.pass1 != self.pass2):
            self.ERROR_MSG = "Passwards did not match"
            raise PasswardDidNotMatchError(self.ERROR_MSG)

    def doesLengthGt8(self):
        """Check whether entered passwards have length greater than 8 or not"""
        if(len(self.pass1) < 8):
            self.ERROR_MSG = "Password must contain atleast 8 characters."
            raise LengthNotEnoughError(self.ERROR_MSG) 

    def doesContainCapitalLetter(self):
        """Check whether entered passwards have atleast one capital letter or not"""    
        if(not any(x.isupper() for x in self.pass1)):
            self.ERROR_MSG = "Password must contain atleast one capital letter"
            raise DoesNotContainCapitalLetterError(self.ERROR_MSG)

    def doesContainDigit(self):
        """Check whether entered passwards have atleast one digit or not"""    
        if(not any(x.isdigit() for x in self.pass1)):
            self.ERROR_MSG = "Password must contain atleast one digit"
            raise DoesNotContainCapitalLetterError(self.ERROR_MSG)
    
    def closeDialog(self):
        self.ui_p.passwordDialog.close()
