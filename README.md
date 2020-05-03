# How to convert .py to .exe

### Step1
We'll need a Python program from which to build our executable. For this example, i'm using a simple script that print string.

**demo.py**  

```python
import numpy as np 

a = np.array([1,2,3,4,5,6])
print("my_array: ", a)
print("Hello!")
for i in range(10):
    print("CS_UIT")
```

### Step2
This process is almost as simple with cx_freeze, but requires an extra configuration step. Before running cx_freeze, you'll need yo create a file called "setup.py" that is stored in the same folder as the *demo.py* program. The *setup.py* file configures the options for cx_freeze, and can get complicated if you're trying to do something very particular. For example:  

```python
from cx_Freeze import setup, Executable

setup(name="Hello_UIT!",
    version = "0.1",
    description = "demo",
    executables = [Executable("demo.py")])
```

To run cx_freeze, you can now:  
1. Navigate to the folder containing demo.py and setup.py  
2. Run the command:  *python3 setup.py build*

### Simplicity vs Configurability
While the setup file required by cx_freeze present an additional step in the process, it also anables great flexibility. In the setup file you can specify which modules, files, and packages to include (or exclude). You can set a target name for your executable, as well as a path to the icon that should be used to represent it. There's also an option to set chosen environment variables upon installation. All this helps you to deliver an executable that matches your needs precisely.  

### Reference
[How To Convert .Py To .Exe](https://www.activestate.com/blog/how-to-convert-py-to-exe/)
