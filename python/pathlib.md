# Path Object

## Create from Current Filepath
``` python
# Import Standard Libraries
from pathlib import Path

path = Path(__file__)
```

## Access Parents
``` python
# Import Standard Libraries
from pathlib import Path

path = Path(__file__)

parent_level_2 = path.parents[2]
```

## Cast Path to String
``` python
# Import Standard Libraries
from pathlib import Path

path = Path(__file__)

path_string = path.as_posix()
```