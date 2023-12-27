# Introduction
## Definition
A *Shell Script* is just a list of commands that are executed by an interpreter, which is the Shell itself.

The interpreter is usually set at the top of the script by the so called *"Sharp Bang"* (#!) notation or *"Shebang"* (Contraction of Sharp Bang):
```bash
#!/bin/bash
```

The *Shebang* is used in order to pass the subsequent Shell path to the interpreter, so it knows what to use. So the process would actually be: `/bin/bash <script_path>.ph`.

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