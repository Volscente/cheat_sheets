# Import Standard Libraries
from pathlib import Path
import os

folder = 'data'

p = Path(__file__).parent.parent / folder
print(p)