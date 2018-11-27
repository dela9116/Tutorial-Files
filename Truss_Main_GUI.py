import numpy as np

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Truss_Design_ui import Ui_Dialog
from Truss_Class import Truss

class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()

        #define two data items
        self.truss=None
        self.filename = None
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_GetWing.clicked.connect(self.GetTruss)

    def GetTruss(self):
        # get the filename using the OPEN dialog
        self.filename=QFileDialog.getOpenFileName()[0]
        if len(self.filename)==0:
            no_file()
            return
        self.ui.textEdit_filename.setText(self.filename)
        app.processEvents()

        # Read the file
        f1 = open(self.filename, 'r')  # open the file for reading
        data = f1.readlines()  # read the entire file as a list of strings
        f1.close()  # close the file  ... very important

        self.truss=Truss()  # create a Truss instance (object)


        self.truss.ReadTrussData(data)

        #fill the small text boxes
        self.ui.textEdit_nNodes.setText('{:5}'.format(self.truss.nNodes))
        self.ui.textEdit_xAverage.setText('{:10.2f}'.format(self.truss.xAverage))
        self.ui.textEdit_yAverage.setText('{:10.2f}'.format(self.truss.yAverage))

    def ExitApp(self):
        app.exit()


def no_file():
    msg = QMessageBox()
    msg.setText('There was no file selected')
    msg.setWindowTitle("No File")
    retval = msg.exec_()
    return None

def bad_file():
    msg = QMessageBox()
    msg.setText('Unable to process the selected file')
    msg.setWindowTitle("Bad File")
    retval = msg.exec_()
    return None


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()

    #if a filename exists at the beginning of the program .. open it
    # ... to save time in the debugging cycle
    name = main_win.filename
    if name is not None:
        main_win.GetTruss(name=main_win.filename)


    sys.exit(app.exec_())
    
 





