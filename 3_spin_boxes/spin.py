import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add title
        self.setWindowTitle("Spin Box")
        
        #set layout
        self.setLayout(qtw.QVBoxLayout())
        
        #Label
        my_label = qtw.QLabel("Pick Somthing From The List :")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)
        
        #Make the spin Box editable
        my_spin = qtw.QSpinBox(self,
                                value = 10,
                                maximum = 100,
                                minimum = 0,
                                singleStep = 5,
                                prefix = "#",
                                suffix = " order")
        my_spin.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_spin)
        
        
        #button
        my_button = qtw.QPushButton("Press Me" , clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()
        
        def press_it():
            my_label.setText(f"You Picked #{my_spin.value()} order!")
            
            
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()