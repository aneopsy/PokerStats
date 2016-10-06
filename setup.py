from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

DATA=[('platforms',[
    'C:\Python34\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll'
    ])]

for files in os.listdir(os.path.join(os.getcwd(),'UI')):
    f1 = os.path.join(os.getcwd(),'UI', files)
    if os.path.isfile(f1):
        f2 = 'UI', [f1]
        DATA.append(f2)

setup(
    options = {'py2exe': {'compressed': True,"includes":["sip"]}},
    windows = [{
                   'script': "main.py",
                   "icon_resources": [(1, os.path.join(os.getcwd(),"resources","converted_icon.ico"))],
                   "dest_base":"PokerStats",
               }],
    zipfile = None,
    data_files = DATA,
)
