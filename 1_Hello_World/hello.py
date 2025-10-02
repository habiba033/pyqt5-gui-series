import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        ## WHERE WE WRITE THE CODE        
        #add a title
        self.setWindowTitle("Hello World !")
        
        #set a layout
        self.setLayout(qtw.QVBoxLayout())
        
        #create a label
        my_label = qtw.QLabel("Hello , What's your name ?")
        
        #change the font
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)
        
        #create an entry Box
        my_entre = qtw.QLineEdit()
        #box name
        my_entre.setObjectName("name_field")
        #Set text
        my_entre.setText("")
        self.layout().addWidget(my_entre)
        
        #create a button
        my_btn = qtw.QPushButton("Press Me" , 
                                clicked = lambda : press_it())
        self.layout().addWidget(my_btn)
        
        self.show()
        
        def press_it():
            # Add name to label
            my_label.setText(f"Hello ,{my_entre.text()}")
            #set the entre
            my_entre.setText("")
        
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()