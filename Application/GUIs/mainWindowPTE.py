# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowPTE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Groot(object):
    def setupUi(self, Groot):
        Groot.setObjectName("Groot")
        Groot.resize(1480, 807)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Groot.sizePolicy().hasHeightForWidth())
        Groot.setSizePolicy(sizePolicy)
        Groot.setStyleSheet("background-color: rgba(252, 252, 252, 252);")
        self.centralwidget = QtWidgets.QWidget(Groot)
        self.centralwidget.setStyleSheet("background-color:rgb(252, 252, 252);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainWindow = QtWidgets.QWidget(self.centralwidget)
        self.mainWindow.setObjectName("mainWindow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rootOptions = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rootOptions.sizePolicy().hasHeightForWidth())
        self.rootOptions.setSizePolicy(sizePolicy)
        self.rootOptions.setMinimumSize(QtCore.QSize(0, 0))
        self.rootOptions.setObjectName("rootOptions")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.rootOptions)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newNote = QtWidgets.QPushButton(self.rootOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNote.sizePolicy().hasHeightForWidth())
        self.newNote.setSizePolicy(sizePolicy)
        self.newNote.setMinimumSize(QtCore.QSize(0, 0))
        self.newNote.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newNote.setObjectName("newNote")
        self.horizontalLayout_6.addWidget(self.newNote)
        self.newNotebook = QtWidgets.QPushButton(self.rootOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newNotebook.sizePolicy().hasHeightForWidth())
        self.newNotebook.setSizePolicy(sizePolicy)
        self.newNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newNotebook.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.newNotebook.setObjectName("newNotebook")
        self.horizontalLayout_6.addWidget(self.newNotebook)
        self.newSubNotebook = QtWidgets.QPushButton(self.rootOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newSubNotebook.sizePolicy().hasHeightForWidth())
        self.newSubNotebook.setSizePolicy(sizePolicy)
        self.newSubNotebook.setMinimumSize(QtCore.QSize(0, 0))
        self.newSubNotebook.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newSubNotebook.setObjectName("newSubNotebook")
        self.horizontalLayout_6.addWidget(self.newSubNotebook)
        self.lineEdit = QtWidgets.QLineEdit(self.rootOptions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addWidget(self.rootOptions)
        self.centralView = QtWidgets.QWidget(self.mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralView.sizePolicy().hasHeightForWidth())
        self.centralView.setSizePolicy(sizePolicy)
        self.centralView.setMinimumSize(QtCore.QSize(0, 0))
        self.centralView.setObjectName("centralView")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralView)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralView)
        self.treeWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet("background-color:rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")
        self.treeWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        item_0.setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        item_0.setFont(0, font)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.treeWidget)
        self.editorArea = QtWidgets.QWidget(self.centralView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editorArea.sizePolicy().hasHeightForWidth())
        self.editorArea.setSizePolicy(sizePolicy)
        self.editorArea.setObjectName("editorArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.editorArea)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleArea = QtWidgets.QWidget(self.editorArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleArea.sizePolicy().hasHeightForWidth())
        self.titleArea.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(3)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        self.titleArea.setFont(font)
        self.titleArea.setStyleSheet("border: 100px ;\n"
"border-bottom-color: rgb(255, 255, 127);")
        self.titleArea.setObjectName("titleArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(self.titleArea)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("")
        self.fileName.setScaledContents(False)
        self.fileName.setAlignment(QtCore.Qt.AlignCenter)
        self.fileName.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        self.verticalLayout_2.addWidget(self.titleArea)
        self.editingButtons = QtWidgets.QWidget(self.editorArea)
        self.editingButtons.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editingButtons.sizePolicy().hasHeightForWidth())
        self.editingButtons.setSizePolicy(sizePolicy)
        self.editingButtons.setAutoFillBackground(False)
        self.editingButtons.setStyleSheet("<html>\n"
"<style>\n"
"body {background-color: powderblue;}\n"
"h1   {color: blue;}\n"
"p    {color: red;}\n"
"</style>\n"
"</html>")
        self.editingButtons.setObjectName("editingButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.editingButtons)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.editingButtons)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.link = QtWidgets.QPushButton(self.editingButtons)
        self.link.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.link.setObjectName("link")
        self.horizontalLayout_3.addWidget(self.link)
        self.code = QtWidgets.QPushButton(self.editingButtons)
        self.code.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.code.setObjectName("code")
        self.horizontalLayout_3.addWidget(self.code)
        self.numberedList = QtWidgets.QPushButton(self.editingButtons)
        self.numberedList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numberedList.setObjectName("numberedList")
        self.horizontalLayout_3.addWidget(self.numberedList)
        self.bullets = QtWidgets.QPushButton(self.editingButtons)
        self.bullets.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bullets.setCheckable(False)
        self.bullets.setDefault(False)
        self.bullets.setFlat(False)
        self.bullets.setObjectName("bullets")
        self.horizontalLayout_3.addWidget(self.bullets)
        self.heading = QtWidgets.QPushButton(self.editingButtons)
        self.heading.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.heading.setObjectName("heading")
        self.horizontalLayout_3.addWidget(self.heading)
        self.horizaontalRule = QtWidgets.QPushButton(self.editingButtons)
        self.horizaontalRule.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizaontalRule.setObjectName("horizaontalRule")
        self.horizontalLayout_3.addWidget(self.horizaontalRule)
        self.dateTime = QtWidgets.QPushButton(self.editingButtons)
        self.dateTime.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.dateTime.setObjectName("dateTime")
        self.horizontalLayout_3.addWidget(self.dateTime)
        self.encryptionButton = QtWidgets.QPushButton(self.editingButtons)
        self.encryptionButton.setObjectName("encryptionButton")
        self.horizontalLayout_3.addWidget(self.encryptionButton)
        self.decryptionButton = QtWidgets.QPushButton(self.editingButtons)
        self.decryptionButton.setObjectName("decryptionButton")
        self.horizontalLayout_3.addWidget(self.decryptionButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.editingButtons)
        self.editingSection = QtWidgets.QWidget(self.editorArea)
        self.editingSection.setObjectName("editingSection")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.editingSection)
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"border-color: rgba(252, 252, 252, 252);\n"
"\n"
"border-width:0px\n"
"")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.mdViewer = QtWidgets.QTextBrowser(self.editingSection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdViewer.sizePolicy().hasHeightForWidth())
        self.mdViewer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.mdViewer.setFont(font)
        self.mdViewer.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.mdViewer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdViewer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mdViewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdViewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdViewer.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.mdViewer.setObjectName("mdViewer")
        self.horizontalLayout_2.addWidget(self.mdViewer)
        self.verticalLayout_2.addWidget(self.editingSection)
        self.horizontalLayout_5.addWidget(self.editorArea)
        self.verticalLayout.addWidget(self.centralView)
        self.horizontalLayout_4.addWidget(self.mainWindow)
        Groot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Groot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1480, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menuEdit)
        self.menuFormat.setObjectName("menuFormat")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Groot.setMenuBar(self.menubar)
        self.actionNotes_Tree = QtWidgets.QAction(Groot)
        self.actionNotes_Tree.setObjectName("actionNotes_Tree")
        self.actionPrint = QtWidgets.QAction(Groot)
        self.actionPrint.setObjectName("actionPrint")
        self.actionQuit = QtWidgets.QAction(Groot)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMD = QtWidgets.QAction(Groot)
        self.actionMD.setObjectName("actionMD")
        self.actionMD_2 = QtWidgets.QAction(Groot)
        self.actionMD_2.setObjectName("actionMD_2")
        self.actionHTML = QtWidgets.QAction(Groot)
        self.actionHTML.setObjectName("actionHTML")
        self.actionPDF = QtWidgets.QAction(Groot)
        self.actionPDF.setObjectName("actionPDF")
        self.actionSearch_in_Current_Note = QtWidgets.QAction(Groot)
        self.actionSearch_in_Current_Note.setObjectName("actionSearch_in_Current_Note")
        self.actionSearch_in_All_Notes = QtWidgets.QAction(Groot)
        self.actionSearch_in_All_Notes.setObjectName("actionSearch_in_All_Notes")
        self.actionOptions = QtWidgets.QAction(Groot)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(Groot)
        self.actionAbout.setObjectName("actionAbout")
        self.actionRequest = QtWidgets.QAction(Groot)
        self.actionRequest.setObjectName("actionRequest")
        self.actionDark_Theme = QtWidgets.QAction(Groot)
        self.actionDark_Theme.setObjectName("actionDark_Theme")
        self.actionLight_Theme = QtWidgets.QAction(Groot)
        self.actionLight_Theme.setObjectName("actionLight_Theme")
        self.actionBold = QtWidgets.QAction(Groot)
        self.actionBold.setShortcutVisibleInContextMenu(True)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(Groot)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(Groot)
        self.actionUnderline.setObjectName("actionUnderline")
        self.menuImport.addAction(self.actionMD)
        self.menuExport.addAction(self.actionMD_2)
        self.menuExport.addAction(self.actionHTML)
        self.menuExport.addAction(self.actionPDF)
        self.menuFile.addAction(self.actionNotes_Tree)
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionQuit)
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuEdit.addAction(self.actionSearch_in_Current_Note)
        self.menuEdit.addAction(self.actionSearch_in_All_Notes)
        self.menuEdit.addAction(self.menuFormat.menuAction())
        self.menuView.addAction(self.actionDark_Theme)
        self.menuView.addAction(self.actionLight_Theme)
        self.menuTools.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionRequest)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Groot)
        QtCore.QMetaObject.connectSlotsByName(Groot)

    def retranslateUi(self, Groot):
        _translate = QtCore.QCoreApplication.translate
        Groot.setWindowTitle(_translate("Groot", "Groot"))
        self.newNote.setText(_translate("Groot", "New Note"))
        self.newNotebook.setText(_translate("Groot", "New Notebook"))
        self.newSubNotebook.setText(_translate("Groot", "New sub-notebook"))
        self.lineEdit.setPlaceholderText(_translate("Groot", "Search this note"))
        self.treeWidget.headerItem().setText(0, _translate("Groot", "Notes"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Groot", "Notebooks"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Groot", "Uncategorized"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.fileName.setText(_translate("Groot", "Testing Name"))
        self.pushButton_5.setText(_translate("Groot", "Bold"))
        self.pushButton_4.setText(_translate("Groot", "Italic"))
        self.pushButton_3.setText(_translate("Groot", "Image"))
        self.link.setText(_translate("Groot", "Link"))
        self.code.setText(_translate("Groot", "Code"))
        self.numberedList.setText(_translate("Groot", "Numbered List"))
        self.bullets.setText(_translate("Groot", "Bullets"))
        self.heading.setText(_translate("Groot", "Heading"))
        self.horizaontalRule.setText(_translate("Groot", "Horizontal Line"))
        self.dateTime.setText(_translate("Groot", "Date and Time"))
        self.encryptionButton.setText(_translate("Groot", "Encrypt"))
        self.decryptionButton.setText(_translate("Groot", "Decrypt"))
        self.plainTextEdit.setPlaceholderText(_translate("Groot", "Type here...."))
        self.menuFile.setTitle(_translate("Groot", "File"))
        self.menuImport.setTitle(_translate("Groot", "Import"))
        self.menuExport.setTitle(_translate("Groot", "Export"))
        self.menuEdit.setTitle(_translate("Groot", "Edit"))
        self.menuFormat.setTitle(_translate("Groot", "Format"))
        self.menuView.setTitle(_translate("Groot", "View"))
        self.menuTools.setTitle(_translate("Groot", "Tools"))
        self.menuHelp.setTitle(_translate("Groot", "Help"))
        self.actionNotes_Tree.setText(_translate("Groot", "Notes Tree"))
        self.actionPrint.setText(_translate("Groot", "Print"))
        self.actionQuit.setText(_translate("Groot", "Quit"))
        self.actionMD.setText(_translate("Groot", "MD"))
        self.actionMD_2.setText(_translate("Groot", "MD"))
        self.actionHTML.setText(_translate("Groot", "HTML"))
        self.actionPDF.setText(_translate("Groot", "PDF"))
        self.actionSearch_in_Current_Note.setText(_translate("Groot", "Search in Current Note"))
        self.actionSearch_in_All_Notes.setText(_translate("Groot", "Search in All Notes"))
        self.actionOptions.setText(_translate("Groot", "Options"))
        self.actionAbout.setText(_translate("Groot", "About"))
        self.actionRequest.setText(_translate("Groot", "Request"))
        self.actionDark_Theme.setText(_translate("Groot", "Dark Theme"))
        self.actionLight_Theme.setText(_translate("Groot", "Light Theme"))
        self.actionBold.setText(_translate("Groot", "Bold"))
        self.actionBold.setShortcut(_translate("Groot", "Ctrl+B"))
        self.actionItalic.setText(_translate("Groot", "Italic"))
        self.actionItalic.setShortcut(_translate("Groot", "Ctrl+I"))
        self.actionUnderline.setText(_translate("Groot", "Underline"))
        self.actionUnderline.setShortcut(_translate("Groot", "Ctrl+U"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Groot = QtWidgets.QMainWindow()
    ui = Ui_Groot()
    ui.setupUi(Groot)
    Groot.show()
    sys.exit(app.exec_())
