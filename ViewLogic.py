import os
import sys
import multiprocessing
import threading
import logging
import warnings
from pathlib import Path
from itertools import groupby

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool
from threading import Thread
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

from View import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        logTextBox = QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter(
            '%(levelname)s - %(message)s')
        )
        logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
        logging.getLogger().addHandler(logTextBox)
        logging.getLogger().setLevel(logging.INFO)

        # Ignore moviepy warnings
        warnings.filterwarnings("ignore")
        
        self.look_for_dir_button.clicked.connect(self.open_file_dialog)
        self.init_video_maker.clicked.connect(self.init_merge)
    
    
    def open_file_dialog(self):
        self.folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Seleccione la carpeta que contiene los videos')
        if(self.folderPath):
            self.dir_name.setText(self.folderPath)
            self.init_video_maker.setDisabled(False)
            logging.info(f"Ruta carpeta de videos: {self.folderPath}")


    def init_merge(self):
        # First group by name of the .mp4 files
        mp4_paths = [path for path in Path(self.folderPath).rglob('*.mp4') if not 'merged' in path.__str__()]

        if len(mp4_paths) != 0:
            group_by_path = [{key: list(group)} for key, group in groupby(mp4_paths, lambda x: os.path.split(x)[0])]
            # Groupby path, file dir and file name
            arranged_files = {}
            for group in group_by_path:
                for path, values in group.items():
                    path_files = {}
                    for key, group in groupby(values, lambda x: os.path.split(x)[1].split('-')[0]):
                        path_files[key] = list(group)
                    arranged_files[path] = path_files

            for path, files_paths in arranged_files.items():
                result_path = f"{path}\\merged"
                if not os.path.exists(result_path):
                    os.mkdir(result_path)

                # Concatenate videos by folder dir and file name with 6000 kbps bitrate
                for key_file, path_list in files_paths.items():
                    prcs = ProcessRunnable(target=self.concatenate_videos, args=(result_path, key_file, path_list))
                    prcs.start()
            logging.info("Union de videos finalizada")
        
        else:
            logging.info("No hay ningun video para unir en el directorio actual")
            

    def concatenate_videos(self, result_path, key_file, path_list):
        temp_result_file_path = f"{result_path}\\{key_file}.temp.mp4"
        result_file_path = f"{result_path}\\{key_file}.mp4"

        if not os.path.exists(result_file_path):
            logging.info(f"Uniendo video: {key_file}.mp4")

            videoclips = [VideoFileClip(video.__str__(), audio=False) for video in path_list]
            final_clip = concatenate_videoclips(videoclips)
            final_clip.write_videofile(temp_result_file_path, bitrate="6000k", threads=multiprocessing.cpu_count(), verbose=False, codec="libx264")
            
            os.rename(temp_result_file_path, result_file_path)

            logging.info(f"Video unido en la ruta: {result_file_path}")
    
        elif os.path.exists(temp_result_file_path):
            os.remove(temp_result_file_path)
            self.concatenate_videos(result_path, key_file, path_list)
        


class QTextEditLogger(logging.Handler, QtCore.QObject):
    appendPlainText = QtCore.pyqtSignal(str)
    def __init__(self, parent):
        super().__init__()
        QtCore.QObject.__init__(self)
        self.widget = QtWidgets.QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        self.widget.setObjectName("logging_text")
        self.widget.setGeometry(QtCore.QRect(40, 100, 321, 171))
        self.appendPlainText.connect(self.widget.appendPlainText)
    
    def emit(self, record):
        msg = self.format(record)
        self.appendPlainText.emit(msg)        



class ProcessRunnable(QRunnable):
    def __init__(self, target, args):
        QRunnable.__init__(self)
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)

    def start(self):
        QThreadPool.globalInstance().start(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    window.show()
    sys.exit(app.exec_())