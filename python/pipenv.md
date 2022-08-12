# Installation

``` shell
pip install pipenv
```

# Create Environment

## Open Shell
``` shell
pipenv shell
```

## Install Libraries
``` shell
pipenv install flask==0.12.1

# Install from VCS
pipenv install -e git+https://github.com/requests/requests.git#egg=requests

# Install for 'Development' enviroment
pipenv install pytest --dev
```

## Lock the Pipfile.lock
``` shell
pipenv lock
```

## Install Pipfile.lock
``` shell
pipenv install --ignore-pipfile

# Install only dependencies in the --dev packages
pipenv install --dev
```