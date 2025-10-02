import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add title
        self.setWindowTitle("Form")
        
        #set layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        #Label
        label_1 = qtw.QLabel("Cool Label Row!")
        label_1.setFont(qtg.QFont("Heltevica", 24))
        
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)
        
        
        #button
        my_button = qtw.QPushButton("Press Me" , clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        #Add rows
        form_layout.addRow(label_1)
        form_layout.addRow("first name :", f_name)
        form_layout.addRow("last name :" ,l_name)
        form_layout.addRow(my_button)
        
        
        self.show()
        
        def press_it():
            label_1.setText(f"You pressed the button {f_name.text()} {l_name.text()} !")
            
            
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()