from cx_Freeze import setup,Executable
import os,sys

os.environ['TCL_LIBRARY'] = r'C:/Users/agoum/AppData/Local/Programs/Python/Python37/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = r'C:/Users/agoum/AppData/Local/Programs/Python/Python37/tcl/tk8.6'

# includes = ["canopen_user","check","PID","QtUserWidget","sqlite_user","tab_op"]  # nommer les modules non trouves par cx_freeze
# includes = ["userlib"]  # nommer les modules non trouves par cx_freeze
excludes = ['Tkinter']
includes = ["pathlib","sys","functools","time","os","PyQt5","sqlite3","re","sys","math","pynput","pandas","numpy","subprocess"]  # nommer les modules utilises
packages = ["numpy","py_lib","public","matplotlib.backends.backend_tkagg","tkinter.filedialog"]  # nommer les packages utilises

includefiles = ["css","tcl86t.dll","remote.ico","tk86t.dll",r"C:\Users\agoum\AppData\Local\Programs\Python\Python37\Lib\site-packages\PyQt5\Qt\plugins\platforms\qwindows.dll"]


# niveau d'optimisation pour la compilation en bytecodes
optimize = 0
  
# si True, n'affiche que les warning et les erreurs pendant le traitement cx_freeze
silent = True

path = sys.path 
path.append('C:/Users/agoum/Documents/Programmation/python/remote_msgs')
path.append('C:/Users/agoum/Documents/Programmation/python/remote_msgs/py_lib')
path.append('C:/Users/agoum/Documents/Programmation/python/remote_msgs/public')

# path.append('C:\\users-data\\saf981896\\Documents\\02 - Applis\\python\\flodas')
# path.append('C:\\Users\\agoum\\Documents\\Programmation\\python\\remote_msgs\\py_lib')
# path.append('C:\\Users\\agoum\\Documents\\Programmation\\python\\remote_msgs\\public')
# path.append(os.path.join("userlib"))
# construction du dictionnaire des options
options = {"path": path,
          "packages": packages,
          "excludes":excludes,
          "includes":includes,
          "include_files": includefiles,
          "optimize": optimize,
          "silent": silent,
          "namespace_packages":['zope'],
          }

target = Executable(
    script="remote_msgs.py",
    base="Win32GUI",
    icon = "remote.ico",
    )

setup(
	name = "Remote msgs",
	version = "3.0",
	description = "Envoi automatique de message sur whatsapp",
	author="Jalil AGOUMI",
  author_email="agoumi.jalil@gmail.com",
	options={"build_exe": options},
	executables = [target],
	)