import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # add title
        self.setWindowTitle("Combo Box")
        
        #set layout
        self.setLayout(qtw.QVBoxLayout())
        
        #Label
        my_label = qtw.QLabel("Pick Somthing From The List :")
        my_label.setFont(qtg.QFont('Helvetica', 25))
        self.layout().addWidget(my_label)
        
        #Make the combo Box editable
        my_combo = qtw.QComboBox(self,
                                editable = True,
                                insertPolicy = qtw.QComboBox.InsertAtBottom)
        
        my_combo.addItem("pepproni","item 1")
        my_combo.addItem("mashrom","item 2")
        my_combo.addItem("pinapple",3)
        my_combo.addItem("cheese",4)
        
        my_combo.addItems(["one","two","three"])
        
        #insert item in specific index
        my_combo.insertItem(2,"THird thing")
        self.layout().addWidget(my_combo)
        #button
        my_button = qtw.QPushButton("Press Me" , clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        
        self.show()
        
        def press_it():
            my_label.setText(f"You Picked {my_combo.currentText()} !")
            
            
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()