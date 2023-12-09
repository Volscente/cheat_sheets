# Issues
## Pylint Compatibility
- It is required to add [pylint-pytest package](https://pypi.org/project/pylint-pytest/).
- Then configure pylint to use the plugin:
    ```bash
    pylint --load-plugins pylint_pytest
    ```
- Finally, configure PyCharm:
    ![PyCharm Pylint Configuration](./../images/python/python_1.png)

## Suppress Google Cloud Bigquery Warning
Add the following lines of code in the `pyproject.toml`
```toml
[tool.pytest.ini_options]
# Filter deprecation warning from google-cloud-bigquery
filterwarnings = [
    "ignore:Deprecated call to `pkg_resources\\.declare_namespace\\('.*'\\):DeprecationWarning",
    "ignore::DeprecationWarning:google.rpc",
]
pythonpath = [
  "src"
]
```
