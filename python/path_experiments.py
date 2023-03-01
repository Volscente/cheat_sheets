# Import Standard Libraries
from pathlib import Path
import os

path = Path.cwd()

print(path)
print(path.resolve())
print(os.path.abspath('./../data/diabetes.csv'))