# example - Execute Python Scripts

This document introduces how to execute Python scripts on the command line or in the code.

### `example.exec`

```python
example.exec(filePath)
```

Executes the specified Python script file.

**Parameter**

* `filePath` - String type. Absolute path for Python script file execution.

**Example**

```python
# Assuming there is a test.py file

def myprint():
    count = 10
    while count > 0:
        count -= 1
        print('##### test #####')

myprint()

#Uploads test.py to the module, enters the command line and executes the following codes
>>> uos.listdir('/usr/')
['apn_cfg.json', 'test.py']
>>> import example
>>> example.exec('/usr/test.py')
# Execution results are as follows

##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
##### test #####
```
