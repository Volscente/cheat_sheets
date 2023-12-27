# Introduction
## Definition
A *Shell Script* is just a list of commands that are executed by an interpreter, which is the Shell itself.

The interpreter is usually set at the top of the script by:
```bash
#!/bin/bash
```

The example above uses the `bash` shell as interpreter, but it is also possible to use others like `zsh` or `ksh`.

## Executable
A Shell Script, in order to be executed, it needs to be granted with the *Execution* priviliges:
```bash
chmod 755 <script_path>.sh
```
Then we can execute the script:
```bash
./<script_path>.sh
```