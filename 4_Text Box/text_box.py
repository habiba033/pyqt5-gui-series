import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add title
        self.setWindowTitle("Text Box")
        
        #set layout
        self.setLayout(qtw.QVBoxLayout())
        
        #Label
        my_label = qtw.QLabel("Write in the Box")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)
        
        #CREATE THE TEXT BOX
        my_txt = qtw.QTextEdit(self,
                            lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
                            lineWrapColumnOrWidth= 20,
                            placeholderText= "Hello ,There !",
                            readOnly = False,
                            #html = "<center><h1> that's a Big Header </h1></center>")
        )
        
        self.layout().addWidget(my_txt)
        
        #button
        my_button = qtw.QPushButton("Press Me" , clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()
        
        def press_it():
            my_label.setText(f"You Typed {my_txt.toPlainText()} !")
            my_txt.setText("You Pressed The Button")
            
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
    