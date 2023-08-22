import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog

from Sources.Dialog.videoSelection import VideoSelectionDialog
from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_videos = []

        # sidebar toggle
        self.ui.widget_sidebar.hide()
        self.showSidebar = True
        self.ui.btn_toggle.clicked.connect(self.toggle_sidebar)

        self.ui.btn_home.clicked.connect(lambda: self.ui.widget_stacked.setCurrentWidget(self.ui.page_home))
        self.ui.btn_about.clicked.connect(lambda: self.ui.widget_stacked.setCurrentWidget(self.ui.page_about))
        self.ui.btn_quit.clicked.connect(lambda: self.close())

        # load videos
        self.video_list_widget = self.ui.video_list
        self.ui.btn_loadVideo.clicked.connect(self.load_videos)

    def load_videos(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        options |= QFileDialog.ShowDirsOnly

        selected_folder = QFileDialog.getExistingDirectory(self, "Select Folder with Videos", QDir.homePath(),
                                                           options=options)
        if selected_folder:
            self.ui.edit_pathDir.setText(selected_folder)
            video_files = [f for f in os.listdir(selected_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]

            dialog = VideoSelectionDialog(video_files, self)
            if dialog.exec():
                self.selected_videos = dialog.selected_videos
                self.update_video_list()

    def update_video_list(self):
        self.video_list_widget.clear()
        self.video_list_widget.addItems(self.selected_videos)

    def toggle_sidebar(self):
        if self.showSidebar:
            self.ui.widget_sidebar.show()
            self.ui.btn_toggle.setIcon(QIcon(":/icons/Resources/icons/arrow-left-circle.svg"))
        else:
            self.ui.widget_sidebar.hide()
            self.ui.btn_toggle.setIcon(QIcon(":/icons/Resources/icons/align-justify.svg"))
        self.showSidebar = not self.showSidebar


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
