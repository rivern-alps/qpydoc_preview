# example - 执行python脚本

提供方法让用户可以在命令行或者代码中执行python脚本。

### `example.exec`

```python
example.exec(filePath)
```

执行指定的python脚本文件。

**参数描述**

* `filePath`，string类型， 要执行python脚本文件的绝对路径

**示例**

```python
# 假设有文件test.py,内容如下

def myprint():
    count = 10
    while count > 0:
        count -= 1
        print('##### test #####')

myprint()

#将test.py文件上传到模块中，进入命令行执行如下代码
>>> uos.listdir('/usr/')
['apn_cfg.json', 'test.py']
>>> import example
>>> example.exec('/usr/test.py')
# 执行结果如下

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
