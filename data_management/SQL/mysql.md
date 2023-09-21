# General
## Installation
Download and install `MySQL` from the following [link](https://dev.mysql.com/downloads/mysql/).

Once installed, you can start `MySQL` by locating the corresponding application in the `System Preferences`.

It is also recommended to add the `mysql` executable to the `PATH` variable:
```bash
export PATH="/usr/local/mysql/bin/mysql:$PATH"
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
```

# Commands
## Start & Stop
You can either go under `System Preference/mysql` on MacOS or in the directory `/usr/local/mysql/support-files` and type:
```bash
sudo ./mysql.server start
```

## Login to the CLI
```bash
mysql -h localhost -u root -p
```
