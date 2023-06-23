import shutil

from PyQt5 import QtWidgets
from Gui_file import Ui_Dialog
import datetime
from datetime import datetime
import os

class windows(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        #   C:\Users\Abdou\Desktop\models results
        #   C:\Users\Abdou\Desktop\dsds
        def copy_directory():
            src = str(self.source_txt.text())
            dst = str(self.destination_txt.text())
            ban_list = str(self.banlist_txt.text()).split(",")
            if os.path.isdir(src) and os.path.isdir(dst):
                for item in os.listdir(src):
                    src_item = os.path.join(src, item)
                    dst_item = os.path.join(dst, item)

                    if os.path.isdir(src_item):
                        if item not in ban_list:
                            if os.path.exists(dst_item):
                                print("file or folder exists with the same name",dst_item)
                            else:
                                shutil.copytree(src_item, dst_item, ignore=shutil.ignore_patterns(*ban_list))
                    else:
                        if item not in ban_list:
                            shutil.copy2(src_item, dst_item)
            else:
                print("not a valid directory")

        self.copy_btn.clicked.connect(copy_directory)