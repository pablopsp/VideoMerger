import os
import sys
from cx_Freeze import setup, Executable

app_path = os.path.join(os.path.dirname(__file__), "ViewLogic.py")

# write_videofiles only works when base in None and cmd is not visible
base = None

setup(
    version = "0.0.1",
    executables = [Executable(app_path, target_name="VideoMerger.exe", base=base)]
)