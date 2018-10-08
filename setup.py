from cx_Freeze import setup , Executable
setup (name = "Calculator " ,
       version = "1.0" ,
       author = "Somesh Kalyankar" ,
       description = "This Software is use for calculating expressions." ,
       executables = [Executable(r"/home/ironman/Desktop/c.py" ,
                                 icon = r"/home/ironman/desktop-rocket.png",
                                 shortcutName = "Calculator",
                                 shortcutDir = "DesktopFolder")]
       )
