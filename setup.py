from cx_Freeze import setup, Executable

setup(name="Hello_UIT!",
    version = "0.1",
    description = "demo",
    executables = [Executable("demo.py")])
