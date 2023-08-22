import os
import sys

import cv2
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog, QHBoxLayout

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

        # menu button actions
        self.ui.btn_home.clicked.connect(lambda: self.ui.widget_stacked.setCurrentWidget(self.ui.page_home))
        self.ui.btn_about.clicked.connect(lambda: self.ui.widget_stacked.setCurrentWidget(self.ui.page_about))
        self.ui.btn_quit.clicked.connect(lambda: self.close())

        # load videos
        self.video_preview_grid = self.ui.video_preview
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
                self.update_video_preview_grid()

    def update_video_preview_grid(self):
        self.clear_video_preview_grid()
        thumbnail_container = QtWidgets.QWidget()
        thumbnail_layout = QHBoxLayout(thumbnail_container)

        for video_filename in self.selected_videos:
            video_path = os.path.join(self.ui.edit_pathDir.text(), video_filename)
            capture = cv2.VideoCapture(video_path)

            if not capture.isOpened():
                print(f"Failed to open video: {video_path}")
                continue

            success, frame = capture.read()

            if success:
                thumbnail_widget = QtWidgets.QLabel()
                thumbnail_widget.setMaximumSize(150, 150)  # Adjust size as needed

                # Convert OpenCV frame to QImage
                qimage = QImage(
                    frame.data,
                    frame.shape[1],
                    frame.shape[0],
                    frame.shape[1] * 3,
                    QImage.Format_RGB888)

                # Convert QImage to QPixmap for thumbnail display
                pixmap = QPixmap.fromImage(qimage).scaled(
                    thumbnail_widget.size(),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation,
                )

                thumbnail_widget.setPixmap(pixmap)
                thumbnail_layout.addWidget(thumbnail_widget)

            capture.release()

            self.video_preview_grid.addWidget(thumbnail_container)

    def clear_video_preview_grid(self):
        for i in reversed(range(self.video_preview_grid.count())):
            item = self.video_preview_grid.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    widget.hide()
                    self.video_preview_grid.removeItem(item)

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
