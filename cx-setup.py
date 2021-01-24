import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os"], 
    "excludes": ["tkinter"],
    "includes": ["src/cli.py"]
}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Python Covid",
        version = "1.2.0",
        description = "Covid python App!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("src/app.py", base=base)])