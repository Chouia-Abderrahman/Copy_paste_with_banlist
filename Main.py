import sys
from PyQt5.QtWidgets import QApplication
from Logic import windows

app = QApplication(sys.argv)
calculator = windows()

sys.exit(app.exec_())