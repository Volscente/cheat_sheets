# Common Errors
## Impossible to Import
Create a `.pylintrc` file inside the root directory of the project with the following content:
```
[MASTER]
init-hook='import sys; sys.path.append("/Users/s.porreca/Projects/<repository_name>/src")'
```
