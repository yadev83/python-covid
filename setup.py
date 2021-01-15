# setup.py
# Used to generate an exe file out of the app.py source
from distutils.core import setup
import py2exe
import sys

main_script_dir = "src\\app.py"
main_folder = main_script_dir.rsplit("\\",1)[0]
sys.path.append(main_folder)

setup(console=["src/app.py"]) 