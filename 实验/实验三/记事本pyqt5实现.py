import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        
        self.createActions()
        self.createMenus()
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('记事本')
        self.show()

    def createActions(self):
        self.newAct = QAction(QIcon('new.png'), '新建', self)
        self.newAct.setShortcut('Ctrl+N')
        self.newAct.triggered.connect(self.newFile)

        self.openAct = QAction(QIcon('open.png'), '打开', self)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.triggered.connect(self.openFile)

        self.saveAct = QAction(QIcon('save.png'), '保存', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.triggered.connect(self.saveFile)

        self.saveAsAct = QAction('另存为', self)
        self.saveAsAct.triggered.connect(self.saveFileAs)

        self.undoAct = QAction('撤销', self)
        self.undoAct.setShortcut('Ctrl+Z')
        self.undoAct.triggered.connect(self.textEdit.undo)

        self.redoAct = QAction('重做', self)
        self.redoAct.setShortcut('Ctrl+Y')
        self.redoAct.triggered.connect(self.textEdit.redo)

        self.cutAct = QAction('剪切', self)
        self.cutAct.setShortcut('Ctrl+X')
        self.cutAct.triggered.connect(self.textEdit.cut)

        self.copyAct = QAction('复制', self)
        self.copyAct.setShortcut('Ctrl+C')
        self.copyAct.triggered.connect(self.textEdit.copy)

        self.pasteAct = QAction('粘贴', self)
        self.pasteAct.setShortcut('Ctrl+V')
        self.pasteAct.triggered.connect(self.textEdit.paste)

        self.selectAllAct = QAction('全选', self)
        self.selectAllAct.setShortcut('Ctrl+A')
        self.selectAllAct.triggered.connect(self.textEdit.selectAll)

        self.aboutAct = QAction('关于', self)
        self.aboutAct.triggered.connect(self.about)

    def createMenus(self):
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('文件')
        fileMenu.addAction(self.newAct)
        fileMenu.addAction(self.openAct)
        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.saveAsAct)

        editMenu = menubar.addMenu('编辑')
        editMenu.addAction(self.undoAct)
        editMenu.addAction(self.redoAct)
        editMenu.addAction(self.cutAct)
        editMenu.addAction(self.copyAct)
        editMenu.addAction(self.pasteAct)
        editMenu.addAction(self.selectAllAct)

        aboutMenu = menubar.addMenu('关于')
        aboutMenu.addAction(self.aboutAct)

    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '文本文件 (*.txt);;所有文件 (*)')
        if fname:
            with open(fname, 'r', encoding='utf-8') as f:
                self.textEdit.setText(f.read())

    def saveFile(self):
        if not hasattr(self, 'currentFile'):
            self.saveFileAs()
        else:
            with open(self.currentFile, 'w', encoding='utf-8') as f:
                f.write(self.textEdit.toPlainText())

    def saveFileAs(self):
        fname, _ = QFileDialog.getSaveFileName(self, '另存为', '', '文本文件 (*.txt);;所有文件 (*)')
        if fname:
            self.currentFile = fname
            self.saveFile()

    def about(self):
        QMessageBox.about(self, '关于', '作者: Your Name\n版权: Your Company')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())