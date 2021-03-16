import os
import sys
from cx_Freeze import setup, Executable

app_path = os.path.join(os.path.dirname(__file__), "ViewLogic.py")
base = "Win32GUI"

packages = ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets", "moviepy.editor"]
excludes = ["tkinter", "PyQt5.uic"]



setup(
    name = "VideoMerger",
    version = "0.0.1",
    options = {"build_exe": {"packages": packages, "excludes": excludes}},
    executables = [Executable(app_path, targetName="VideoMerger.exe", base=base)]
)