#hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(200, 100, 100, 100)
helloMsg = QLabel("<h1>jeevan wa ki jai ho....!</h1>", parent=window)
helloMsg.move(60, 60)
helloMsg.setStyleSheet("color: pink")

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec()) 