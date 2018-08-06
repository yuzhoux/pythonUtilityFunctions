# My Python Utility Functions

**1. dynamicCommands.py**

This python function replaces a parameterized command with input variables and time variables. It helps with running the same command across subsets and time periods. 

```
hive-shell -q "./dynamicCommands.py file_name=query.sql regionVar=USA"
```
**2. modelSetup.py**

This python file has steps and functions for common tasks in modeling setup: loading data from csv files, encoding categorical variables, train-test split and model export. 

**3. pysparkFeatureEngineering.py**

This pyspark file has functions to manipulate many variables together. In big data projects, the number of variables is large, therefore we need functions to manipulate a list of variables together instead of doing so one by one. 

**4.subProcess.py**

This python function submit a SQL statement to target query engine.