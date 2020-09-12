def compile(source, tool="cx_Freeze"):
    if tool == "cx_Freeze":
        from cx_Freeze import setup, Executable
        options = {"build.exe" : {"includes" : ["os"]}}
        setup(name = "ListDir",
            version = "1.0",
            description = "Console utility",
            options = options,
            executables = [Executable("{0}".format(source))]
            )
    elif tool == "PyInstaller":
        import subprocess
        callstring = "pyinstaller {0} -F".format(source) # PyInstaller
        # callstring = "python setup.py build" # cx_Freeze
        subprocess.Popen(callstring, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

source = "listdir.py"
tool = "cx_Freeze"
tool = "PyInstaller"

compile(source, tool)
