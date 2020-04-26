
from PySide2 import QtWidgets,QtGui

from modules.setPassword import password
from modules.fileHandling import currentNote
from modules.markdownHandling import viewInMarkdown
from modules.treeHandling import loadfileStructure, noteLoader,itemVal, isNote
from modules.GUIchanges import createNotebook, createSubNotebook, createNote, rename, dlt
from modules.searchInNote import searchText,finishedSearch


def showMenu(self,pos):
    item = self.ui.treeWidget.itemAt(pos)
    print(item.text(0))
    if item is None:
        return
    menu = QtWidgets.QMenu()
    if item is self.ui.treeWidget.topLevelItem(0):
        menu.addAction(createNotebook)
    elif item is self.ui.treeWidget.topLevelItem(1):
        menu.addAction(createNote)
    else:
        dets = isNote(item)
        if(dets[0]):
            pass
        else:
            menu.addAction(createSubNotebook)
            menu.addAction(createNote)
        menu.addAction(rename)
        menu.addAction(dlt)
    menu.exec_(self.ui.treeWidget.mapToGlobal(pos))


def _delayChecker(self):
    if(self.timer.isActive()):
        self.timer.stop()
    self.timer.start(self.DELAY)

def _noteLoader(self):
    changeNote = lambda : noteLoader(self.ui.treeWidget.selectedItems()[0],self.ui.fileName,self.ui.plainTextEdit)
    self.ui.treeWidget.itemSelectionChanged.connect(changeNote)

def _markdownViewer(self):
    mdView = lambda: viewInMarkdown(self.ui.plainTextEdit.toPlainText(),self.mdExtensions,self.ui.mdViewer)
    sFile = lambda: currentNote.saveFile(self.ui.plainTextEdit.toPlainText())
    self.timer.timeout.connect(sFile)
    self.timer.timeout.connect(mdView)
    self.ui.plainTextEdit.textChanged.connect(self._delayChecker)


def encryptNote(self):
    self.passwdE = password(self)
    self.ui.encryptionButton.clicked.connect(lambda: self.passwdE.openPasswordDialog())

    
def decryptNote(self):
    self.passwdD = password(self)
    self.ui.decryptionButton.clicked.connect(lambda: self.passwdD.openVerifyPasswordDialog())

def searchInNote(self):
    self.ui.searchBar.textChanged.connect(lambda: searchText(self.ui))
    
def searchModeChanged(self):
    self.ui.wholeWord.clicked.connect(lambda:searchText(self.ui))
    self.ui.regexButton.clicked.connect(lambda:searchText(self.ui))
    self.ui.matchCase.clicked.connect(lambda:searchText(self.ui))

def findNextOccurance(self):
    self.ui.nextMatch.clicked.connect(lambda :searchText(self.ui,QtGui.QTextCursor.NextCharacter))

def findPrevOccurance(self):
    self.ui.prevMatch.clicked.connect(lambda :searchText(self.ui,QtGui.QTextCursor.PreviousCharacter,reversed = True))

def _finishedSearch(self):
    self.ui.searchBar.editingFinished.connect(lambda :finishedSearch(self.ui.errorLabel))

def reloadUI(self):
    loadfileStructure(self.ui.treeWidget)
    self._noteLoader()

    
def closeEvent(self,event):
    currentNote.closeFile()
    event.accept()

